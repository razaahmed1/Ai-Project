import pandas as pd
from src.data_preprocessing import preprocess_data
from src.knn import KNN
from src.decision_tree import DecisionTree
from src.logistic_regression import LogisticRegression
from src.neural_network import NeuralNetwork
from src.random_forest import RandomForest
from src.linear_regression import LinearRegression
from src.evaluation import evaluate_model

def main():
    # Load the dataset
    df = pd.read_csv('data/dataset.csv')  # Update with actual dataset path
    print("Data loaded successfully.")

    # Preprocess the data
    X_train, X_test, y_train, y_test = preprocess_data(df)
    print("Data preprocessing completed.")

    # Initialize models
    models = {
        'KNN': KNN(k=5),
        'Decision Tree': DecisionTree(max_depth=5),
        'Logistic Regression': LogisticRegression(),
        'Neural Network': NeuralNetwork(),
        'Random Forest': RandomForest(n_trees=10),
        'Linear Regression': LinearRegression()
    }

    # Train and evaluate each model
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        metrics = evaluate_model(y_test, y_pred)
        print(f"{model_name} evaluation metrics: {metrics}")

if __name__ == "__main__":
    main()