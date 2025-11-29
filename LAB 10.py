import numpy as np

# Sigmoid function and derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (3 features now)
X = np.array([
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
    [1, 0, 0],
    [0, 1, 0]
])

# Output labels (2 outputs)
y = np.array([
    [0, 1],
    [1, 0],
    [1, 0],
    [0, 1],
    [0, 1],
    [1, 0]
])

# Neural network architecture
input_neurons = 3
hidden_neurons = 4
output_neurons = 2

# Initialize weights and biases randomly
W1 = np.random.uniform(-1, 1, (input_neurons, hidden_neurons))
b1 = np.random.uniform(-0.5, 0.5, (1, hidden_neurons))
W2 = np.random.uniform(-1, 1, (hidden_neurons, output_neurons))
b2 = np.random.uniform(-0.5, 0.5, (1, output_neurons))

# Training parameters
learning_rate = 0.6
epochs = 5000

# Training loop
for epoch in range(epochs):
    # Forward Pass
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)
    final_input = np.dot(hidden_output, W2) + b2
    final_output = sigmoid(final_input)
    
    # Calculate error
    error = y - final_output
    
    if epoch % 1000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch} Loss: {loss:.4f}")
    
    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    error_hidden = d_output.dot(W2.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)
    
    # Update weights and biases
    W2 += hidden_output.T.dot(d_output) * learning_rate
    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    W1 += X.T.dot(d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# Final results
print("\aAfter training:")
print(final_output.round(3))
