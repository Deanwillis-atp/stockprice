import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf #yahoo finance 

msft = yf.Ticker("MSFT")
info = msft.info
history = msft.history(period="max")
split_dividends = msft.actions

print(split_dividends)