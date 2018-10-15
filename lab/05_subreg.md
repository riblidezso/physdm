### Subset selection, regularization

1, Forward stepwise selection
- (-), Download data from http://science.sciencemag.org/content/early/2018/01/17/science.aar3247 (has been a previous hw)
- (-), Load protein levels, and convert them to numerical values if necessary (has been a previous hw)
- (-), Inspect missing values, and drop patients with missing values in protein levels (has been a previous hw)
- (-), Load cancer labels (has been a previous hw)
- (A), Perform forward iterative subset selection using statsmodels logistic regression when predicting the cancer/normal binary labels using protein levels as inputs. Use the log-likelihood values to select the best additional variable in each iteration.


2, Subset selection
- (A), Plot the AIC and the BIC criterion values depending on the number of variables during forward subset selection. Interpret the result based on the formulas for the 2 criteria!
- (B), Plot the AUC from a 5-fold cross validation (use sklearn KFold with random_state=0), depending on the number of variables during forward model selection. What do you see compared to the curves from AIC, and BIC?


3, Comparison of tools
- (-), Estimate the AUC of a fit with 5-fold cross validation  (use sklearn KFold with random_state=0) using the logistic regression from statsmodels using all variables. (has been a previous hw)
- (-), Repeat it with logistic regression fom sklearn. (has been a previous hw)
- (A), Sci-kit learn  will be less accurate than statsmodels in this dataset. What are the resons behind the difference? 
- (B), Try to fix the problems, and produce a fit witk sklearn which has a 5-fold CV AUC very close (diff<0.0001) to the one with statmodels.

4, Large dimensional regression
- Load the prepared data file "methyl.csv" (Which is a subset of the data from the article: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3780611/ )
- (A), Predict the age of people based on methylation values, using linear regression with a 80-20% train-test split (use sklearn train-test split with random_state=0). Plot the scatterplot of true values vs predictions for both the training and the testing set, what do you see?
- (B), Plot the MSE with 5 fold CV, using Ridge regression, depending on the penalty threshold. Find and optimal penalty value.
- (C), Plot the MSE with 5 fold CV, using lasso regression, depending on the penalty threshold. Find and optimal penalty value. Inspect how many coefficients are 0?
- (D), Use the best model found by the methods above to predict age from methylation with a 80-20% train-test split (use sklearn train-test split with random_state=0). Plot the scatterplot of true values vs predictions for both the training and the testing set.


5, Shrinkage and coefficient selection
- (A), Show on one plot each coefficient with a line using Ridge regression, depending on the penalty threshold. 
- (B), Show on one plot each coefficient with a line using Lasso regression, depending on the penalty threshold. 
- (C), Reuse your code form 1,2 and: Perform forward iterative subset selection with linear regression (**use sklearn its much faster**). Use the R-squared values to select the best additional variable in each iteration. Plot the AIC and the BIC values and MAE from 5-fold cross validation (use sklearn KFold with random_state=0) depending on the number of variables during forward model selection. Which is the best number of variables? **This will take quite some time, at least go up to 150 variables selected.**
- (D), Use the best linear regression model found by forward subset selection to predict age from methylation with a 80-20% train-test split (use sklearn train-test split with random_state=0). Plot the scatterplot of true values vs predictions for both the training and the testing set. How does it look compared to 4/(D)?



