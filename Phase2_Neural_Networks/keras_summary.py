from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model= Sequential([Dense(5, input_dim=4),
                   Dense(5),
                   Dense(3)])

model.summary()