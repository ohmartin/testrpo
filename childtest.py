import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')
pollution_data = pd.read_csv("C:\\Users\\213356\\OneDrive - MyFedEx\\PILOT\\Training\\Python\\Training\\UFOPOLLUTANTS.csv")
pollution_data = pollution_data.head(1000)

sns.lmplot(x="NO2.Mean",
           y="CO.Mean",
           col="year",
           data=pollution_data,
           aspect=0.5)
plt.show()
