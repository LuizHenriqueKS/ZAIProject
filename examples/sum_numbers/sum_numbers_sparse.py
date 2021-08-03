import tensorflow as tf
import ZAIProject as ai
import json

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

project = ai.project.Project()

project.fit.input.add().addAll([
    ai.processor.RegExp(r"(.*)\=", joinGroups=True),
    ai.processor.ForEach([
        ai.processor.SplitStr(''),
        ai.processor.ValueToIndex()
    ])
])

project.fit.output.add().addAll([
    ai.processor.RegExp(r"\=(\d+)", joinGroups=True),
    ai.processor.ForEach([
        ai.processor.JoinStr(''),
        ai.processor.ValueToIndex(),
        ai.processor.AutoPadding1D('right')
    ])
])

project.predict.baseFit()

project.scale(samples, verbose=True)

print('ModelInfo', project.modelInfo)

tsModel = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=[2]),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Dense(1)
])
tsModel.compile(optimizer=tf.optimizers.Adam(0.001), loss='mse')

model = ai.model.TensorModel(project, tsModel)

model.fit(samples, epochs=10000, tillLoss=0)

print('samples', samples)

model.evaluate(samples, verbose=True)
