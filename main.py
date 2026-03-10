import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('best_selling_video_games.csv')
# mask = df['Rank'].apply(lambda x: not str(x).isdigit())
# df.loc[mask,"Publisher(s)"] = df.loc[mask, "Releaseyear"]
# df.loc[mask, "Releaseyear"] = df.loc[mask, "Platform(s)"]
# df.loc[mask, "Platform(s)"] = df.loc[mask, "Series"]
# df.loc[mask, "Series"] = df.loc[mask, "Rank"]
# temp = df.loc[mask, "Title"]
# df.loc[mask, "Title"] = df.loc[mask, "Sales(millions)"]
# df.loc[mask, "Sales(millions)"] = temp
# df['Rank'] = df.index + 1 
# new_mask = df['Series'].str.contains(r"\[.*?\]")
# df.loc[new_mask, "Ref."] = df.loc[new_mask, "Series"].str.extract(r'(\[.*?\])').iloc[:,0]
# df.loc[new_mask, "Series"] = df.loc[new_mask, "Series"].str.replace(r"\[.*?\]", "", regex=True).str.strip()
# print(df.loc[new_mask])
# print(df['Title'].dtype)
# print(df[["Sales(millions)", "Releaseyear"]].describe())
# df.fillna({"Ref.": "[#]"}, inplace=True)
# df.sort_values(by="Sales(millions)", ascending=False, inplace=True)
# print(df["Ref."].value_counts())
# print(df.head(10))
# print(df['Publisher(s)'].value_counts())
# print(df.info())
# print(df[df["Publisher(s)"] == "Nintendo"])
# mask_name = df[df['Series'].isna()].index
# df.loc[mask_name, "Series"] = df.loc[mask_name, "Title"]
# print(df.loc[mask_name])
# df.to_csv('cleaned_data.csv', index=False)
# print(df.info())
df = pd.read_csv('clear.csv')
df["Publisher(s)"].value_counts().head(10).plot(kind="pie", legend=False, autopct=lambda p: f'{int(p*sum(df["Publisher(s)"].value_counts())/100)}')
plt.title("Top 10 Publishers by Number of Games")
plt.tight_layout()
plt.savefig("top_10_publishers_pie.png")

# by year
# size_year = df.groupby(by="Releaseyear").size().sort_index()

# size_year.plot(kind="bar", legend=False)
# plt.title("Number of Games Released Each Year (Bar)")
# plt.xlabel("Release Year")
# plt.ylabel("Number of Games")
# plt.tight_layout()
# plt.savefig("games_by_year_bar.png")

# size_year.plot(kind="line", marker="o", legend=False)
# plt.title("Number of Games Released Each Year (Line)")
# plt.xlabel("Release Year")
# plt.ylabel("Number of Games")
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.show()
# plt.savefig("games_by_year_line.png")


# top10
# print(df.head(10))
# top10.plot(x="Title", y="Sales(millions)", kind="bar", legend=False)
# plt.title("Top 10 Best-Selling Video Games")
# plt.xlabel("Title")
# plt.ylabel("Sales (millions)")
# plt.xticks(rotation=45, ha="right")
# plt.tight_layout()
# plt.savefig("top_10_pandas.png")