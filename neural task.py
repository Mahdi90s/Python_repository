import numpy as np


class Layer:
    def __init__(self, input_size, output_size, learning_rate=0.8):
        self.weights = np.random.rand(input_size, output_size)
        self.learning_rate = learning_rate

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-0.5 * z))
    
    def sigmoid_derivative(self, z):
        return z * (1 - z)

class InputLayer(Layer):
    def forward(self, inputs):
        # Pass inputs to the hidden layer, no activation required here
        return inputs

class HiddenLayer(Layer):
    def forward(self, inputs):
        self.inputs = inputs
        self.outputs = self.sigmoid(np.dot(inputs, self.weights))
        return self.outputs

    def backpropagate(self, error, next_weights, next_gradient):
        # Calculate error for the hidden layer
        hidden_errors = np.dot(next_gradient, next_weights.T)
        hidden_grad = hidden_errors * self.sigmoid_derivative(self.outputs)
        self.weights += self.learning_rate * np.dot(self.inputs.T, hidden_grad)
        return hidden_grad

class OutputLayer(Layer):
    def forward(self, inputs):
        self.inputs = inputs
        self.outputs = self.sigmoid(np.dot(inputs, self.weights))
        return self.outputs

    def backpropagate(self, targets):
        # Calculate error and gradients for the output layer
        output_errors = targets - self.outputs
        output_grad = output_errors * self.sigmoid_derivative(self.outputs)
        self.weights += self.learning_rate * np.dot(self.inputs.T, output_grad)
        mse = np.mean(output_errors**2)
        return output_grad, mse

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_layer = InputLayer(input_size, hidden_size)
        self.hidden_layer = HiddenLayer(hidden_size, output_size)
        self.output_layer = OutputLayer(hidden_size, output_size)

    def forward(self, inputs):
        inputs = self.input_layer.forward(inputs)
        hidden_outputs = self.hidden_layer.forward(inputs)
        final_outputs = self.output_layer.forward(hidden_outputs)
        return final_outputs

    def train(self, inputs, targets, epochs=1000):
        for epoch in range(epochs):
            # Forward pass
            hidden_outputs = self.hidden_layer.forward(inputs)
            outputs = self.output_layer.forward(hidden_outputs)
            
            # Backward pass
            output_grad, mse = self.output_layer.backpropagate(targets)
            self.hidden_layer.backpropagate(error=outputs - targets, 
                                            next_weights=self.output_layer.weights,
                                            next_gradient=output_grad)
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Mean Squared Error: {mse:.4f}")

# Usage
inputs = np.array([[1, 2]])  # Input data
targets = np.array([[0, 1]])  # Target output

network = NeuralNetwork(input_size=2, hidden_size=2, output_size=2)
network.train(inputs, targets, epochs=500)

# Predict after training
print("Predicted Output:", network.forward(inputs))
