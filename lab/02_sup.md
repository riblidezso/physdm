# Lab exercise 02, Supervised learning, KNN


---



1, Load and preprocess the data
* A, Download the modified version of the *"Sleep in Mammals: Ecological and Constitutional Correlates"* dataset.  https://patbaa.web.elte.hu/Mammals.xls
* B, Check manually the excel sheet, which value marks the missing values?
* C, Load the excel sheet directly via pandas (the 'All Data' sheet). Tell pandas to track the missing values correctly!
* D, Remove columns that have more than 10 missing value!
* E, Replace each remained missing value with the mean of its column!

2, K-nearest neighbors regression
* A, Predict the lifespan of each animal with KNN regression. Use Euclidean distance, uniform weights in your model and set K to 10. Generate the predictions with leave-one-out cross-validation.
* B, Plot the predicted lifespan for each aminal vs the actual lifespan.
* C, Calculate the Pearson's correlation and the MAE (mean absolute error) between the predicted and the actual values.

3, K-nearest neighbors regression with normalization.
* A, Normalize each column of your data frame (except for the predicted variable, the lifespan) to have 0 mean, and unit variance, and repeat exercise 2. 
* B, Why is scaling of the data is important when using KNN? Write down with your own words!
* C, Investigate the predictions. Which animals die too early/live too long according to our model?
* D, Plot the MAE (mean absolute error) of the prediction as a function of K for K $\in$ {1; 5; 10; 15}


4, K-nearest neighbors regression by hand. You may use only numpy and pandas for this task.
* A, Calculate the lifespan KNN (10 neighbor, Euclidean distance, uniform weights) prediction for the Man. Use the normalized dataset. Fit the model on all the data except for the Man.
* B, How does your hand-crafted prediction matches with the prediction generated in **3,A**?


---

### Hints:

* Decorate your notebook with, questions, explanation etc, make it self contained and understandable!
* Comments you code
* Write functions for repetitive tasks!
* Use the pandas package for data loading and handling
* Use matplotlib for plotting or bokeh and plotly for interactive investigation
* Use the scikit learn package for almost everything
* Use for loops only if it is really necessary!
