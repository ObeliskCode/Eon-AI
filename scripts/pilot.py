# pilot.py

import numpy as np
import tensorflow as tf
from your_perceptron_module import LatexRNN  # Adjust this import based on your module name

def generate_data(samples, time_steps, features):
    x_train = np.random.random((samples, time_steps, features))
    y_train = np.random.randint(0, 2, (samples, 2))
    return x_train, y_train

def main():
    # Hyperparameters
    samples = 1000
    time_steps = 10
    features = 5
    hidden_size = 10
    output_size = 2
    epochs = 100

    # Generate data
    x_train, y_train = generate_data(samples, time_steps, features)

    # Build and compile the model
    model = LatexRNN(input_size=features, hidden_size=hidden_size, output_size=output_size)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=epochs)

if __name__ == "__main__":
    main()
