import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from infmath import infn_append, infn_mult_append, infn_set
from random import randint
from tensorflow.keras.preprocessing.sequence import pad_sequences

def H(informal_set):
    infn = informal_set
    if len(infn) == ((2 * max(infn)) + 1):
        return max(infn)
    return 0

def generate_initial_data(num_samples=100, seq_length=10):
    training_data = []
    labels = []
    
    for _ in range(num_samples):
        target = randint(1, 100)
        sequence = [randint(1, 10) for _ in range(seq_length)]
        training_data.append(sequence)
        labels.append(target)

    seq = [3,3]
    tar = 7
    training_data.append(seq)
    labels.append(tar)
    
    training_data = pad_sequences(training_data, maxlen=seq_length, padding='post')
    return np.array(training_data), np.array(labels)

def build_model(input_shape):
    model = models.Sequential()
    model.add(layers.Embedding(input_dim=101, output_dim=16, input_length=input_shape))
    model.add(layers.LSTM(32, return_sequences=True))
    model.add(layers.LSTM(32))
    model.add(layers.Dense(10, activation='relu'))
    model.add(layers.Dense(1, activation='linear'))
    model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
    return model

# Training data
seq_length = 10
training_data, labels = generate_initial_data(seq_length=seq_length)
print(training_data, labels)
model = build_model(input_shape=(seq_length,))

def attempt_solution(target, model, training_data, labels):
    target_sequence = np.full((1, 10), target) 

    predicted_sequence = model.predict(target_sequence)

    if predicted_sequence.shape[0] < 10:
        predicted_sequence = np.pad(predicted_sequence, (0, 10 - predicted_sequence.shape[0]), mode='constant')
    elif predicted_sequence.shape[0] > 10:
        predicted_sequence = predicted_sequence[:10]

    current_set = infn_set(int(predicted_sequence[0][0]))
    for operation in predicted_sequence[0][1:]:
        if operation >= 0:
            current_set = infn_append(current_set, int(operation))
        else:
            current_set = infn_mult_append(current_set, int(-operation))

    if H(current_set) == target:
        print(f"Verified sequence for {target}: {predicted_sequence}")
        training_data = np.append(training_data, [predicted_sequence], axis=0)
        labels = np.append(labels, target)
    else:
        print(f"Failed sequence for {target}. Retrying...")

    return training_data, labels

epochs = 5
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}")
    model.fit(training_data, labels, epochs=1, verbose=1)

    # Attempt solution and expand training data
    for target in range(1, 10):
        training_data, labels = attempt_solution(target, model, training_data, labels)
