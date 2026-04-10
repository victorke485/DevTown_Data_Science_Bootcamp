import pandas as pd
data = {
    "names": ["Alex", "Brian", "Victor", "Ann"],
    "marks": [23, 45, 78, 79],
    "age": [19, 18, 20, 22]
}
df = pd.DataFrame(data)

# print(df)
# print(df.columns)
# print(df.shape)
# print(df.info())
# print(df["names"])
# print(df[["names", "marks"]])
# print(df[df["marks"]<50])
# df["Passed"] = df["marks"]>=50
# print(df)
print(df.iloc[0])
print(df.loc[1])

# Sorting
# df_sorted = df.sort_values(by="marks", ascending=False)
# print(df_sorted)