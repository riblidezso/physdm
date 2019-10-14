# Lab assignment 05 subset selection and regularization


1. Large dimensional regression
    * A, Download the prepared data file from
         http://dkrib.web.elte.hu/datamining/small_met.csv
         (Which is a subset of columns of the data from the article: 
         https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3780611/ )
    * B, Fit a linear regression to predict the ages of the patients, using
         the methylation values. 
    * C, Make predictions on your training data and compare the predicted and the true
         ages on a scatterplot.  Calculate the mean absolute error the predictions.
    * D, Make predictions on the data in a 20-fold cross validation setup. 
         Compare the predicted and the true ages on a scatterplot.  
         Calculate the mean absolute error of the predictions.
         Measure the time needed to perform the 20 fits.
    * E, Make predictions on the data in a leave one out cross validation (LOOCV) setup. 
         Compare the predicted and the true ages on a scatterplot.  
         Calculate the mean absolute error of the predictions.
         Measure the time needed to perform the fits.
         
2. Implement iterative stepwise greedy forward subset selection.
    * A, Train single linear regressions using only 1 column, 
         select the input columns which gives the lowest training error. 
         Train your model on all data.
    * B, Continue to add more columns by evaluating the effect of the
         addition of each remaining column on the training error.
         Always select the next column which decreses the error the most.
         Go up to using 100 columns. Note it may take a few minutes.
         Measure the time needed to complete this.
    * C, Calculate the LOOCV error after adding each new input column,
         plot the dependence of the LOOCV error on the number of columns used.
         Is it still getting better after 100 columns? 
           
3. Train regularized linear regressors.  
    (You don't need to normalize the data, it comes somewhat pre-normalized)
    * A, Train a Ridge-regression with default parameters. 
         Evaluate the LOOCV error. Compare the predicted and the true
         ages on a scatterplot.
    * B, Train a lasso-regression with default parameters. 
         Evaluate the LOOCV error. Compare the predicted and the true
         ages on a scatterplot.
         What is going on? Try with smaller penalty.
    * C, Train an Elastic-net regression with default parameters. 
         Evaluate the LOOCV error. Compare the predicted and the true
         ages on a scatterplot.
         What is going on? Try with smaller penalties.
    
4. Investigate regularized linear regressors. 
    * A, Scan the threshold of the penatly parameter for lasso and Ridge
         regression and plot a 20 fold CV error depending on the penalty.
         Select the best penalty value (approximately).
    * B, Scan the threshold of the penalty parameter for lasso and Ridge
         regression between 0.001, and 1 with 30 points.
         Plot the coefficients depending on the penalty.
         Always train your models on the whole dataset.
         (Yes, draw 500 lines on the same plot.)
