import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.python.keras import activations
from tensorflow.python.keras.layers.core import Flatten
import ZAIProject as ai

samples = []

for i in range(0, 9):
  seq = [i]
  for j in range(1, 6):
    seq.append((i + j) % 10)
  samples.append(seq)

print(samples)

project = ai.project.Project()

project.fit.input.add().addAll([
    ai.processor.Lambda(lambda i: i[:2])
])

project.fit.output.add().addAll([
    ai.processor.Lambda(lambda i: i[2:]),
    ai.processor.Sparse()
])

project.predict.baseFit()

project.scale(samples, verbose=True)

inputDim = project.modelInfo.input[0].maxValue + 1
outputDim = project.modelInfo.output[0].maxValue + 1

tsModel = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=[2]),
    tf.keras.layers.Embedding(inputDim, 10),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.RepeatVector(4),
    tf.keras.layers.GRU(10, return_sequences=True),
    tf.keras.layers.TimeDistributed(
        tf.keras.layers.Dense(outputDim, activation='softmax'))
])

tsModel.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['sparse_categorical_accuracy'])

model = ai.model.TensorModel(project, tsModel)

dataset = ai.dataset.TensorDataset(project, samples)

print('First input', next(dataset.as_numpy_iterator())[0])
print('First output', next(dataset.as_numpy_iterator())[1])

dataset = dataset.batch(5)

model.fitDataset(dataset, epochs=1000, tillAccuracy=1)

model.evaluate(samples, table=True)
