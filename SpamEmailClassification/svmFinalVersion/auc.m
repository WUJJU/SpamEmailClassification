function area = auc(Output, Target)
%AUC Compute area under ROC curve
%
%  Usage: area = auc(Output, Target)
%
%  Parameters: Output   - Vector of classifier output values 
%              Target   - Vector of targets (+/-1)
%              area     - area under ROC curve
%
%  Author: Steve Gunn (srg@ecs.soton.ac.uk)

if (nargin ~= 2) % check correct number of arguments
    help auc
else
    
    correct = 0; 
    valid = 0;
    for i=1:length(Target)-1
        for j=i+1:length(Target)
            if (Target(i) ~= Target(j))
                valid = valid + 1;
                if (Output(i) == Output(j))
                    correct = correct + 1;
                elseif (Target(i) == -1)
                    if (Output(i) < Output(j))
                        correct = correct + 2;
                    end
                else
                    if (Output(i) > Output(j))
                        correct = correct + 2;
                    end
                end
            end
        end
    end
    if valid == 0 
        area = 0;
    else
        area = correct/(2*valid);
    end
end