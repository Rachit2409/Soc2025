import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.DataFrame({
    "people":["male","male","female"],
    "number":[70,40,90]
})
#sns.barplot(x="number",y="people",data=df,palette=["green","blue","red"])
ax = sns.barplot(x="people", y="number", data=df, palette=["green", "blue"])
ax.set_facecolor("lightyellow")
plt.show()