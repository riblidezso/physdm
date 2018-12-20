# 10. NLP lab exercises

1. apply sklearn t-SNE on the MNIST dataset
- embed the MNIST dataset to a two dimensional space and visualize it
- color the different digits with different colors
- add a legend which shows which color is which digit
- we expect something like this: https://www.mathworks.com/help/examples/stats/win64/VisualizeHighDimensionalDataUsingTSNEExample_01.png
- if you have much worse results, try to tune the t-SNE's parameters

2. read the following .wav files and plot their signal wave vs time
- 'okay': http://www.pacdv.com/sounds/voices/okay-1.wav
- 'yes': http://www.pacdv.com/sounds/voices/yes-2.wav

3. spectrograms
- convert the .wav files to spectrograms
- plot the time vs. frequency diagram where the color shows the absolute value of the Fourier spectrum at that given frequency at that given time

4. write a class that can do text preprocessing
- it should tokenize the given string (you can tokenize on all non alphabetic characters or on all white characters. your solution should be able to do both)
- build up a vocabulary
- convert each new word to a one-hot encoded vector if that word appeared in the vocabulary before

5. write your own t-SNE model
- it is enough to have 2D embedding, there is no need for the general N dimensional case
- repeat the 1. task with your own t-SNE model!
