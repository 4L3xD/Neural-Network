# inputs = [1, 2, 3, 2.5]

# weights0 = [0.2, 0.8, -0.5, 1.0]
# weights1 = [0.5, -0.91, 0.26, -0.5]
# weights2 = [-0.26, -0.27, 0.17, 0.87]
 
# bias0 = 2
# bias1 = 3
# bias2 = 0.5
  
# output = [
#            inputs[0] * weights0[0] + inputs[1] * weights0[1] + inputs[2] * weights0[2] + inputs[3] * weights0[3] + bias0,
#            inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
#            inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2
#          ]
# print(output)
 
""" inputs = [1, 2, 3, 2.5]
weights = [
            [0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]
          ]
biases = [2, 3, 0.5]

layer_outputs = [] # output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs) """

import numpy as np

# inputs = [1, 2, 3, 2.5]
# weights = [0.2, 0.8, -0.5, 1.0]
# bias = 2

# output = np.dot(weights, inputs) + bias
# print(output)

inputs = [1, 2, 3, 2.5]
weights = [
            [0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]
          ]
biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases
print(output)