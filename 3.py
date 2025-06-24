import pandas as pd
data={
    "name":["ram","rachit","op"],
    "age":[10,20,30],
    "salary":[100,90,80]
}
df=pd.DataFrame(data)
print(df,"\n")
df.sort_values(by=["age","salary"],ascending=[True,True],inplace=True)
print(df)