from ZAIProject import processor
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

project = ai.project.Project(forceSingleOutput=True, verbose=2)

project.fit.input.add().addAll([
    ai.processor.RegExp(r"(.*)\=", joinGroups=True),
    ai.processor.SplitStr(''),
    ai.processor.ForEach(ai.processor.ValueToIndex())
])

project.fit.output.add().addAll([
    ai.processor.RegExp(r"\=(\d+)", joinGroups=True),
    ai.processor.SplitStr(''),
    ai.processor.ForEach(ai.processor.ValueToIndex()),
    ai.processor.AutoPadding1D(),
    ai.processor.ForEach(ai.processor.IntToBinary(binaryLength=4))
])

project.predict.baseFit()

project.scale(samples, verbose=True)

print('First input', project.dataApplier().applyFitInputOne(samples[0]))
print('First target', project.dataApplier().applyFitTargetOne(samples[0]))

inputShape = project.modelInfo.input[0].shape
inputDim = project.modelInfo.input[0].maxValue + 1
outputDim = project.modelInfo.output[0].shape[1]

tsModel = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=inputShape),
    tf.keras.layers.Embedding(input_dim=inputDim, output_dim=10),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.RepeatVector(2),
    tf.keras.layers.GRU(10, return_sequences=True),
    tf.keras.layers.TimeDistributed(
        tf.keras.layers.Dense(outputDim, activation='sigmoid')
    )
])
tsModel.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['binary_accuracy'])
tsModel.summary()

model = ai.model.TensorModel(project, tsModel)

model.fit(samples, epochs=10000, tillAccuracy=1)

print('samples', samples)

model.evaluate(samples, table=True)

print('Predict', list(model.predict(samples)))
