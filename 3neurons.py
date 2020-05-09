inputs = [1, 2, 3]
weights0 = [0.2, -0.8, 1.0]
weights1 = [0.3, -0.6, -0.4]
weights2 = [0.1, -0.2, 1.91]

biases = [2, 0.5]

bias0 = 2
bias1 = 0.5

output = [ inputs[0] * weights0[0] + inputs[1] * weights0[1] + inputs[2] * weights0[2] + bias1,
           inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + bias0,
         ]
print(output)
