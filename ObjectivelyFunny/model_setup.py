# imports
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

def initialize_model(vocab_size, seq_length, embed_dims):
    model = Sequential()

    model.add(Embedding(
        input_dim = vocab_size,
        input_length = seq_length,
        output_dim = embed_dims,
        mask_zero = True))

    # LSTM and Dense layers
    model.add(LSTM(100, return_sequences=True))
    model.add(LSTM(100))
    model.add(Dense(100, activation='relu'))

    # Output layer
    model.add(Dense(vocab_size, activation='softmax'))

    # Compile Function
    model.compile(loss='categorical_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])

    return model
