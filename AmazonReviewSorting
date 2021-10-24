import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

##########################################
#Görev 1
##########################################

#Average Rating’i güncel yorumlara göre hesaplayınız ve var olan average rating ile kıyaslayınız.

df_amazon = pd.read_csv(r"C:\Users\Hp\Desktop\amazon_review\amazon_review.csv")

df_amazon["reviewerID"].nunique()
df_amazon.head()
df_amazon.info()

df = df_amazon[["asin", "overall", "reviewTime"]]

#Ürün reytingi
df["overall"].mean()

# reviewTime object bunun zaman değişkeni olması gerekiyor.
df['reviewTime'] = pd.to_datetime(df['reviewTime'])
df["reviewTime"].max()

current_date = pd.to_datetime("2014-12-12 0:0:0")

df["days"] = (current_date - df['reviewTime']).dt.days
df.head()

df["days"].describe()

# 100 günden az
df.loc[df["days"] <= 100, "overall"]
df.loc[df["days"] <= 100, "overall"].mean()

# 100 günden çok 500 günden az
df.loc[(df["days"] > 100) & (df["days"] <= 500), "overall"]
df.loc[(df["days"] > 100) & (df["days"] <= 500), "overall"].mean()

# 500 günden çok 1000 günden az yorumlar
df.loc[(df["days"] > 500) & (df["days"] <= 1000), "overall"]
df.loc[(df["days"] > 500) & (df["days"] <= 1000), "overall"].mean()

# 1000 günden çok yorumlar
df.loc[df["days"] > 1000, "overall"]
df.loc[df["days"] > 1000, "overall"].mean()

df.loc[df["days"] <= 100, "overall"].mean() * 28/100 + \
df.loc[(df["days"] > 100) & (df["days"] <= 500), "overall"].mean() * 26 / 100 + \
df.loc[(df["days"] > 500) & (df["days"] <= 1000), "overall"].mean() * 24 / 100 + \
df.loc[df["days"] > 1000, "overall"].mean() * 22 / 100

##############################
# Görev 2
##############################

# Ürün için ürün detay sayfasında görüntülenecek 20 review’i belirleyiniz.

df_amazon.head()
df = df_amazon[["reviewerID","reviewerName","reviewText","overall","summary","helpful_yes","total_vote"]]

df_amazon["helpful_no"] = df_amazon["total_vote"]-df_amazon["helpful_yes"]
def wilson_lower_bound(up, down, confidence=0.95):
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)


df_amazon["wilson_lower_bound"] = df_amazon.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)

x=df_amazon.sort_values("wilson_lower_bound", ascending=False).head(20)

for i, col in enumerate(df.columns):
    print(i, col)


