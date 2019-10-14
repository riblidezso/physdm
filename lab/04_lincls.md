### Linear methods in classification

1. Load hurricane data from the article "Hurricane-induced selection on the morphology of an island lizard". (You may use ELTE wifi to access materials placed behind Nature's paywall.) https://www.nature.com/articles/s41586-018-0352-3
    - A, Drop the lizard with the most missing values
    - B, Drop the ID column, and the 'SumFingers','SumToes','MaxFingerForce' columns,
    which were only measured after the hurricane
    - C, Encode, the Sex, Origin ans Hurricane values into binary columns,
    and drop the original text columns.
    - D, Make sure all your columns are encoded as floating point values, 
    not unsigned integers!
----
2. Use logistic regression from the statsmodels package to predict whether
    the lizard was measured after of before the hurricane, 
    using the whole dataset
    - A, Investigate the Toe and Finger area coefficients, whats going on? 
    Fix this problem by only keeping the mean measurements.
    - B, Which measured quality had the most significant positive effect on survival?
    - C, Which measured quality had the most significant negative effect on survival?
    - D, Try explain the results in your words. Check the abstract of the paper.
    - E, Repeat the fit after scaling each input column to 0 mean and 1 variance. 
    Have the coefficients changed? Have the predictions changed?
----
3. Repeat the fit with scikit-learn on the unnormalized dataset.
    - A, Compare the coefficients with the ones you got from statsmodels. 
    Are they the same? If not try to answer why?
    - B, Try to tweak the parameters of the scikit-learn method to reproduce the
    the coefficients produced by statsmodels.
    - C, Plot the ROC curve for the full dataset, and calculate the AUC.
    - D, Repeat the fit after scaling each input column to 0 mean and 1 variance. 
    Have the coefficients changed? Have the predictions changed?
----    
4. Split the dataset into 5 folds and predict each fold by training on the other 4.
    - A, Make sure to fix the seed of the splitting to 0 to make it reproducible.
    - B, Plot the ROC for the 5 folds separately as curves on the same plot.
    - C, Calculate the AUC values for the 5 folds separately.
