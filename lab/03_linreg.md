# 03. Lab exercises, Linear regression

----

1. Implement linear regression using SVD. (use np.linalg.svd). Write a class for linear regression, using the following template:


    ```
    class LinReg():
    """Linear regression class."""
    
    def __init__(self):
        """Intialize linear regression."""
        self.coefficients = None
    
    def fit(self,x_train, y_train):
        """Fit linear regression."""
        return self
    
    def predict(self,x_test):
        """Predict with linear regression."""
        return y_test
    ```
    
    
2. Application:
- A, Apply the linear regressor on photometric redshift estimation using the provided photoz_mini.csv file. Use a 80-20% train test split. Calculate the mean squared error (MSE) of predicctions and plot the true and the predicted values on a scatterplot for both the training and the test set. 
- B, Repeat 2/A using the linear regression class of scikit-learn.
- C, Compare the coefficients of the two implementations.
- D, Use 5 fold cross validation using your linear regression class. Estimate the mean and standard deviation of the MSE of the predictions. 
- E, Compare the result of 2/D to the result of KNN regression.




3. Statsmodels
- A Fit linear regression with statsmodels package on the whole dataset. Assess the significance of each color.
- B Iteratvely omit the least significant colors. Compare the $R^2$ of the 5 fits.
- C Validate each 5 combinations of colors using cross validation with 5 folds using your linear regression class. How does the MSE change after omitting the colors? Which is best combination of input colors?
- D, Repeat execise C using a KNN regressor, do you see similar behaviour?


4. Inspection 
- A, Select the best combination of input colors found in 3/C, fit the whole dataset, and inspect the residuals of the fit on a residual plot, is there a clear trend? 
- B, Inspect the residuals of the fit on a residual plot, identify and color outliers ( where residuals are larger than 3 $
\sigma$ ) .
- C, Identify high levarage data points.


5. Interactions, quadratic terms

- A, Select the best combination of inputs found in 3/C and add interaction between the colors and inspect it's siginifcance using the whole dataset.
- B, Validate the added interaction using cross validation on 5 folds using your linear regression class or the scikit-learn linear regression class. How does the MSE change after adding interactions?
- C, Add quadratic form of the colors as predictive variables. Asses the significance of the quadratic terms. Which quadratic term is significant?
- D, Create the final model by adding the siginificant quadratic term, interactions and  the best input colors. Validate this model using cross validation with 5 folds using your linear regression class. Inspect the final MSE, and compare it to the original model with all colors, the one with the best colors, and the one with interactions. Which is the best?

---

