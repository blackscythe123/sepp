# Common Templates for CI/CD, MLflow, and Optuna

This document provides simple, foundational templates for integrating Continuous Integration/Continuous Deployment (CI/CD), MLflow (experiment tracking), and Optuna (hyperparameter tuning). These templates are generic and can be adapted for any system.

---

## 1. CI/CD Pipeline Template (GitHub Actions)

This `.yml` file represents a basic CI/CD pipeline. It sets up a Python environment, installs dependencies, runs tests, and (optionally) triggers a deployment step.

**File:** `.github/workflows/ci_cd_pipeline.yml`

```yaml
name: Simple CI/CD Pipeline

# Trigger the workflow on push or pull request to the main branch
on:
  push:
    branches: [ "main", "dev" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
    # Step 1: Check out the repository code
    - name: Checkout Repository
      uses: actions/checkout@v3

    # Step 2: Set up Python environment
    - name: Set up Python 3.9
      uses: actions/setup-python@v4
      with:
        python-version: "3.9"

    # Step 3: Install dependencies
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # Step 4: Run Tests (e.g., using pytest)
    - name: Run Unit Tests
      run: |
        pytest tests/

  deploy:
    # Only run deploy if build-and-test succeeds and it's the main branch
    needs: build-and-test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest

    steps:
    - name: Deploy Application
      run: |
        echo "Deploying application to production server..."
        # Add deployment script/commands here (e.g., Docker, AWS, Heroku)
```

---

## 2. MLflow Template (Simple Program)

This Python script demonstrates how to start an MLflow run, log parameters (like hyperparameters), log metrics (like accuracy), and save the trained model as an artifact.

**File:** `mlflow_trainer_template.py`

```python
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
```
*To view results, run `mlflow ui` in your terminal and open `http://127.0.0.1:5000`.*

---

## 3. Optuna Template (Simple Program)

This script uses Optuna to automatically search for the best hyperparameters to maximize model accuracy.

**File:** `optuna_tuner_template.py`

```python
import optuna
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

# 1. Load Data (Can be done globally or inside the objective)
data = load_iris()
X, y = data.data, data.target

# 2. Define the Objective Function
def objective(trial):
    # Suggest hyperparameters using the trial object
    n_estimators = trial.suggest_int('n_estimators', 10, 200)
    max_depth = trial.suggest_int('max_depth', 2, 32)
    min_samples_split = trial.suggest_float('min_samples_split', 0.1, 1.0)
    
    # Initialize the model with suggested parameters
    clf = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )

    # Evaluate the model using cross-validation
    # We use accuracy (cv=3 for speed)
    score = cross_val_score(clf, X, y, n_jobs=-1, cv=3)
    accuracy = score.mean()

    # Optuna will try to MAXIMIZE/MINIMIZE this returned value based on direction
    return accuracy

if __name__ == "__main__":
    # 3. Create a Study object and specify direction (maximize accuracy)
    study = optuna.create_study(direction="maximize", study_name="RF_Tuning")
    
    # 4. Optimize the study
    print("Starting Optuna Study...")
    study.optimize(objective, n_trials=20) # Run 20 trials

    # 5. Output Results
    print("\nOptimization Complete!")
    print(f"Number of finished trials: {len(study.trials)}")
    print("Best trial:")
    trial = study.best_trial

    print(f"  Value (Accuracy): {trial.value:.4f}")
    print("  Params: ")
    for key, value in trial.params.items():
        print(f"    {key}: {value}")
```
