from tensorflow.python.ops.gen_array_ops import Slice
from ZAIProject import processor
import tensorflow as tf
import ZAIProject as ai

samples = []

for i in range(0, 9):
  seq = [i]
  for j in range(1, 6):
    seq.append((i + j) % 10)
  samples.append(seq)

print(samples)

project = ai.project.Project(forceSingleValuePerOutput=True, verbose=2)

project.fit.input.add().addAll([
    ai.processor.Slice1D(0, 2)
])

project.fit.input.add().addAll([
    ai.processor.Slice1D(2, 4)
])

project.fit.output.add().addAll([
    ai.processor.Slice1D(4, 5),
    ai.processor.Sparse()
])

project.fit.output.add().addAll([
    ai.processor.Slice1D(5, 6),
    ai.processor.Sparse()
])

project.predict.baseFit()

print('First input', project.fit.input.applyOne(samples[0]))
print('First output', project.fit.output.applyOne(samples[0]))

project.scale(samples, verbose=True)

inputDim = project.modelInfo.input[0].maxValue + 1
outputDim = project.modelInfo.output[0].maxValue + 1

input1 = tf.keras.layers.Input(shape=[2])
input2 = tf.keras.layers.Input(shape=[2])

middle = tf.keras.layers.Concatenate()([input1, input2])
middle = tf.keras.layers.Embedding(inputDim, 10)(middle)
middle = tf.keras.layers.Flatten()(middle)
middle = tf.keras.layers.Dense(10, activation='relu')(middle)

output1 = tf.keras.layers.Dense(outputDim, activation='softmax')(middle)
#output1 = tf.keras.layers.RepeatVector(1)(output1)
output2 = tf.keras.layers.Dense(outputDim, activation='softmax')(middle)
#output2 = tf.keras.layers.RepeatVector(1)(output2)

tsModel = tf.keras.Model([input1, input2], [output1, output2])

tsModel.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['sparse_categorical_accuracy'])

model = ai.model.TensorModel(project, tsModel)

dataset = ai.dataset.TensorDataset(
    project,
    samples,
    singleOutputs=[True, True]
)

print('First input', next(dataset.as_numpy_iterator())[0])
print('First output', next(dataset.as_numpy_iterator())[1])

dataset = dataset.batch(5)

#print('First input', next(dataset.as_numpy_iterator()))
#print('First output', next(dataset.as_numpy_iterator()))

model.fitDataset(dataset, verbose=0, epochs=1000, tillAccuracy=1)

model.evaluate(samples, table=True)
