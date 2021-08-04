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

project = ai.project.Project(
    forceSingleValuePerOutput=True,
    verbose=2,
    recursive=ai.recursive.Raw([2])
)

project.fit.input.add().addAll([
    ai.processor.Lambda(lambda i: i[:2])
])

project.fit.input.add().addAll([
    ai.processor.Context(0),
    ai.processor.AutoPadding1D()
])

project.fit.output.add().addAll([
    ai.processor.Lambda(lambda i: i[2:]),
    ai.processor.AutoPadding1D()
])

project.predict.baseFit()

project.predict.output[0].addAll([
    ai.processor.ForEach([
        ai.processor.Round()
    ])
])

project.scale(samples, verbose=True)

print('First input', project.dataApplier().applyFitInputOne(samples[0]))
print('First target', project.dataApplier().applyFitTargetOne(samples[0]))

input1 = tf.keras.layers.Input(shape=[2])

input2 = tf.keras.layers.Input(shape=[2])

inputDim = 11
outputDim = 2

output = tf.keras.layers.Concatenate()([input1, input2])
output = tf.keras.layers.Embedding(inputDim, 10)(output)
output = tf.keras.layers.Flatten()(output)
output = tf.keras.layers.Dense(20)(output)
output = tf.keras.layers.Dense(outputDim)(output)
tsModel = tf.keras.Model([input1, input2], output)
tsModel.compile(
    'adam',
    'mse'
)

model = ai.model.TensorModel(project, tsModel)

dataset = ai.dataset.TensorDataset(project, samples).prefetch(100).batch(100)

model.fit(dataset, epochs=10000, tillLoss=9E-10)

model.evaluate(samples, table=True)

print('Predict one', model.predictOne([1, 2]))
print('Predict one', model.predictOne([1, 2], [3, 4]))
print('Predict one', model.predictOne([1, 2], [5, 6]))
print('Predict one', model.predictOne([1, 2], [6, 7]))
