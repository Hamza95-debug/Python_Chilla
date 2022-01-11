import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_theme(style="ticks", color_codes=True)
data_chilla=sns.load_dataset("chilla_data2_for_plots_cleaned.csv")

sns.countplot(x="Gender", hue="Age", data=data_chilla)
plt.show()