# 07 Tree based learning exercises 
 
1. Apply the decision tree classifier from sklearn to the titanic data using 80-20% train test split, use a decision tree with 50 leafs. Evalute the training and the testing performance with ROC curves and AUC values.
2. Evaluate decision trees starting with 2 leafs then 2,3,4 etc until 50 leafs, with 5-fold cross validation AUC, using the same dataset. Use KFold with "random_state = 42" . Plot the CV error depending on the number of leafs, and select the best size of the tree.
3. Visualize the above fitted best decision tree and interpret it in some sentences. You can find templates for visualization code on the scikit-learn website!
4. Apply all the tree based classifiers in sklearn (DecisionTrees, RandomForest, Extratrees, GradientBoostedTrees) and Xgboost, with 5 fold CV on the titanic dataset. Which one seems to work the best?
5. Implement decision tree classification using numpy only. Compare it to the sklearn version with the same test as in exercise 1.
