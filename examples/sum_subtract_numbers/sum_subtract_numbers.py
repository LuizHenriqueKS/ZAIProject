import tensorflow as tf
from tensorflow.python.ops.gen_array_ops import reverse
import ZAIProject as ai

samples = [
    "1+1=2,0",
    "2+1=3,1",
    "3+3=6,0",
    "4+2=6,2",
    "5+3=8,2",
    "6+6=12,0",
    "7+3=10,4",
    "8+4=12,4",
    "9+1=10,8"
]

project = ai.project.Project()

project.fit.input.add().addAll([
    ai.processor.RegExp(r"(\d+)\+(\d+)"),
    ai.processor.ForEach(ai.processor.StrToInt())
])

project.fit.output.add().addAll([
    ai.processor.RegExp(r"\=(\d+)"),
    ai.processor.ForEach(ai.processor.StrToInt())
])

project.fit.output.add().addAll([
    ai.processor.RegExp(r"\,(\d+)"),
    ai.processor.ForEach(ai.processor.StrToInt())
])

project.predict.baseFit()

project.scale(samples, verbose=True)

tsModelInput = tf.keras.layers.Input(shape=[2])
tsModelOutput1 = tf.keras.layers.Dense(1)(tsModelInput)
tsModelOutput2 = tf.keras.layers.Dense(1)(tsModelInput)
tsModel = tf.keras.Model(tsModelInput, [tsModelOutput1, tsModelOutput2])
tsModel.compile(optimizer='adam', loss='mse')

model = ai.model.TensorModel(project, tsModel)

model.fit(samples, epochs=10000, verbose=2)

print('samples', samples)

model.evaluate(samples, verbose=True)
