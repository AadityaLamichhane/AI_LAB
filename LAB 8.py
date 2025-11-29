# Import Library of Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
import numpy as np

# Predictor variables (features) - changed randomly
x = np.array([
    [2, 6], [-1, 3], [0, 2], [-3, 1],
    [3, 5], [-2, -1], [1, 0], [2, 1],
    [4, 2], [3, 6], [-3, 2], [-1, 7]
])

# Target variables (class labels) - changed randomly
y = np.array([1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1])

# Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(x, y)

# Predict Output for new samples
predicted = model.predict([[0, 3], [4, 4]])
print("Predicted class labels:", predicted)

# Install necessary packages
# !pip install scikit-learn numpy
