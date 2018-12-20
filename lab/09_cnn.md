Use Keras for the CNN!


If you need, you can use K80 GPUs for free via Google Colab

## 1. Download the cifar100 dataset via the keras API
- how many classes do we have in the dataset? how many train and test examples do we have?
- what is the dimension of the images?
- show 5 images from the dataset!
- make one-hot encoding for the labels
## 2. creating CNN architecutre
- create a convolutional neural network
- the network should have the following layers:
  - input (32, 32, 3)
  - conv2D, 16 kernels, kernel size = 3, valid padding, relu actvation
  - conv2D, 16 kernels, kernel size = 3, valid padding, relu actvation
  - maxpooling kernel size = 2*2
  - conv2D, 32 kernels, kernel size = 3, valid padding, relu actvation
  - conv2D, 32 kernels, kernel size = 3, valid padding, relu actvation
  - maxpooling kernel size = 2*2
  - flatten
  - dense, 100 neurons, softmax activation
 - how many parameters do we have for each layer?
## 3. training the CNN
- use Adam optimizer with default parameters
- use categorical crossentropy as loss function
- compile the model
- - print out a summary of the model
- train the CNN on the training data for 5 epochs with batch size of 32
- use the test data as validation data
## 4. Evaluate performance
- plot the training and the validation loss on the same plot!
- plot the training and the validation accuracy on the same plot!
- do we overfit?
## 5. Train an other CNN
- as we can see the previous archutecture is not the best...
- come up with an architecture that can achieve more than 50% accuracy on the test set.
- print out the summary for this model!
- plot the loss and accuracy curves for this model too!
