# import library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#import data from file
chilla = pd.read_csv("data_viz.csv")
# print(chilla)

sns.set_theme(style="ticks", color_codes=True)

p= sns.countplot(x="Gender", hue="Age",  data=chilla)
plt.show()