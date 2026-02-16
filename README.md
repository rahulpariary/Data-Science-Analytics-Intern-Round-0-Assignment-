# Trader Performance vs Market Sentiment

**Primetrade.ai Data Science Intern Assignment**

## 📌 Project Objective

This project analyzes how **market sentiment (Fear vs Greed)** influences trader behavior and performance on the Hyperliquid exchange.

The goal is to uncover behavioral trading patterns and derive actionable strategy insights using:

* Data Analysis
* Behavioral Segmentation
* Machine Learning
* Interactive Dashboard

---

## 📂 Dataset

Two datasets were used:

1. **Bitcoin Market Sentiment (Fear & Greed Index)**

   * Daily sentiment classification

2. **Historical Trader Data (Hyperliquid)**

   * Trade executions
   * Position sizes
   * PnL
   * Trade direction

---

## 🧠 Methodology

### Data Preparation

* Cleaned missing & duplicate values
* Converted timestamps to daily level
* Merged trading data with sentiment data

### Feature Engineering

Created behavioral trading metrics:

* Daily PnL
* Win rate
* Trade frequency
* Long/Short ratio
* Position size (proxy for leverage)
* Drawdown proxy (loss magnitude)

### Analysis

Compared trader performance across sentiment regimes:

* Fear vs Greed profitability
* Behavioral shifts
* Risk appetite changes

### Segmentation

Traders grouped into behavioral archetypes:

* High vs Low leverage traders
* Frequent vs Infrequent traders
* Consistent vs Inconsistent traders

### Machine Learning

Predicted trade profitability using:

* Logistic Regression
* Decision Tree
* Random Forest (best performance)

### Dashboard

Built an interactive Streamlit app to:

* Explore trader behavior
* Visualize sentiment impact
* Simulate profitability prediction

---

## 📊 Key Insights

* Trader behavior significantly changes across sentiment regimes
* Risk-taking increases during Greed markets
* Large losses occur more frequently during Fear periods
* Consistent traders reduce activity in volatile sentiment phases

---

## 🧪 Tech Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Streamlit

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd trader-sentiment-analysis
```

### 2️⃣ Create virtual environment (recommended)

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

If requirements.txt not present:

```
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

---

## ▶️ How to Run

### Step 1 — Run Notebook

Open Jupyter Notebook and run all cells:

```
Primetrade.ai.ipynb
```

This will generate:

```
processed_data.csv
rf_model.pkl
```

---

### Step 2 — Launch Dashboard

In project folder run:

```
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 📁 Project Structure

```
project/
│── Primetrade.ai.ipynb
│── app.py
│── processed_data.csv
│── rf_model.pkl
│── README.md
```

---

## 💡 Strategy Recommendations

* Reduce leverage during Fear regimes
* Follow consistent traders during volatile sentiment
* Increase participation only in stable Greed phases

---

## 👤 Author

Adesh Chatterjee
Data Science Intern Candidate
