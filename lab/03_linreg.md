# Lab exercise 03, Linear regression

---


1, Download the wine rating data from dkrib.web.elte.hu/datamining/wine.csv.gz
* A, Drop the unnamed id column, the winery, the tasters name and twitter handle, the title, and the region_1/2
* B, Encode the character length of the description as a vaiable, and drop the original text column
* C, Encode whether the designation is missing or not a one-hot encoded variable, and drop the original column
* D, Encode the most common 20 varieties with one hot encoding, remove the original text column.
* E, Encode the most common 20 country values with one hot encoding, remove the original text column.
* F, Encode the most common 20 province values with one hot encoding, remove the original text column.
* G, Impute missing prices with the mean of the prices.


2, Fit a linear regression to estimate the points given to a wine. Use the full dataset for fitting.
* A, Use statsmodels to do a linear regression, print the summary of the results.
* B, Do the same, with scikit-learn, print the coefficients, and the intercept
* C, Compare the results, are they the same?
* D, Interpret the results,
    are more expensive wines better?
    do they write more about better wines?
    do they like American wines?
    is Rose any good?
    
    
3, Fit a linear regression to estimate the price of a wine.
* A, Interpret the results
    Which countries produce the best value (when controlling for qualty)
    Which country produces the most overpriced wines? (when controlling for qualty)
    Could you guess the most overpiced province surprising?
* B, Predit the prices of wines with your model, plot the true and the precited prices on a scatterplot.
* C, Which wines are the most overpriced, and the best value according to your model. 
    Think about it as an investment, so use the relative difference of the predicted the real price.
    Print the original text description for 1-1
* D, Which wines are so bad, that they should pay you to drink it? 
    Print the details, and the original text description for the worst.
* E, Which wines should be most expensive?
    Print the details, and the original text description.
    
    

4, Add a column which represents whether the wine comes from the top 20 countries (0) or it is a different country (1).
* A, Fit a linear model using statsmodels, and one with scikit-learn predicting the points from the other columns.
* B, Compare the coefficients, are they different? If yes which ones?
* C, Try to find out what is the for the difference here?
    

    



---

### Hints:

* Decorate your notebook with, questions, explanation etc, make it self contained and understandable!
* Comment you code
* Write functions for repetitive tasks!
* Use the pandas package for data loading and handling
* Use matplotlib for plotting or bokeh and plotly for interactive investigation
