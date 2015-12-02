function acc = accuracy(trueY, predictedY, ranking) 
%Compute the accuracy of a set of predictions for binary labels 
%In the multi label case, all labels must be correct for 1 example

if (nargin < 2)
    fprintf('%s\n', help(sprintf('%s', mfilename)));
    error('Incorrect number of inputs - see above usage instructions.');
end

[numExamples, numLabels] = size(trueY);

acc = sum(sum(trueY == predictedY, 2) == numLabels)/(numExamples);