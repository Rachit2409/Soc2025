import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.random.rand(6, 6)
df = pd.DataFrame(data, columns=["A", "B", "C", "D", "E", "F"])
sns.heatmap(df, cmap="coolwarm")
plt.show()
