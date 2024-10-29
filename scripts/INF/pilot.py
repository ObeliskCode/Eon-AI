import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from infmath import infn_append, infn_mult_append, infn_set
from tensorflow.keras.preprocessing.sequence import pad_sequences

def H(informal_set):
    infn = informal_set
    if len(infn) == ((2 * max(infn)) + 1):
        return max(infn)
    return 0

def generate_initial_data(num_samples=100, seq_length=10):
    training_data = []
    labels = []

    def append_data(target, seq):
        training_data.append(target)
        labels.append(seq)

    append_data(1, [0+1])
    append_data(2, [0+1, 0+1])
    append_data(3, [1+1, 0+1])
    append_data(4, [1+1, 1+1])
    append_data(5, [1+1, 2+1])
    append_data(6, [2+1, 2+1])
    append_data(7, [2+1, 3+1])
    append_data(8, [2+1, 4+1])
    append_data(9, [3+1, 4+1])
    append_data(10, [4+1, 4+1])
    append_data(3, [0+1, 0+1, 0+1])
    append_data(4, [0+1, 0+1, 0+1, 0+1])
    append_data(5, [0+1, 0+1, 0+1, 0+1, 0+1])
    append_data(6, [0+1, 0+1, 0+1, 0+1, 0+1, 0+1])
    append_data(7, [0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1])
    append_data(8, [0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1])
    append_data(9, [0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1])
    append_data(10, [0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1, 0+1])
    
    
    training_data = np.array(training_data)
    labels = pad_sequences(labels, maxlen=seq_length, padding='post')

    return training_data, np.array(labels)

def build_model(input_shape, seq_output_length):
    model = models.Sequential()
    model.add(layers.Input(shape=(input_shape,)))
    model.add(layers.Embedding(input_dim=101, output_dim=32, input_length=1))
    model.add(layers.LSTM(64, return_sequences=True))
    model.add(layers.LSTM(64))
    model.add(layers.Dense(seq_output_length, activation='linear'))
    model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
    return model

def attempt_solution(target, model):
    target_np = np.array([[target]])

    predicted_sequence = model.predict(target_np)
    predicted_sequence = np.round(predicted_sequence).astype(int)

    if predicted_sequence.shape[1] < 10:
        predicted_sequence = np.pad(predicted_sequence, ((0, 0), (0, 10 - predicted_sequence.shape[1])), mode='constant')
    elif predicted_sequence.shape[1] > 10:
        predicted_sequence = predicted_sequence[:, :10]

    #print(predicted_sequence[0])

    fstop = int(predicted_sequence[0][0])
    if fstop >= 1:
        current_set = infn_set(fstop)
    else:
        current_set = set([0])
    for operation in predicted_sequence[0][1:]:
        if operation >= 0:
            if operation >= 1:
                addop = int(operation) - 1
                current_set = infn_append(current_set, addop)
        else:
            current_set = infn_mult_append(current_set, int(-operation))

    if H(current_set) == target:
        print(f"Verified sequence for {target}: {predicted_sequence}")
        return predicted_sequence
    else:
        #print(f"Failed sequence for {target}. H returned {H(current_set)}. Retrying...")
        return None

seq_length = 10
training_data, labels = generate_initial_data(seq_length=seq_length)
model = build_model(input_shape=1, seq_output_length=seq_length)

max_attempt = 11

epochs = 1000
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}")
    model.fit(training_data, labels, epochs=1, verbose=2)

    new_training_data = []
    new_labels = []

    ctr = 1

    for target in range(1, max_attempt):
        new_sequence = attempt_solution(target, model)
        if new_sequence is not None:
            ctr += 1
            new_training_data.append(target)
            new_labels.append(new_sequence[0])

    if ctr >= int((max_attempt-1)/2):
        max_attempt += 10

    if new_training_data and new_labels:
        new_training_data = np.array(new_training_data)
        #print(f"new_training_data.shape{new_training_data.shape}")
        new_labels = np.array(new_labels)
        #print(f"new_labels.shape{new_labels.shape}")

        # Concatenate only if shapes are aligned
        if new_training_data.shape[0] == new_labels.shape[0]:
            training_data = np.concatenate([training_data, new_training_data], axis=0)
            labels = np.concatenate([labels, new_labels], axis=0)

    print(f"Updated training data size: {training_data.shape}, Labels size: {labels.shape}")