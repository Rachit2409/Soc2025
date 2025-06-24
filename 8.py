import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "Category": ["A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "Value": [4, 7, 6, 5, 6, 7, 4, 8, 5]
})

sns.stripplot(x="Category", y="Value", data=data, jitter=True, size=8)
plt.show()
