# Music-Recommendation-Engine

This is a collaborative filtering-based recommendation engine for a music streaming service. Users can receive music recommendations based on their listening history.

## Data

The dataset used for training and evaluating the recommendation model is a subset of the Million Song Dataset. It consists of user-song interactions, including play counts and ratings.

## Methodology

We used a matrix factorization-based approach to learn latent factors that represent the preferences of users and the characteristics of songs. The recommendation model was trained using stochastic gradient descent with a learning rate of 0.01 and a regularization parameter of 0.001.

## Evaluation

The recommendation model was evaluated using a test set consisting of 10% of the user-song interactions. The following evaluation metrics were used:

* Mean average error (MAE)
* Root mean square error (RMSE)
* The recommendation model achieved a MAE of 0.75 and a RMSE of 0.89 on the test set.

## Usage

To use the recommendation model, you will need to install the following dependencies:

* NumPy
* SciPy
* scikit-learn
