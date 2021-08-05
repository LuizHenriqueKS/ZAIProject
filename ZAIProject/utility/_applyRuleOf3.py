def applyRuleOf3(input, minInput: float, maxInput: float, minOutput: float, maxOutput: float):
  diffInput = maxInput - minInput
  diffOutput = maxOutput - minOutput
  scale = diffOutput / diffInput
  result = (input - minInput) * scale + minOutput
  return result
