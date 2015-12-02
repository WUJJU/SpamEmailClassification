from __future__ import division
import re
import math
import os

def sampletest(cl):
    path3='/Users/wuhao/Desktop/MachineLearning/FinalProject/enron1copy/spamTest/'   
    path4='/Users/wuhao/Desktop/MachineLearning/FinalProject//enron1copy/hamTest/'
    right=0
    #test total number
    ttn=0
    for filename in os.listdir(path3):
        os.chdir(path3)
        f=open(filename,'r')
        ttn+=1
        content=f.read()
        cater=cl.classify(content,default='ham')
        if cater=='spam':
            right+=1
            
    for filename in os.listdir(path4):
        os.chdir(path4)
        f=open(filename,'r')
        ttn+=1
        content=f.read()
        cater=cl.classify(content,default='ham')
        if cater=='ham': right+=1
    print right
    print ttn
    accuracy=right/ttn
    return accuracy
        
def sampletrain(cl):
    path1='/Users/wuhao/Desktop/MachineLearning/FinalProject/enron1copy/spam/'
    path2='/Users/wuhao/Desktop/MachineLearning/FinalProject/enron1copy/ham/'
    n1=0
    n2=0
    for filename in os.listdir(path1):
        os.chdir(path1)
        f=open(filename,'r')
        content=f.read()
        n1+=1
        print n1,filename,len(content)
        cl.train(content,'spam')
        f.close()
    
    for filename in os.listdir(path2):
        os.chdir(path2)
        f=open(filename,'r')
        n2+=1
        content=f.read()
        print n2,filename,len(content)
        cl.train(content,'ham')
        f.close()
    
           
def getwords(doc):
    splitter=re.compile('\\W*')
    #print doc
    # Split the words by non-alpha characters
    words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]

    # Return the unique set of words only
    return dict([(w,1) for w in words])

class classifier():
    def __init__(self,getfeatures,filename=None):
        # Counts of feature/category combinations
        self.fc={}
        # Counts of documents in each category
        self.cc={}
        self.getfeatures=getfeatures

    # Increase the count of a feature/category pair
    def incf(self,f,cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat]+=1

    # Increase the count of a category
    def incc(self,cat):
        self.cc.setdefault(cat,0)
        self.cc[cat]+=1

    # The number of times a feature has appeared in a category
    def fcount(self,f,cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0

    # The number of items in a category
    def catcount(self,cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0

    # The total number of items
    def totalcount(self):
        return sum(self.cc.values())

    # The list of all categories
    def categories(self):
        return self.cc.keys()

    def train(self,item,cat):
        features=self.getfeatures(item)
        # Increment the count for every feature with this category
        for f in features:
            self.incf(f,cat)

        # Increment the count for this category
        self.incc(cat)
    def fprob(self,f,cat):
        if self.catcount(cat)==0: return 0
        return self.fcount(f,cat)/self.catcount(cat)
    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        basicprob=prf(f,cat)
        totals=sum([self.fcount(f,c) for c in self.categories()])
        bp=((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp
    
class naivebayes(classifier):
    def __init__ (self,getfeatures):
        classifier.__init__(self,getfeatures)
        self.thresholds={}

    def setthreshold(self,cat,t):
        self.thresholds[cat]=t

    def getthreshold(self,cat):
        if cat not in self.thresholds: return 1.0
        return self.thresholds[cat]
    
    def docprob(self,item,cat):
            features=self.getfeatures(item)
            
            p=1
            for f in features:  p*=self.weightedprob(f,cat,self.fprob)
            return p
    def prob(self,item,cat):
            catprob=self.catcount(cat)/self.totalcount()
            #print catprob
            docprob=self.docprob(item,cat)
            return docprob*catprob

    def classify(self,item,default=None):
        probs={}
        max=0.0
        best='ham'
        for cat in self.categories():
            probs[cat]=self.prob(item,cat)
            if probs[cat]>max:
                max=probs[cat]
                best=cat
        for cat in probs:
            if cat==best: continue
            if probs[cat]*self.getthreshold(best)>probs[best]:return default
        return best
        
  
