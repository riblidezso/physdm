
# Separating hyperplanes and SVM

1. Data loading
download data from https://www.kaggle.com/c/titanic/data (you may need to register first)
we will need only the train.csv file
check for missing values and handle them reasonably!
understand the variables, make a few exploratory data analysis plots! (At least two!)
who buys 1st class tickets? create a plot that shows it!
if possible, convert/encode the columns to get numerical features, if not, remove them!
2. Apply logistic regression classifier on the data
try to predict whether the passenger survived
for the prediction use all the numerical feature!
make a 5 fold cross-validation (shuffle the data first!)
Is it neccessary to use 5 fold cross-validation? Or would be a simple 80/20 train/test split enough?
3. Apply SVM classifier on the data
try to predict whether the passenger survived
for the prediction use all the numerical feature!
try linear kernel (this is the SVC actually), radial kernel and polynomial too.
make a 5 fold cross-validation (shuffle the data first!) for all.
which one is better?
4. Compare the results
plot ROC for the SVM with polynomial kernel and for the logistic regression
compare AUCs
what are the most important features?
5. Split the data randomly to 3 parts: 70% train, 15% validation, 15% test data
check the behaviour of the SVM by modifying at least 4 of its hyperparameters.
create plots (at least 2) that shows the train, val and test accuracy based on a given hyperparameter's different values. It it a good idea to rely on validation data when tuning hyperparameter in this case?
try to incrementally add features (starting from 0 features) to a logistic regression and plot the accuracy vs #features

(1). Data loading
download data from https://www.kaggle.com/c/titanic/data
we will need only the train.csv file
check for missing values and handle them reasonably!
understand the variables, make a few exploratory data analysis plots! (At least two!)
if possible, convert/encode the columns to get numerical features, if not, remove them!
