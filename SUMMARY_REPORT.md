## Trader Behavior vs Market Sentiment — Summary Report

### Methodology
The objective of this project was to analyze how market sentiment (Fear vs Greed) influences trader behavior and profitability on the Hyperliquid exchange.

First, the trading dataset and the Bitcoin Fear & Greed Index dataset were cleaned and aligned on a daily timestamp. Missing values and duplicates were removed, and timestamps were standardized.
Behavioral trading features were then engineered, including daily PnL, win rate, trade frequency, long/short ratio, and position size. Since explicit leverage was not available, position size (USD exposure) was used as a proxy for leverage. A drawdown proxy was also created using the magnitude of negative PnL.

Next, performance metrics were compared across sentiment regimes to evaluate whether traders behave differently during Fear and Greed markets. Traders were further segmented into behavioral groups such as high vs low leverage users, frequent vs infrequent traders, and consistent vs inconsistent performers.

Finally, predictive models (Logistic Regression, Decision Tree, Random Forest) were trained to estimate the probability of a profitable trade using sentiment and behavior features. A Streamlit dashboard was developed to allow interactive exploration of these findings.

---

### Key Insights

1. **Performance depends on market sentiment**
   Traders generally perform better during Greed periods, where markets are trend-following and directional. Fear periods showed lower win rates and larger loss magnitudes, indicating emotional or reactive trading.

2. **Risk-taking behavior changes significantly**
   During Greed regimes, traders increased position sizes and directional bias, demonstrating higher confidence. In Fear markets, trading activity remained high but with poorer outcomes, suggesting panic-driven decisions.

3. **Trader consistency matters more than activity**
   Frequent traders were not necessarily more profitable. Instead, consistent traders — those with stable win rates — performed better across both sentiment regimes and reduced risk during volatile periods.

4. **Profitability is nonlinear and behavioral**
   The Random Forest model outperformed linear models, indicating that profitability depends on conditional interactions between sentiment and trader behavior rather than simple relationships.

---

### Strategy Recommendations

1. **Risk Adjustment Rule**
   Reduce leverage and position size during Fear regimes, as large losses are more common and market direction is less reliable.

2. **Selective Participation Rule**
   Increase trading activity during stable Greed markets where directional momentum exists, but avoid overtrading during panic-driven Fear periods.

3. **Trader Filtering Rule**
   Follow signals only from consistent traders in volatile sentiment conditions, as they manage risk better and avoid emotional trades.

---

Overall, the analysis demonstrates that market sentiment strongly influences trader psychology, which in turn impacts performance. Incorporating sentiment-aware risk management can significantly improve trading outcomes.