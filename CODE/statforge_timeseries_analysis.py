# ==========================================
# STATFORGE FINAL PROJECT (FULL VERSION)
# ==========================================

import matplotlib
matplotlib.use('Agg')   # <-- ensures graphs save properly

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# ------------------------------
# 1. LOAD DATA
# ------------------------------
df = pd.read_csv("DATA/delhi_climate.csv")

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df = df.sort_values('Date')
df.set_index('Date', inplace=True)

print("\nFirst 5 rows:\n", df.head())
print("\nStatistical Summary:\n", df.describe())

# ------------------------------
# 2. TEMPERATURE TREND
# ------------------------------
plt.figure()
plt.plot(df.index, df['Temperature'])
plt.title("Temperature Trend")
plt.savefig("1_temperature_trend.png")
plt.close()

# ------------------------------
# 3. AQI TREND
# ------------------------------
plt.figure()
plt.plot(df.index, df['AQI'])
plt.title("AQI Trend")
plt.savefig("2_aqi_trend.png")
plt.close()

# ------------------------------
# 4. MULTI VARIABLE GRAPH
# ------------------------------
plt.figure()
plt.plot(df.index, df['Temperature'], label='Temperature')
plt.plot(df.index, df['AQI'], label='AQI')
plt.plot(df.index, df['Humidity'], label='Humidity')
plt.legend()
plt.title("Multi-variable Trend")
plt.savefig("3_multi_variable.png")
plt.close()

# ------------------------------
# 5. MOVING AVERAGE
# ------------------------------
df['Rolling_Mean'] = df['Temperature'].rolling(7).mean()
df['Rolling_STD'] = df['Temperature'].rolling(7).std()

plt.figure()
plt.plot(df.index, df['Temperature'], label='Actual')
plt.plot(df.index, df['Rolling_Mean'], label='Rolling Mean')
plt.fill_between(df.index,
                 df['Rolling_Mean'] - df['Rolling_STD'],
                 df['Rolling_Mean'] + df['Rolling_STD'],
                 alpha=0.2)
plt.legend()
plt.title("Rolling Mean & Volatility")
plt.savefig("4_moving_average.png")
plt.close()

# ------------------------------
# 6. HISTOGRAM
# ------------------------------
plt.figure()
plt.hist(df['Temperature'])
plt.title("Temperature Distribution")
plt.savefig("5_histogram.png")
plt.close()


plt.figure()
plt.boxplot(df['Temperature'])
plt.title("Temperature Box Plot")
plt.savefig("6_boxplot.png")
plt.close()

# ------------------------------
# 8. SCATTER PLOT
# ------------------------------
plt.figure()
plt.scatter(df['Temperature'], df['AQI'])
plt.title("Temperature vs AQI")
plt.xlabel("Temperature")
plt.ylabel("AQI")
plt.savefig("7_scatter.png")
plt.close()

# ------------------------------
# 9. HEATMAP
# ------------------------------
plt.figure()
sns.heatmap(df[['Temperature','AQI','Humidity']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("8_heatmap.png")
plt.close()

# ------------------------------
# 10. TREND LINE (REGRESSION)
# ------------------------------
x = np.arange(len(df))
y = df['Temperature']
trend = np.poly1d(np.polyfit(x, y, 1))

plt.figure()
plt.plot(df.index, y, label='Actual')
plt.plot(df.index, trend(x), label='Trend', linestyle='--')
plt.legend()
plt.title("Trend Line")
plt.savefig("9_trendline.png")
plt.close()

# ------------------------------
# 11. DAILY CHANGE
# ------------------------------
df['Temp_Change'] = df['Temperature'].diff()

plt.figure()
plt.plot(df.index, df['Temp_Change'])
plt.title("Daily Temperature Change")
plt.savefig("10_daily_change.png")
plt.close()

# ------------------------------
# 12. ROLLING CORRELATION
# ------------------------------
rolling_corr = df['Temperature'].rolling(7).corr(df['AQI'])

plt.figure()
plt.plot(df.index, rolling_corr)
plt.title("Rolling Correlation (Temp vs AQI)")
plt.savefig("11_rolling_corr.png")
plt.close()

# ------------------------------
# 13. CUMULATIVE SUM
# ------------------------------
df['Temp_CumSum'] = df['Temperature'].cumsum()

plt.figure()
plt.plot(df.index, df['Temp_CumSum'])
plt.title("Cumulative Temperature")
plt.savefig("12_cumsum.png")
plt.close()

# ------------------------------
# 14. OUTLIER DETECTION
# ------------------------------
mean = df['Temperature'].mean()
std = df['Temperature'].std()

df['Z'] = (df['Temperature'] - mean) / std
outliers = df[df['Z'].abs() > 2]

print("\nOutliers:\n", outliers[['Temperature','Z']])

# ------------------------------
# 15. TIME SERIES DECOMPOSITION
# ------------------------------
decomposition = seasonal_decompose(df['Temperature'], model='additive', period=7)
decomposition.plot()
plt.savefig("13_decomposition.png")
plt.close()

# ------------------------------
# 16. FORECAST
# ------------------------------
forecast = df['Temperature'].tail(7).mean()
print("\nNext Day Forecast:", round(forecast,2))

print("\n✅ ALL GRAPHS SAVED IN FOLDER")