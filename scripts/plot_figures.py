import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../data/processed/UCS_CBR_processed.csv')

fig, ax1 = plt.subplots(figsize=(6,5))
sns.barplot(x='Material', y='28_Days_MPa', data=data, ax=ax1, color='skyblue')
ax1.set_ylabel('28-day Strength (MPa)')

ax2 = ax1.twinx()
sns.lineplot(x='Material', y='PAI', data=data, ax=ax2, marker='o', color='red')
ax2.set_ylabel('PAI (%)')

plt.title('Figure 1: Strength and PAI')
plt.savefig('../figures/figure1_strength_pai.png', dpi=300)
plt.show()
