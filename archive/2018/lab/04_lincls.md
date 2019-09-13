### Linear methods in classification

1, Load data
- (A), Download data from http://science.sciencemag.org/content/early/2018/01/17/science.aar3247
- (B), Load protein levels, and convert them to numerical values if necessary
- (C), Inspect missing values, and drop patients with missing values in protein levels
- (D), Load cancer labels

2, Logisic regression with Statsmodels
- (A), Fit a logistic regression using statsmodels to cancer/normal binary labels using protein levels as inputs
- (B), Evaluate the logloss and the accuracy of the fit.
- (C), Evaluate the ROC, and AUC of the fit.

3, Hepatocellular carcinoma 
- (A), Fit a logistic regression using statsmodels to Hepatocellular carcinoma (liver cancer)/normal binary labels.
- (B), Select the 4 most significant proteins and repeat the fit.
- (C), Select the 1 most significant protein and repeat the fit.
- (D), Compare the ROC, and AUC of the fits with 4 and 1 proteins. Which would you use when screening for cancers?
- (E), Interpret the results using the wikipedia page of Hepatocellular carcinoma. 

4, Cross validation
- (A), Fit logistic regression using statsmodels to cancer/normal binary labels using protein levels as inputs using 5 fold cross-validation
- (B), Calculate the mean and the std of AUC values for the 5 folds, and plot the 5 ROC curves on the same plot.

5, Sklearn
- (A), Fit a logistic regression using scikit-learn to cancer/normal binary labels using protein levels as inputs
- (B), Compare the coefficient with the statsmodels output, are they the same? If not why not?
- (C), Fit logistic regression using sklearn to cancer/normal binary labels using protein levels as inputs using 5 fold cross-validation, Calculate the mean and the std of AUC values for the 5 folds, and plot the 5 ROC curves on the same plot.
- (D),  Fit linear discriminant analysis using sklearn to cancer/normal binary labels using protein levels as inputs using 5 fold cross-validation, Calculate the mean and the std of AUC values for the 5 folds, and plot the 5 ROC curves on the same plot. Is it better than logistic regression?
- (E), Fit a logistic regression using scikit-learn to the multi class problem with a different class for each cancer type and one for normals. Evaluate predictions with the confusion matrix, interpret the result matrix.
