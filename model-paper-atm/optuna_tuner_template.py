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
