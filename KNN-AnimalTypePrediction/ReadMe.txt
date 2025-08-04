# Animal Type Prediction using KNN Algorithm

This project uses the K-Nearest Neighbors (KNN) algorithm to predict the type of animal based on its physical and behavioral features using the `zoo.csv` dataset.


📁 Project Structure
├── knn.ipynb  # Main project notebook
├── zoo.csv                        # Dataset used
├── README.txt                     # Project documentation
├──Requirements.txt            # Technologies Used


## 🧠 Algorithm Used
- **K-Nearest Neighbors (KNN)**:
- Supervised machine learning algorithm.
- Classifies an animal based on the most common class among its k-nearest neighbors.
- `sklearn.neighbors.KNeighborsClassifier` is used.


## 📊 Objective
To train a model on the dataset so that it can:
- Accurately classify a new animal based on its features.
- Help understand how KNN works on categorical/boolean feature data.


🚀 How to Run
1. Clone the repo:
git clone https://github.com/your-username/KNN-AnimalTypePrediction.git

2. Install dependencies:
pip install -r requirements.txt

3. Open the notebook and run:
knn.ipynb

