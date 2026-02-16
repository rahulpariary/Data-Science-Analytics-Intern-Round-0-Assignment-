import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

st.set_page_config(layout="wide")
st.title("📊 Trader Performance vs Market Sentiment Dashboard")

# Load data
df = pd.read_csv("processed_data.csv")

st.sidebar.header("Filters")

sentiment = st.sidebar.multiselect(
    "Select Market Sentiment",
    options=df['classification'].unique(),
    default=df['classification'].unique()
)

filtered = df[df['classification'].isin(sentiment)]

# ------------------------
# Section 1: Overview
# ------------------------
st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Trades", len(filtered))
col2.metric("Unique Traders", filtered['Account'].nunique())
col3.metric("Avg PnL", round(filtered['Closed PnL'].mean(),2))

# ------------------------
# Section 2: Performance
# ------------------------
st.header("Performance vs Sentiment")

perf = filtered.groupby('classification').agg(
    avg_pnl=('Closed PnL','mean'),
    win_rate=('is_profit','mean'),
    avg_size=('abs_size','mean')
)

st.dataframe(perf)

fig, ax = plt.subplots()
sns.barplot(x=perf.index, y=perf['avg_pnl'], ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# ------------------------
# Section 3: Behavior
# ------------------------
st.header("Trader Behavior")

fig2, ax2 = plt.subplots()
sns.boxplot(x='classification', y='abs_size', data=filtered, ax=ax2)
plt.yscale('log')
st.pyplot(fig2)

# ------------------------
# Section 4: Segments
# ------------------------
st.header("Trader Segments")

segment = filtered.groupby('Account').agg(
    pnl=('Closed PnL','mean'),
    win=('is_profit','mean'),
    size=('abs_size','mean'),
    trades=('Account','count')
)

st.dataframe(segment.head(20))

# ------------------------
# Section 5: Prediction Demo
# ------------------------
st.header("Profitability Prediction")

size = st.slider("Position Size", 10, 10000, 1000)
direction = st.selectbox("Direction", ["Long","Short"])
sent = st.selectbox("Sentiment", df['classification'].unique())

is_long = 1 if direction=="Long" else 0

input_df = pd.DataFrame({
    'abs_size':[size],
    'is_long':[is_long],
    'Greed':[1 if sent=="Greed" else 0],
    'Fear':[1 if sent=="Fear" else 0]
})

try:
    model = pickle.load(open("rf_model.pkl","rb"))
    pred = model.predict(input_df)[0]
    st.success("Profitable Trade Likely ✅" if pred==1 else "Loss Likely ⚠️")
except:
    st.warning("Train and save model to enable predictions")
