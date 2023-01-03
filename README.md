# Music-Recommendation-Engine
This is a collaborative filtering-based recommendation engine for a music streaming service. Users can receive music recommendations based on their listening history.

## Data
The dataset used for training and evaluating the recommendation model is a subset of the Million Song Dataset. It consists of user-song interactions, including play counts and ratings.

## Methodology
We used a matrix factorization-based approach to learn latent factors that represent the preferences of users and the characteristics of songs. The recommendation model was trained using stochastic gradient descent with a learning rate of 0.01 and a regularization parameter of 0.001.
