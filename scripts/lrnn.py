import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

import sys
import heapq

sys_maxsize_simulation = 9223372036854775807  # This is typically the value of sys.maxsize on most 64-bit systems

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

EPOCH_NUM = 100

def domain_restrict(x):
    paris_list = []  # List to hold computed values for potential future use.

    w = x / sys_maxsize_simulation  # Normalize the input based on the maximum system size.

    paris_list.clear()  # Clear the list to ensure no stale data remains.

    return w  # Return the normalized value.
    
def domain_restrict_avg(x):
    mval_list = []  # List to hold the heap of values.
    paris_list = []  # List to hold computed averages (currently unused).

    for n in x:  # Iterate through the input values.
        heapq.heappush(mval_list, n)  # Push each value onto the heap.

    accum = []  # List to accumulate normalized values.

    while(len(mval_list) > 0):  # While there are values in the heap.
        y = heapq.heappop(mval_list)  # Pop the smallest value from the heap.
        q = y / sys_maxsize_simulation  # Normalize the value.
        accum.append(q)  # Append it to the accumulation list.

    res = 0  # Initialize a result accumulator.

    for w in accum:  # Iterate through the accumulated normalized values.
        res += w  # Sum the normalized values.

    w = res / len(x)  # Calculate the average.

    mval_list.clear()  # Clear the heap list.
    paris_list.clear()  # Clear the average list.

    return w  # Return the average.

def range_squeeze(x):
    print("Range squeeze function called")  # Log the call to the function.
    squeezed_values = x - np.min(x)  # Squeeze values to start from zero.
    squeezed_values /= np.max(squeezed_values)  # Normalize to [0, 1].
    
    print(f"Squeezed values: {squeezed_values}")  # Log the squeezed values for debugging.
    
    return squeezed_values  # Return the squeezed values.

def range_squeeze_avg(x):
    print("Range squeeze average function called")  # Log the call to the function.
    squeezed_avg = np.mean(range_squeeze(x))  # Compute the average of the squeezed values.
    
    print(f"Squeezed average: {squeezed_avg}")  # Log the squeezed average for debugging.
    
    return squeezed_avg  # Return the squeezed average.

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
        self.negative_sech = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )
        self.zero_sech = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )
        self.negative_cos = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )
        self.zero_cos = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )
        self.negative_sin = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )
        self.zero_sin = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.negative_dist = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )
        self.zero_dist = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.zero_identity = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.negative_identity = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        
        self.ox_identity = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.zero_gain = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.negative_gain = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.vx_bias = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.ox_bias = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.offset = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )

        self.cutoff = self.add_weight(
            shape=(hidden_size,), initializer="random_normal", trainable=True
        )



    def call(self, inputs, hidden_state):
        pre_activation = (
            tf.matmul(inputs, self.W_input)
            + tf.matmul(hidden_state, self.W_hidden)
            + self.bias
        )

        dr_pre_activation = domain_restrict(tf.abs(pre_activation)) + self.vx_bias

        latex_negative = tf.tanh(dr_pre_activation) * self.negative
        latex_zero = tf.tanh(dr_pre_activation) * self.zero
        latex_negative_sech = (1.0 /tf.cosh(dr_pre_activation)) * self.negative_sech
        latex_zero_sech = (1.0 / tf.cosh(dr_pre_activation)) * self.zero_sech
        latex_negative_cos = tf.cos(dr_pre_activation) * self.negative_cos
        latex_zero_cos = tf.cos(dr_pre_activation) * self.zero_cos
        latex_negative_sin = tf.sin(dr_pre_activation) * self.negative_sin
        latex_zero_sin = tf.sin(dr_pre_activation) * self.zero_sin

        latex_tanh = tf.abs(latex_zero - latex_negative)
        latex_sech = tf.abs(latex_zero_sech - latex_negative_sech)
        latex_cos = tf.abs(latex_zero_cos - latex_negative_cos)
        latex_sin = tf.abs(latex_zero_sin - latex_negative_sin)
        latex_identity = tf.abs(pre_activation) + self.identity

        latex_zero_dist = ((latex_tanh * latex_sech) + latex_cos - latex_sin) * self.zero_dist
        latex_negative_dist = ((latex_tanh * latex_sech) - latex_cos - latex_sin) * self.negative_dist  

        post_activation = latex_zero_dist + latex_negative_dist + latex_identity

        vx = tf.abs(post_activation)
        vx -= tf.abs(post_activation)

        advance_soft_max_clip = tf.abs(vx + self.negative_identity) * self.negative_gain
        advance_soft_max_linear = tf.abs(post_activation + self.zero_identity) * self.zero_gain 

        ox_pre_activation = domain_restrict(tf.abs(pre_activation)) + self.ox_bias

        ox_latex_negative = tf.tanh(ox_pre_activation) * self.negative
        ox_latex_zero = tf.tanh(ox_pre_activation) * self.zero

        ox_identity = tf.abs(pre_activation) + self.identity
        ox_post_activation = (ox_latex_zero + ox_latex_negative) * self.ox_identity + ox_identity

		#[todo]: code cutoff to be an "informal number"
        gain = domain_restrict_avg(tf.abs(post_activation + ox_post_activation) + self.offset + self.cutoff)  # Compute gain using domain restriction

        return pre_activation, hidden_state, gain


class LatexRNN(tf.keras.Model):
    def __init__(self, input_size, hidden_size, output_size):
        super(LatexRNN, self).__init__()
        self.rnn_cell = Latex_RNN_Cell(input_size, hidden_size)
        self.dense = tf.keras.layers.Dense(output_size, activation='softmax')

    def call(self, inputs):
        batch_size = tf.shape(inputs)[0]
        time_steps = tf.shape(inputs)[1]
        hidden_state = self.rnn_cell.get_initial_state(batch_size=batch_size)

        outputs = []

        for t in range(time_steps):
            output, hidden_state, gain = self.rnn_cell(inputs[:, t, :], hidden_state)
            outputs.append(output)

        outputs = tf.stack(outputs, axis=1)  # Stack outputs to create a sequence of outputs
        final_output = self.dense(outputs)  # Pass the outputs through the dense layer
        return final_output


# Training script example
if __name__ == "__main__":
    # Create dummy data for demonstration
    x_train = np.random.random((1000, 10, 5))  # 1000 samples, 10 timesteps, 5 features
    y_train = np.random.randint(0, 2, (1000, 2))  # 1000 samples, 2 classes

    # Build and compile the model
    model = LatexRNN(input_size=5, hidden_size=10, output_size=2)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=EPOCH_NUM)

    # Example plotting function
    plt.plot(range(EPOCH_NUM), model.history.history['accuracy'])
    plt.title('Model Accuracy Over Epochs')
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    plt.show()
