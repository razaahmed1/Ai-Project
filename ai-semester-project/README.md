# AI Semester Project

This project is designed to implement various machine learning algorithms from scratch, including K-Nearest Neighbors, Decision Tree, Logistic Regression, Artificial Neural Network, Random Forest, and Linear Regression. The project also includes data preprocessing, model evaluation, and visualization of results.

## Project Structure

- **data/**: Contains datasets used in the project.
  - **README.md**: Information about the dataset, including its source, features, and preprocessing steps.
  
- **notebooks/**: Contains Jupyter Notebooks for analysis.
  - **main_analysis.ipynb**: Main analysis file that includes data loading, preprocessing, model training, evaluation, and visualization.

- **src/**: Contains the source code for the project.
  - **\_\_init\_\_.py**: Marks the directory as a Python package.
  - **data_preprocessing.py**: Functions for handling missing values, normalizing data, and applying PCA.
  - **knn.py**: Implementation of the K-Nearest Neighbors algorithm.
  - **decision_tree.py**: Implementation of the Decision Tree algorithm.
  - **logistic_regression.py**: Implementation of the Logistic Regression algorithm.
  - **neural_network.py**: Implementation of an Artificial Neural Network.
  - **random_forest.py**: Implementation of the Random Forest algorithm.
  - **linear_regression.py**: Implementation of Linear Regression.
  - **evaluation.py**: Functions for calculating evaluation metrics.
  - **utils.py**: Utility functions for data loading and visualization.

- **tests/**: Contains unit tests for the implementations.
  - **test_knn.py**: Unit tests for K-Nearest Neighbors.
  - **test_decision_tree.py**: Unit tests for Decision Tree.
  - **test_logistic_regression.py**: Unit tests for Logistic Regression.
  - **test_neural_network.py**: Unit tests for Neural Network.
  - **test_random_forest.py**: Unit tests for Random Forest.
  - **test_linear_regression.py**: Unit tests for Linear Regression.
  - **test_evaluation.py**: Unit tests for evaluation metrics.

- **requirements.txt**: Lists required Python packages for the project.

- **main.py**: Entry point for the project, orchestrating data loading, preprocessing, model training, and evaluation.

## Instructions

1. Clone the repository or download the project files.
2. Install the required packages listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```
3. Place your dataset in the `data/` directory.
4. Run the `main.py` file to execute the project:
   ```
   python main.py
   ```
5. Explore the Jupyter Notebook in `notebooks/` for detailed analysis and visualizations.

## Objectives

- Implement various machine learning algorithms from scratch.
- Understand the underlying principles of each algorithm.
- Evaluate model performance using appropriate metrics.
- Visualize results to gain insights into model predictions.

## Acknowledgments

This project is inspired by the need to understand machine learning algorithms deeply and their practical applications in data science.