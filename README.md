# Crop Recommendation System 🌾

## 🌐 Live Demo
You can try out the live application here: [Agro Production Optimizer](https://agro-production-optimizer.onrender.com)

> **Note:** The application is hosted on a free tier. If the site is inactive, it may take 30-60 seconds to "wake up" upon the first visit.

An intelligent agricultural tool that recommends the most suitable crop to grow based on soil nutrients and environmental conditions. This project uses **Machine Learning (Logistic Regression)** and is deployed via a **Flask** web application.

## 🚀 Features

* **Predictive Modeling**: Uses a pre-trained Scikit-Learn model to predict 22 different types of crops.
* **User-Friendly Interface**: A simple web form built with HTML5, CSS3, and Bootstrap.
* **Real-time Results**: Instantly displays the recommended crop along with a representative image.
* **Optimized Performance**: Loads a serialized model (`.pkl`) for faster response times.

## 🛠️ Tech Stack

* **Language**: Python 3.x
* **Framework**: Flask
* **Machine Learning**: Scikit-Learn, Pandas, NumPy
* **Data Visualization**: Matplotlib, Seaborn
* **Frontend**: HTML, CSS, Bootstrap

## 📂 Project Structure

```text
MiniProject/
├── static/                                         # CSS, background images, and crop icons
├── templates/                                      # index.html (Main UI)
├── Optimizing Agricultural Production.ipynb        # ML model training & Testing
├── app.py                                          # Flask application logic
├── crop_app_model.pkl                              # Serialized ML model
├── data.csv                                        # Agricultural dataset
├── requirements.txt                                # Project dependencies
└── README.md                                       # Project documentation

```

## ⚙️ Local Setup

1. **Clone the repository**:
```bash
git clone https://github.com/YourUsername/Crop-Recommendation-System.git
cd Crop-Recommendation-System

```


2. **Create and activate a virtual environment**:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate

```


3. **Install dependencies**:
```bash
pip install -r requirements.txt

```


4. **Run the application**:
```bash
python app.py

```


Open `http://127.0.0.1:5000` in your browser.

## 📊 Dataset Information

The model is trained on a dataset containing parameters for Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall.

---
## 🧪 How it Works
The system takes 7 key soil and environmental factors as input:
1. **N-P-K**: Nitrogen, Phosphorus, and Potassium levels in the soil.
2. **Temperature & Humidity**: Local climate conditions.
3. **pH**: The acidity or alkalinity of the soil.
4. **Rainfall**: Average annual or seasonal precipitation.

The **Logistic Regression** model then processes these inputs to find the crop with the highest probability of success in those specific conditions.

