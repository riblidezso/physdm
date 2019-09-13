# Lab excercise 01, Unsupervised learning and clustering


---



1, Get data
* A Download the data from the article *"Hurricane-induced selection on the morphology of an island lizard"*.
* https://www.nature.com/articles/s41586-018-0352-3

2, PCA 
* A, Perform PCA on meaningful lizard body measurement data. 
* B, Plot, and interpret the first 3 components using the descriptive labels ('Origin', 'Sex', 'Hurricane').

3, T-SNE
* A, Perform T-SNE on meaningful lizard body measurement data. 
* B, Plot, and interpret the emerging clusters using the descriptive labels ('Origin', 'Sex', 'Hurricane'). 
* C, Repeat T-SNE 3 times using random seeds (0,1,2) and compare them visually. 
* D, Try T-SNE using 3 components too, do new clusters emerge which explain other descriptive labels?

4, K-means
* A, Perform K-means clustering on meaningful lizard body measurement data with 2 clusters. 
* B, Interpret the clusters using the descriptive labels ('Origin', 'Sex', 'Hurricane'). 
* C, Repeat A and B in the 2D T-SNE embedding space.
* D, Perform K-means clustering on the original data with 3 and 4 clusters. Assess visually the meaning of clusters in the 2D space of the 1st and 3rd PCA component. What is the relationship between the clusters and the descriptive labels? 

5, Hierarchical clustering
* A, Perform hierarchical clustering on meaningful lizard body measurement data. Show the results on a dendrogram.
* B, Interpret the dendrogram using the descriptive labels ('Origin', 'Sex', 'Hurricane').



---

### Hints:

* Use the pandas package for data loading and handling
* Use the scikit learn package for PCA,T-SNE, K-Means
* Use the seaborn package for hierarchical clustering
* You need to understand why some columns are full of missing data, and remove these columns. You also need to remove 1 single row in the data which has other missing values too.
* Only perform PCA on body measurement data, not the following columns: ('ID','Origin','Sex','Hurricane')!
* Normalize data before peforming the PCA ( columns should have 0 mean, and variance = 1)




