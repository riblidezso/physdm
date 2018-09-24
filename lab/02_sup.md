# 02. Lab excercies, Supervised learning, KNN

----

1. Implement naive K nearest neighbour regression as a function only using python and numpy. The signature of the function should be:


    ```
    def knn_regression(x2pred, x_train, y_train, k=10):
        """Return prediction with knn regression."""
        .
        .
        .
        return y_pred
    ```
    
    
2. Apply the KNN regressor on photometric redshift estimation using the provided photoz_mini.csv file. Use a 80-20% train test split. Calculate the mean absolute error of predictions, and plot the true and the predicted values on a scatterplot.

3. Apply the KNN regressor on photometric redshift estimation using the provided photoz_mini.csv file. Use 5 fold cross validation. Estimate the mean and satndard deviation of the MAE of the predictions.

4. Repeat excercise (3.) with the KNN regression class from sklearn. Compare the predictions and the runtime.

5. Implement weighted KNN regression and apply it on the same data. Use 5 fold cross validation. Estimate the mean and satndard deviation of the MAE of the predictions. Plot the true and the predicted values from one fold on a scatterplot.

---
