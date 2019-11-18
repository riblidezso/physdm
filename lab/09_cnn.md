# Lab exercise 09, CNN
---
**Use Keras for the CNN and the neural network implementations, trainings.   
If you need, you may use Kaggle or Google Colab for free GPU usage.   
Kooplex has no GPU, only CPU.**

---



1, Loading data
* A, Download the CIFAR10 dataset via the Keras API.
* B, How many training and test images do we have?
* C, What are the dimensions of the images? (N x M pixel)
* D, Plot 2 images from each class!

2, Model fitting I.
* A, Create a fully connected neural network via Keras
    - network should have the following layers:
     - Flatten with input of (32, 32, 3)
     - Dense, 128 neurons, ReLu activation
     - Dense, 128 neurons, ReLu activation
     - Dense, 10 neurons, softmax activation
* B, Fit the neural network for the training data.
    - use Adam optimizer with its default settings
    - use batch size of 64
    - use accuracy as a metric
    - use categorical_crossentropy loss
    - print the metric after each epoch for both the train and the test set!
    - norm the images to have the pixel values between 0-1 (instead of 0-255)
    - convert the labels to one-hot-encoded variables (see to_categorical)
    - train the neural network for 5 epochs


3, Model fitting II.
* A, Create a convolutional neural network via Keras
    - network should have the following layers:
     - input of (32, 32, 3)
     - conv2D, 16 kernels, kernel size = 3, valid padding, ReLu actvation
     - conv2D, 16 kernels, kernel size = 3, valid padding, ReLu actvation
     - maxpooling kernel size = 2*2
     - conv2D, 32 kernels, kernel size = 3, valid padding, ReLu actvation
     - conv2D, 32 kernels, kernel size = 3, valid padding, ReLu actvation
     - maxpooling kernel size = 2*2
     - flatten
     - Dense, 10 neurons, softmax activation
* B, Fit the neural network with the same options as in exercise 2.

4, Improving CNN
* A, Try to fit an other convolutional neural network tha can achieve 70% accuracy on the test set.
  - You have to come up with the architecture
  - Fit the neural network with the same options as in exercise 2. (so you can fit it only for 5 epochs!)



---
