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

You can then use the following code to make recommendations for a given user:

`from recommendation_engine import recommend`

`recommendations = recommend(user_id, model, user_item_matrix, n=10)`

Where user_id is the ID of the user for whom you want to make recommendations, model is the trained recommendation model, user_item_matrix is the user-item interaction matrix, and n is the number of recommendations to generate.

## Running the code

To run the code, you will need to:

* Preprocess the data by running python `preprocess.py`. This will filter the dataset and create the user-item interaction matrix.
* Train the recommendation model by running python `train.py`. This will train the model and save it to a file.
* Make recommendations by running python `recommend.py user_id n`, where user_id is the ID of the user for whom you want to make recommendations, and n is the number of recommendations to generate.

## Project on Kaggle

The project is also available on Kaggle at <https://www.kaggle.com/user/project>.

## Additional resources

Matrix Factorization Techniques for Recommender Systems
Collaborative Filtering for Implicit Feedback Datasets

## Challenges and future improvements

One challenge we faced was dealing with the sparsity of the user-item interaction matrix, as many users only interacted with a small number of songs. In the future, we could try using a different approach such as item-based collaborative filtering or a hybrid approach to address this issue.

## Testing and continuous integration

We use `PyTest` to run unit tests and `Travis` CI to ensure code quality and run tests automatically on every commit. To run the tests locally, you can use `pytest`

## Deployment

To deploy the recommendation engine in a production environment, you will need to:

* Build the recommendation engine by running `python build.py`. This will create a standalone version of the recommendation engine that can be deployed on a server.
* Set up a server with the necessary dependencies installed.
* Deploy the recommendation engine on the server by copying the built files to the server and starting the recommendation service.

## Contributing

If you would like to contribute to the project, please follow these guidelines:

* Open an issue to discuss the proposed change or feature.
* Fork the repository and make your changes on a separate branch.
* Write tests to cover your changes.
* Run the tests and ensure that they pass.
* Submit a pull request.

## License

This project is licensed under the MIT License.
