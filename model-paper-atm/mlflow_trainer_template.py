import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model():
    # 1. Load Data
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    # 2. Define Hyperparameters
    n_estimators = 100
    max_depth = 5

    # 3. Start MLflow tracking run
    # (Optional: Set experiment name if you want to group runs)
    mlflow.set_experiment("My_Simple_Experiment")
    
    with mlflow.start_run(run_name="RandomForest_Run"):
        print(f"Training with n_estimators={n_estimators}, max_depth={max_depth}")

        # Log Parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)

        # Train Model
        clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        clf.fit(X_train, y_train)

        # Predict and calculate metric
        predictions = clf.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        # Log Metric
        mlflow.log_metric("accuracy", accuracy)
        print(f"Model Accuracy: {accuracy:.4f}")

        # Log Model as an artifact
        mlflow.sklearn.log_model(clf, "random_forest_model")
        
        print("Run logged to MLflow successfully.")

if __name__ == "__main__":
    train_model()
