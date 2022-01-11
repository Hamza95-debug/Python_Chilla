import seaborn as sns
import matplotlib.pyplot as plt

#seaborn 
sns.set_theme(style="ticks", color_codes=True)
titanic=sns.load_dataset("titanic")

sns.catplot(x='sex', y='survived', hue='class', kind='bar', data=titanic)
plt.show()