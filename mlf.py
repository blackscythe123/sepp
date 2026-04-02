import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)

with mlflow.start_run():
    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    # Log
    mlflow.log_param("model_type", "LogisticRegression")
    mlflow.log_metric("accuracy", accuracy)

    # Save model
    mlflow.sklearn.log_model(model, "model")


# import mlflow

# with mlflow.start_run():
#     # Log parameters
#     mlflow.log_param("learning_rate", 0.01)
#     mlflow.log_param("epochs", 10)

#     # Log metrics
#     mlflow.log_metric("accuracy", 0.92)
#     mlflow.log_metric("loss", 0.1)

#     # Log a file (artifact)
#     with open("output.txt", "w") as f:
#         f.write("Hello MLflow")

#     mlflow.log_artifact("output.txt")

#to run python mlf.py
#to see ui python -m mlflow ui
