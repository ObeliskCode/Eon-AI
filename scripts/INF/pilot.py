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
    
    ## random data
    ##for _ in range(num_samples):
    ##    target = randint(1, 100)
    ##    sequence = [randint(1, 10) for _ in range(seq_length)]
    ##    training_data.append(sequence)
    ##    labels.append(target)

    def append_data(seq,tar):
        training_data.append(seq)
        labels.append(tar)

    append_data([3,3],7)
    append_data([0],1)
    append_data([0,0],2)
    append_data([2,2],6)
    append_data([2,4],8)
    
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

    print(predicted_sequence[0])

    # Todo: fix 0's counting as +>0 during prediction/eval

    # [Hack]
    fstop = int(predicted_sequence[0][0])
    if fstop >= 1:
        current_set = infn_set(fstop)
    else:
        current_set = set([0])
    for operation in predicted_sequence[0][1:]:
        if operation >= 0:
            # hack 0 means nothing 1 means +>0
            if operation >= 1:
                addop = int(operation) - 1
                current_set = infn_append(current_set, addop)
        else:
            current_set = infn_mult_append(current_set, int(-operation))

    if H(current_set) == target:
        print(f"Verified sequence for {target}: {predicted_sequence}")
        training_data = np.append(training_data, [predicted_sequence], axis=0)
        labels = np.append(labels, target)
    else:
        print(f"Failed sequence for {target}. H returned {H(current_set)}. Retrying...")

    return training_data, labels

epochs = 5
for epoch in range(epochs):
    print(f"Epoch {epoch + 1}/{epochs}")
    model.fit(training_data, labels, epochs=1, verbose=1)

    # Attempt solution and expand training data
    for target in range(1, 10):
        training_data, labels = attempt_solution(target, model, training_data, labels)
