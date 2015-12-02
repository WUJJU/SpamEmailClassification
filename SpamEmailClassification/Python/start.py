import spamBayes
cl=spamBayes.naivebayes(spamBayes.getwords)
spamBayes.sampletrain(cl)
spamBayes.sampletest(cl)