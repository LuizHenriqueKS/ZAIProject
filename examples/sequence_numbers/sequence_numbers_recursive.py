import tensorflow as tf
import ZAIProject as ai

samples = []

for i in range(0, 9):
    seq = [i]
    for j in range(1, 6):
        seq.append(i + j)
    samples.append(seq)

print(samples)

project = ai.project.Project(recursive=ai.recursive.Sparse(2))

project.fit.input.add().addAll([
    ai.processor.Lambda(lambda i: i[:2])
])

project.fit.input.add().addAll([
    ai.processor.Output(0),
    ai.processor.AutoPadding1D()
])

project.fit.output.add().addAll([
    ai.processor.Lambda(lambda i: i[2:])
])

project.predict.baseFit()

input1 = tf.keras.layers.Input(shape=[2])

input2 = tf.keras.layers.Input(shape=[2])

output = tf.keras.layers.Concatenate()([input1, input2])
output = tf.keras.layers.Embedding(10, 10)(output)
output = tf.keras.layers.Flatten()(output)
output = tf.keras.layers.Dense(20, activation='relu')(output)
output = tf.keras.layers.Reshape([2, 10])(output)
output = tf.keras.layers.TimeDistributed(
    tf.keras.layers.Dense(11, activation='softmax')
)(output)


tsModel = tf.keras.Model([input1, input2], output)

model = ai.model.TensorModel(project, tsModel)

model.fit(output, epochs=2000, tillAccuracy=1)

model.evaluate(samples)