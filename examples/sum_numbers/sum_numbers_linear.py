import tensorflow as tf
import ZAIProject as ai

samples = [
    "1+1=2",
    "2+1=3",
    "3+3=6",
    "4+2=6",
    "5+3=8",
    "6+6=12",
    "7+3=10",
    "8+4=12",
    "9+1=10"
]

project = ai.project.Project(forceSingleValuePerOutput=True, verbose=2)

project.fit.input.add().addAll([
    ai.processor.RegExp(r"(\d+)\+(\d+)"),
    ai.processor.ForEach(ai.processor.StrToInt())
])

project.fit.output.add().addAll([
    ai.processor.RegExp(r"\=(\d+)"),
    ai.processor.ForEach(ai.processor.StrToInt())
])

project.predict.baseFit()

project.scale(samples, verbose=True)

tsModel = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=[2]),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
tsModel.compile(optimizer=tf.optimizers.Adam(0.001), loss='mse')

model = ai.model.TensorModel(project, tsModel)

model.fit(samples, epochs=10000, tillLoss=0)

print('samples', samples)

model.evaluate(samples, table=True)

tests = [
    '2+2=4',
    '8+8=16',
    '10+10=20'
]

model.evaluate(tests, table=True)

print('Predict', list(model.predict(samples)))
