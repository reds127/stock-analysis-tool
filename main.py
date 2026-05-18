import yfinance as yf
import matplotlib.pyplot as plt

#Asks user for two stock tickers to compare
ticker1 = str(input("Enter ticker 1")).upper()
ticker2 = str(input("Enter ticker 2")).upper()


#Downloads stock data and calculates metrics
def analyse_stock(ticker):
    #downloads 1 month of historical stock data
    data = yf.download(ticker,period ="1mo")
    #calculates daily percentage change in closing price
    data["Daily Return"] = data["Close"].pct_change()
    #calculates average daily return
    avg_return = data["Daily Return"].mean()
    #calculates volatility 
    avg_vol = data["Daily Return"].std()
    return data, avg_return, avg_vol

#runs analysis for both stocks
tk1, tk1_avg, tk1_vol = analyse_stock(ticker1)
tk2, tk2_avg, tk2_vol = analyse_stock(ticker2)

#decides which stock perfromed better based on avg return
if tk1_avg > tk2_avg:
    winner=(f"{ticker1} had higher returns")
else:
    winner=(f"{ticker2} had higher returns")

#creates summary report 
stats_text = f"""
STOCK COMPARISON REPORT

{ticker1}
Average Return: {tk1_avg:.5f}
Volatility: {tk1_vol:.5f}

{ticker2}
Average Return: {tk2_avg:.5f}
Volatility: {tk2_vol:.5f}

Winner: {winner}
"""

#creates figure 
plt.figure(figsize=(12,6))
#creates title
plt.title(f"{ticker1} vs {ticker2} Daily Returns (1 Month)")

#plots daily returns for both stocks
plt.plot(tk1["Daily Return"], label=ticker1)
plt.plot(tk2["Daily Return"], label=ticker2)

#labels axes
plt.xlabel("Days")
plt.ylabel("Daily Returns")
#legend
plt.legend()
#adds space for report
plt.subplots_adjust(bottom=0.4)

#displays report
plt.figtext(
    0.5, 
    0.02,
    stats_text,
    fontsize=9,
    ha="center"
)

plt.show()

