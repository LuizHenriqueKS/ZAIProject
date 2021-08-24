from ..base._loaders import Loaders
from ..processor.loader import *
from ..recursive.loader import *
from ._modelInfoLoader import ModelInfoLoader


class DefaultLoaders(Loaders):

  def __init__(self):
    super().__init__()
    self.addLoader(Slice1DProcessorLoader())
    self.addLoader(ContextProcessorLoader())
    self.addLoader(AutoPadding1DProcessorLoader())
    self.addLoader(Erased1DProcessorLoader())
    self.addLoader(NoneProcessorLoader())
    self.addLoader(SparseProcessorLoader())
    self.addLoader(CustomRecursiveLoader())
    self.addLoader(SparseRecursiveLoader())
    self.addLoader(ModelInfoLoader())
    self.addLoader(SplitStrProcessorLoader())
    self.addLoader(ForEachProcessorLoader())
    self.addLoader(ValueToIndexProcessorLoader())
    self.addLoader(LambdaProcessorLoader())
    self.addLoader(IndexToValueProcessorLoader())
    self.addLoader(SamplesToAudioFileProcessorLoader())
    self.addLoader(AudioFileToSamplesProcessorLoader())
    self.addLoader(FlattenProcessorLoader())
    self.addLoader(ContextLengthProcessorLoader())
    self.addLoader(BinaryToIntProcessorLoader())
    self.addLoader(IntToBinaryProcessorLoader())
    self.addLoader(ReverseNormalizeLoader())
    self.addLoader(ReverseSparseProcessorLoader())
    self.addLoader(RuleOf3ProcessorLoader())
    self.addLoader(ValueProcessorLoader())
    self.addLoader(IndexToCategoricalProcessorLoader())
    self.addLoader(RoundProcessorLoader())
    self.addLoader(Trim1DProcessorLoader())
    self.addLoader(NormalizeProcessorLoader())
    self.addLoader(DownQualityAudioSamplesProcessorLoader())
    self.addLoader(TrimAudioSamplesProcessorLoader())
    self.addLoader(MelspectrogramToAudioSamplesProcessorLoader())
    self.addLoader(AudioSamplesToMelspectrogramProcessorLoader())
    self.addLoader(Erased2DProcessorLoader())
    self.addLoader(AutoPadding2DProcessorLoader())
    self.addLoader(Padding2DProcessorLoader())
