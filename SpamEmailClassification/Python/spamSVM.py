from __future__ import division
import os
import re


#dic={'make':1,'address':2,'all':3,'3d':4,'over':5,'remove':6,'internet':7,'order':8,'mail':9,'receive':10,'will':11,'people':12,'report':13,'addresses':14,'free':15,'business':16,'email':17,'you':18,'credit':19,'your':20,'font':21,'000':22,'money':23,'hp':24,'hpl':25,'george':26,'650':27,'lab':28,'labs':29,'telnet':30,'857':31,'data':32,'415':33,'85':34,'technology':35,'1999':36,'parts':37,'pm':38,'direct':39,'cs':40,'meeting':41,'original':42,'project':43,'re':44,'edu':45,'table':46,'conference':47,'our':48,';':49,'(':50,'[':51,'!':52,'$':53,'#':54,'shipping':55,'today':56,'here':57,'available':58,'online':59}
dic={'make':1,'address':2,'all':3,'3d':4,'over':5,'remove':6,'internet':7,'order':8,'mail':9,'receive':10,'will':11,'people':12,'report':13,'addresses':14,'free':15,'business':16,'email':17,'you':18,'credit':19,'your':20,'font':21,'000':22,'money':23,'hp':24,'hpl':25,'george':26,'650':27,'lab':28,'labs':29,'telnet':30,'857':31,'data':32,'415':33,'85':34,'technology':35,'1999':36,'parts':37,'pm':38,'direct':39,'cs':40,'meeting':41,'original':42,'project':43,'re':44,'edu':45,'table':46,'conference':47,'our':48,';':49,'(':50,'[':51,'!':52,'$':53,'#':54,'shipping':55,'today':56,'here':57,'available':58,'online':59,'certified':60,'hot':61,'guarantee':62,'fast':63,'rates':64,'opportunity':65,'discount':66}
#,'certified':60,'hot':61,'guarantee':62,'fast':63,'rates':64,'opportunity':65,'discount':66
def sampletrain():
    path1='/Users/wuhao/Desktop/MachineLearning/FinalProject/enron1/spam/'
    path2='/Users/wuhao/Desktop/MachineLearning/FinalProject/enron1/ham/'
    n1=0
    n2=0
 
    for filename in os.listdir(path1):
        os.chdir(path1)
        f=open(filename,'r')
        content=f.read()
        n1+=1
        print n1,filename,len(content)
        train(content,'spam')
        f.close()
    for filename in os.listdir(path2):
        os.chdir(path2)
        f=open(filename,'r')
        content=f.read()
        n1+=1
        print n1,filename,len(content)
        train(content,'ham')
        f.close()
        
def writeout(dicwrite,cat):
    path3='/Users/wuhao/Desktop/MachineLearning/FinalProject/enron1/'
    os.chdir(path3)
    f=open('forsvm4.data','a')
    for d in dic:
        if dicwrite.has_key(d):
            f.write(str(dicwrite[d])+',')
        else:  f.write(str(0)+',')
    if cat=='spam': f.write(str(1)+'\n')
    else: f.write(str(0)+'\n')
    f.close()
    
def getwords(doc):
    splitter=re.compile('\\W*')
    arraywords=[]
    #print doc
    # Split the words by non-alpha characters
    words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]
    for w in words:
        arraywords.append(w)
        

    # Return the all words in single file
    return arraywords


def train(item,cat):
        global dic
        features=getwords(item)
        dicwrite={}
        # Increment the count for every feature with this category
        for f in features:
            if dic.has_key(f):
                dicwrite[f]=features.count(f)/len(features)


        writeout(dicwrite,cat)

        
                



