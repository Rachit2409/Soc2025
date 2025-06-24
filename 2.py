import pandas as pd
data = {
    "name": ["Ram", "Shyam", "Geeta", "Sita", "Aman", "Ravi", "Neha", "Priya", "Anil", "Meena"],
    "age": [25, 30, 28, 26, 32, 35, 24, 29, 31, 27],
    "salary": [50000, 60000, None,58000, 62000, 70000, 49000, 56000, 64000, 51000],
    "performance": [85, 78, 92, 88, 80, 76, 95, 89, 84, 91]
}
Rac=pd.DataFrame(data)
Rac["height"]=[1,2,3,4,5,6,None,8,9,10]
print(Rac)
print()
Rac["height"].interpolate(method="linear",axis=0,inplace=True)
print(Rac)