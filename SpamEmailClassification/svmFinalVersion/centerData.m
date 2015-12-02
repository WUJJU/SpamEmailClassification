function [cX1, cX2, means] = centerData(X1, X2) 
% Centers matrices X1 (and optionally X2) by taking the mean of each column 
% (feature) of X1 and subtracting it from the feature values.
%
% Usage: [cX1, cX2] = centerData(X1, X2) 
% Inputs/Outputs: 
%   X1 - an (l x n) matrix whose rows are examples
%   X2 (optional) - an (l2 x m) matrix whose rows are examples
%
%   cX1 - centered X1 
%   cX2 (optional) - centered X2 
%
% Copyright (C) 2006 Charanpal Dhanjal 

% This library is free software; you can redistribute it and/or
% modify it under the terms of the GNU Lesser General Public
% License as published by the Free Software Foundation; either
% version 2.1 of the License, or (at your option) any later version.
% 
% This library is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
% Lesser General Public License for more details.
% 
% You should have received a copy of the GNU Lesser General Public
% License along with this library; if not, write to the Free Software
% Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
% USA

if (nargin < 1)
    fprintf('%s\n', help('centerData'));
    error('Incorrect number of inputs - see above usage instructions.');
end

fprintf('Centering %d x %d matrix\n', size(X1, 1), size(X1, 2)); 

numX1Examples = size(X1, 1);
meanX1 = mean(X1);

if (nargin == 1)
    cX1 = X1 - ones(numX1Examples, 1)*meanX1;
    cX2 = meanX1; 
else 
    vprintf('Centering %d x %d matrix\n', size(X2, 1), size(X2, 2)); 
    numX2Examples = size(X2,1);
    cX1 = X1 - ones(numX1Examples, 1)*meanX1;
    cX2 = X2 - ones(numX2Examples, 1)*meanX1;
    means = meanX1;
end
