# 🧬 Breast Cancer Predictor

This project is a **Streamlit web application** that predicts whether a **breast tumor** is **benign** or **malignant** using a custom-built **Logistic Regression model**. The app allows medical professionals and researchers to interactively input cell nuclei features and instantly get predictions and probabilities.

---

## 🚀 Features

- 🩻 Predicts **benign** or **malignant** tumors
- 📊 Shows prediction **probabilities**
- 📈 Dynamic **radar chart** visualization for comparison
- 🛠️ Built-in **data cleaning & preprocessing**
- ✅ Custom Logistic Regression model with **98.8% accuracy**
- 🧪 Compared with `scikit-learn` Logistic Regression (98.2% accuracy)
- 🎛️ Adjustable sliders for feature inputs

---

## 🧠 Model Details

- A custom Logistic Regression model built from scratch (NumPy only)
- Trained using features extracted from the `data.csv` dataset
- Model and scaler are saved as `.pkl` files for fast loading
- Probability outputs manually computed using the sigmoid function

---

## 🗂️ Project Structure
📦 Breast_Cancer_Predictor
├── 📁 app
│ └── main.py # Streamlit app entry point
├── 📁 model
│ ├── model.ipynb # Jupyter notebook for training & comparison
│ ├── custom_model.py # Custom logistic regression class
│ ├── model.pkl # Pickled custom-trained model
│ └── scalar.pkl # Pickled scaler (StandardScaler or similar)
├── data.csv # Cleaned and preprocessed dataset
└── README.md # Project documentation

## 🧪 Dataset

- Based on the **Breast Cancer Wisconsin (Diagnostic) Dataset**
- Features include:
  - Radius, Texture, Perimeter, Area, Smoothness, etc.
  - Mean, Standard Error, and Worst value measurements
- Target variable: `diagnosis` (M = Malignant, B = Benign)
  
## 📦 Requirements
- pip install streamlit pandas numpy plotly scikit-learn matplotlib
  
## Run the app
- streamlit run app/main.py

## Accuracy Comparison
- Custom Logistic Regression	98.8% ✅
- Scikit-learn Logistic Regression	98.2%

## 🤝 Contributing
Pull requests are welcome! Feel free to fork and improve the project.

## 📬 Contact
Made with by Aaima Farrukh
www.linkedin/in/aaimafarrukh

## 📄 License
This project is licensed under the MIT License.



