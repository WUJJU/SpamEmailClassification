%task1
load('forsvm3.data')
X=forsvm3(:,1:66);
Y=forsvm3(:,67);

 %normalized and center the data
[nSmp,nFea] = size(X);
for i = 1:nSmp
     X(i,:) = X(i,:) ./ max(1e-12,norm(X(i,:)));
end
%Center Data
X=centerData(X);



% split data into balanced set
Xn=size(X,1);
R=randperm(Xn);
size(R)
Rn=size(R,2);
split_p=round(Rn*0.8);

indices=R(1:split_p);
indices2=R(split_p+1:end);
size(indices)
Xtrain=X(indices,:);
Ytrain=Y(indices,:);
%Ytrain2=ngnd(indices,:);
Xtest=X(indices2,:);
Ytest=Y(indices2,:);
%Ytest=ngnd(indices2,:);
%cross validation k-fold
k=5;
N=size(Xtrain,1)
indices=crossvalind('Kfold',N,k);
%bestweight=zeros(37,38);
acc =0;
MAP =0;
for i=1:5
disp(['fold: ' num2str(i)])  
    test=(indices==i);
    train=~test;
    XtrainR=Xtrain(train,:);
    YtrainR=Ytrain(train,:);
     XtestR=Xtrain(test,:);
    YtestR=Ytrain(test,:);
    %size(XtrainR)
    size(YtrainR)
     
   rmodel = svmtrain(YtrainR, XtrainR,'-t 2 -c 1000 -g 0.1 ');
    [predict_label, accuracy, dec_values] =svmpredict(YtestR, XtestR, rmodel);
      acc = acc+accuracy(1);
  
end    
accaverage = acc/5

%RSVModel = svmtrain(Ytrain, Xtrain, '-t 2 -c 10000 -g 0.01');
%[predict_label1, accuracy1, dec_values1] =svmpredict(Ytest, Xtest, RSVModel);
%accuracy1