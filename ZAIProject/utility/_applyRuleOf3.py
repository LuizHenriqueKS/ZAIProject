def applyRuleOf3(input, minInput: float, maxInput: float, minOutput: float, maxOutput: float):
  if isinstance(input, list) and len(input) == 1:
    input = input[0]
  diffInput = maxInput - minInput
  diffOutput = maxOutput - minOutput
  scale = diffOutput / diffInput
  result = (input - minInput) * scale + minOutput
  return result
