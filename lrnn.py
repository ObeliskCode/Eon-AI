import tensorflow as tf
import numpy as np


# pip install tensorflow --break-system-packages # you may have to run this command


# Perceiving The Perceptron - Perpetual Enigma
# Link : https://prateekvjoshi.com/2012/12/04/perceiving-the-perceptron/
# A perceptron has a number of external input links, one internal input (called bias), a threshold, and one output link.
# Usually, the input values are boolean (that is, they can only have two possible values: 1 or 0), but they can be any real number as well.
# The output of the perceptron, however, is always boolean. Dec 4, 2012


# Problem : https://stackoverflow.com/questions/52450683/can-a-perceptron-take-real-values-as-input-or-just-0-and-1
# Continuous Tan-Sigmoid Function : https://en.wikibooks.org/wiki/Artificial_Neural_Networks/Activation_Functions
# We use the tanh function in a way that is uncommon to normal perceptron design;
# tanh is our activation function as per a normal perceptron would have;
# except that our activated function output is then multiplied by a variable "gain" which is also tuned;
# the concept of a variable "gain" is how my perceptron is not "binary" but "continous" (Continuous Neural Network) ;


class Latex_RNN_Cell(tf.keras.layers.Layer):
    def __init__(self, input_size, hidden_size):
        super(Latex_RNN_Cell, self).__init__()
        self.W_input = self.add_weight(
            shape=(input_size, hidden_size), initializer="random_normal", trainable=True
        )
        self.W_hidden = self.add_weight(
            shape=(hidden_size, hidden_size),
            initializer="random_normal",
            trainable=True,
        )
        self.bias = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.identity = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )
        self.negative = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )
        self.zero = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

    def call(self, inputs, hidden_state):
        pre_activation = (
            tf.matmul(inputs, self.W_input)
            + tf.matmul(hidden_state, self.W_hidden)
            + self.bias
        )
        latex_negative = tf.tanh(pre_activation) * self.negative
        latex_zero = tf.tanh(pre_activation) * self.zero
        latex_identity = self.identity

        next_hidden_state = latex_negative + latex_zero + latex_identity
        return next_hidden_state


class Latex_RNN(tf.keras.Model):
    def __init__(self, input_size, hidden_size, output_size):
        super(Latex_RNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn_cell = Latex_RNN_Cell(input_size, hidden_size)
        self.output_layer = tf.keras.layers.Dense(output_size)

    def call(self, inputs):
        hidden_state = tf.zeros((tf.shape(inputs)[0], self.hidden_size))

        for t in range(inputs.shape[1]):
            hidden_state = self.rnn_cell(inputs[:, t], hidden_state)

        output = self.output_layer(hidden_state)
        return output


mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


train_images = train_images.reshape((-1, 28, 28)).astype("float32") / 255.0
test_images = test_images.reshape((-1, 28, 28)).astype("float32") / 255.0

input_size = 28
hidden_size = 128
output_size = 10

latex_rnn = Latex_RNN(input_size, hidden_size, output_size)

latex_rnn.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

latex_rnn.fit(
    train_images,
    train_labels,
    epochs=5,
    batch_size=64,
    validation_data=(test_images, test_labels),
)

test_loss, test_acc = latex_rnn.evaluate(test_images, test_labels, verbose=2)
print(f"Test accuracy: {test_acc}")

predictions = latex_rnn.predict(test_images[:10])
predicted_classes = tf.argmax(predictions, axis=1)
print(f"Predicted classes: {predicted_classes.numpy()}")
