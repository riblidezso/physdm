# Lab exercise 06, SVM


---



1, Load, preprocess and explore the data
* A, Download the NBA Matches 2013-2018 dataset from Kaggle: https://www.kaggle.com/mariodrusso/nba-matches-2013-18
* B, Each game appears twice in the database. Both time the match is marked from the view of the given team. Keep only those matches, where the match is marked from the viewpoint of the home team! (You may need to check and understand the column names.)
* C, Convert the 'Result' column to binary, which marks if the home team won (1) or lost (0). 
* D, Create two datasets, one with all the matches that were played in 2015 and one with all the matches that were played in 2016.
* E, Keep only the following columns for both:  
['Result', '2-Point Field Goals', '2-point Field Goal Attempts', '3-Point Field Goals', '3-Point Field Goal Attempts', 'Free Throws', 'Free Throw Attempts']

2, Data exploration - **you need to complete this task only for the 2015 data**
* A, Show the Pearson correlations between all the remained columns. 
* B-C-D, Make 3 plots, that can reveal any interesting hidden connection in the dataset.  
Make publication-ready figures: axis labels, title, legend, easy-to-read fontsize etc..

3, SVM - **for this step use 2015 for fitting the models and for validation use the 2016 data**
* A, with keeping all the other parameters at their default values, fit SVM with the following three kernels: ['linear', 'poly', 'rbf']
* B, Ehh... poly is pretty slow, isn't it? Apply some data transformation that we learnt in the previous lessons to speed it up!
* C, Select one of the kernels and perform a hyperparameter search for a few selected parameters (fit the SVM with different parameters on the 2015 data and evaluate it on the 2016 data). Plot the results (use accuracy as a metric). 


4, SVM decision boundary
* A, Fit an SVM for the ['Free Throws', '3-Point Field Goals'] variables to predict the match results. For the fitting use the 2015 data. Do not normalize the data.  
The SVM should have the following parameters: C=0.75, kernel='rbf', leave the other parameters at its default values!
* B, Print the prediction accuracy and plot the ROC curce for both the 2015 and the 2016 data.
* C, Plot the decision function for the fitted SVM alongside with the points!  
Hint: we expect a plot similar to this one:
![](http://patbaa.web.elte.hu/svm_help.png)



---

### Hints:

* Decorate your notebook with, questions, explanation etc, make it self contained and understandable!
* Comments you code
* Write functions for repetitive tasks!
* Use the pandas package for data loading and handling
* Use matplotlib for plotting or bokeh and plotly for interactive investigation
* Use the scikit learn package for almost everything
* Use for loops only if it is really necessary!
