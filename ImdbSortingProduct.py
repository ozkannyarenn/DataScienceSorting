

import pandas as pd
import scipy.stats as st

pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

df = pd.read_csv(r"C:\Users\Hp\Desktop\movies_metadata\movies_metadata.csv",
                 low_memory=False) # DtypeWarning kapamak için

df.head()
df.shape
df["imdb_id"].nunique()
df = df[["title", "vote_average", "vote_count"]]

#######################
# Vote Average'a Göre Sıralama
#######################

df.sort_values("vote_average", ascending=False).head(20)

df["vote_count"].describe([0.10, 0.25, 0.50, 0.70, 0.90, 0.95, 0.99]).T

pd.cut(df["vote_count"], [10,25,50,70,80,90,95,99,100]).value_counts()
df[df["vote_count"] > 400].sort_values("vote_average", ascending=False)

#################
# vote_count
#################

df[df["vote_count"] > 400].sort_values("vote_count", ascending=False).head(20)

from sklearn.preprocessing import MinMaxScaler
