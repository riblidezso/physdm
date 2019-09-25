#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:47:50 2019

@author: ribli



# %%
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

3, TSNE with normalization.
* A, Normalize each column of your data frame to have 0 mean, and unit variance, and repeat exercise 2.
* B, For each categorical attribute, create a plot where the points are colored according to the class they belong to, also use different marker for each class on the plots.
* C, Try to guess what is the meaning of the distinct clusters? You don't need to understand every single cluster, but pick a few, and investigate them.
* D, Attempt to use K-means on your embedded 2d points to cluster them into meaningful clusters. Note, you need to somewhat correctly guess the number of clusters a priori.

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



"""

# %%
%pylab inline


# %%
import pandas as pd
import umap
from sklearn.manifold import TSNE, MDS
from sklearn.decomposition import PCA
from sklearn.decomposition import NMF
from sklearn.cluster import KMeans


# %%
df = pd.read_csv('/users/ribli/Downloads/titanic/train.csv')


# %% 1


df.drop(['PassengerId','Name','Ticket'],axis=1,inplace=True)
df= pd.concat([df,pd.get_dummies(df['Sex'])],axis=1)
df.drop(['Sex','male'],axis=1,inplace=True)
df= pd.concat([df,pd.get_dummies(df['Embarked'])],axis=1)
df.drop(['Embarked'],axis=1,inplace=True)
df.fillna(-1,inplace=True)
df['Cabin'] = (df.Cabin==-1).astype('int')







# %% 2

figsize(8,7)
u = TSNE()
xu = u.fit_transform(df)
scatter(xu[:,0], xu[:,1], c=df.Age,cmap='jet')
colorbar()
xlabel('TSNE 1')
ylabel('TSNE 2')
savefig('fig2a.jpg')
title('Age')
show()

scatter(xu[:,0], xu[:,1], c=df.Fare,cmap='jet')
colorbar()
xlabel('TSNE 1')
ylabel('TSNE 2')
title('Fare')
savefig('fig2b.jpg')




# %% 3a

from sklearn.preprocessing import StandardScaler 
s = StandardScaler()
xs = s.fit_transform(df.values)

u = TSNE()
xu = u.fit_transform(xs)
scatter(xu[:,0], xu[:,1], c=df.Age,cmap='jet')
xlabel('TSNE 1')
ylabel('TSNE 2')
colorbar()
savefig('fig3aa.jpg')
title('Age')
show()

scatter(xu[:,0], xu[:,1], c=df.Fare,cmap='jet')
xlabel('TSNE 1')
ylabel('TSNE 2')
colorbar()
title('Fare')
savefig('fig3ab.jpg')


# %% 3b
catcols = [u'Survived', u'Pclass',  u'SibSp', u'Parch', u'Cabin',
           u'female', u'C', u'Q', u'S']
colors = ['k','r','g','m','y','b','orange','brown']
markers = ['o','x','+','v','s','H','.','^']
for cc in catcols:
    vals = np.unique(df[cc])
    for i,v in enumerate(vals):
        idx = df[cc]==v
        scatter(xu[idx,0], xu[idx,1], c=colors[i],marker=markers[i],
                label=str(v))
    legend()
    xlabel('TSNE 1')
    ylabel('TSNE 2')
    title(cc)
    savefig('fig3b_'+cc+'.png')
    show()
        
# %% 3d

        
labels = KMeans(5).fit_predict(xs)
for i,l in enumerate(np.unique(labels)):
    idx = labels==l
    scatter(xu[idx,0], xu[idx,1], c=colors[i%8], marker=markers[i%8],
                label=str(l))
legend()
xlabel('TSNE 1')
ylabel('TSNE 2')
title('K-means')
savefig('fig3d.png')
show()
    
    


# %% 4a

u = umap.UMAP()
xu = u.fit_transform(xs)
scatter(xu[:,0], xu[:,1])
xlabel('UMAP 1')
ylabel('UMAP 2')
savefig('fig4a.jpg')
show()

# %%

u = PCA()
xu = u.fit_transform(xs)
scatter(xu[:,0], xu[:,1])
xlabel('PCA 1')
ylabel('PCA 2')
savefig('fig4b.jpg')
show()

#%%
u = NMF()
xu = u.fit_transform(xs-xs.min())  # no negative values!!
scatter(xu[:,0], xu[:,1])
xlabel('NNMF 1')
ylabel('NNMF 2')
savefig('fig4c.jpg')
show()

# %%

u = MDS()
xu = u.fit_transform(xs)
scatter(xu[:,0], xu[:,1])
xlabel('MDS 1')
ylabel('MDS 2')
savefig('fig4d.jpg')
show()
