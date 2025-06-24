import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'day': ['Mon', 'Mon', 'Tue', 'Tue', 'Wed', 'Wed', 'Thu', 'Thu'],
    'sales': [200, 220, 180, 190, 250, 240, 210, 230],
    'region': ['East', 'West', 'East', 'West', 'East', 'West', 'East', 'West']
}

df = pd.DataFrame(data)
sns.lineplot(data=df, x='day', y='sales', hue='region', marker='o')
plt.title("Sales by Region")
plt.show()
