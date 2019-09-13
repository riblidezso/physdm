# Lab exercise 01, Unsupervised learning and clustering


---



1, Get and prepare data
* A, Download the data from the kaggle challenge *"Titanic: Machine Learning from Disaster"*.  https://www.kaggle.com/c/titanic You need to register to Kaggle to do so.
* B, Load the train.csv table with pandas
* C, Drop columns with the following data : names, ids, and ticket ids
* D, Encode the place or embarkation with 3 new binary columns, drop the original text column
* E, Encode the sex of the original values with 1 binary column, drop the original text column
* F, Encode in a new column whether the Cabin value was missing for a passenger or not, drop the original column
* G, Fill missing values with -1
* H, Check your dataframe, it should only contain numerical values at this point!

2, TSNE embedding
* A, Embed your dataframe without any normalization into 2 dimensions using TSNE (use the scikit-learn implementation)
* B, Plot each person a filled circle marker in the two dimensional space and colour each circle according to the continuous value of the age of the passenger
* C, Plot each person a filled circle marker in the two dimensional space and colour each circle according to the continuous value of the price of their ticket
* D, Describe the results you got, why are these variables important for TSNE?

3. TSNE with normalization.
* A, Normalize each column of your data frame to have 0 mean, and unit variance, and repeat exercise 2.
* B, For each categorical attribute, create a plot where the points are colored according to the class they belong to, also use different marker for each class on the plots.
* C, Try to guess what is the meaning of the distinct clusters? You don't need to understand every single cluster, but pick a few, and investigate them.

4, More dimension reduction. Embed your data to 2 dimensions, and plot the data points (no need for colours etc), using
* A, UMAP (Uniform Manifold Approximation and Projection) ( you will need to install it using `pip install --user umap-learn`
* B, PCA (Principal Component Analysis), use the first two components
* C, NNMF (Non-Negative Matrix Factorization, ofter called NMF)
* D, MDS (Multidimensional scaling)   
All the tools are available in scikit-learn expect for UMAP.



---

### Hints:

* Decorate your notebook with, questions, explanation etc, make it self contained and understandable!
* Comments you code
* Write functions for repetitive tasks!
* Use the pandas package for data loading and handling
* Use matplotlib for plotting or bokeh and plotly for interactive investigation
* Use the scikit learn package for almost everything
* Remember, you need to install UMAP!





