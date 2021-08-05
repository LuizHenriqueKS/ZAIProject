from ZAIProject import processor
from os import listdir, path
import pathlib
import ZAIProject as ai
import tensorflow as tf
import librosa
import soundfile
import warnings
warnings.filterwarnings('ignore')

directory = pathlib.Path(__file__).parent.resolve()

samples = []

for f in listdir(directory):
  if not f.startswith('-') and f.endswith('.mp3'):
    samples.append(f)

print('Samples', samples)

project = ai.project.Project()

project.fit.input.add().addAll([
    ai.processor.Slice1D(0, -4),
    ai.processor.SplitStr(''),
    ai.processor.ForEach([
        ai.processor.ValueToIndex()
    ])
])

project.fit.output.add().addAll([
    ai.processor.Lambda(lambda f: path.join(directory, f)),
    ai.processor.AudioFileToSamples(mono=True, sampleRate=1000),
    ai.processor.AutoPadding1D(name='PaddingSample'),
    ai.processor.ForEach([
        ai.processor.ValueToIndex()
    ])
])

project.scale(samples, verbose=True)

ai.project.io.writeFile(project, path.join(directory, 'project.json'))

dataset = ai.dataset.TensorDataset(project, samples)
tf.data.experimental.save(dataset, path.join(directory, 'dataset_tmp'))

#print('First input', project.dataApplier().applyFitInputOne(samples[0]))
#print('First target', project.dataApplier().applyFitTargetOne(samples[0]))
