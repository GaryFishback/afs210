import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid.csv", encoding='latin-1')
# print(df.tail())
numbers = df["Active"].value_counts()
paths = df["Active"].value_counts().keys()
# print(paths)

plt.title("State wise recovery cases of COVID-19 in USA")
plt.ylabel("Actve")
plt.xlabel("Province/State")
plt.xticks(rotation = 75)
print(df["Country_Region"])
# print(df["Active"])
# if(df["Country_Region"].any() == "US"):
#     print('hello')
# print(df["Country_Region"].bool())
# plt.legend()
# if((df["Country_Region"] == "US")).all():
#     print('hello')
plt.bar(df["Province_State"], df["Active"])
plt.show()

