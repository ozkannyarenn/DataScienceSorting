# AB Testing (Bağımsız İki Örneklem T Testi)

# 1. Hipotezleri Kur
# 2. Varsayım KOntrolü
#    - 1. Normallik Varsayımı
#    - 2. Varyans Homojenliği
# 3. Hipotezin Uygulanması
#    - p-value < 0.05 ise HO red.
#    - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi(parametrik test)
#    - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi(non-parametrik test)
# Not:
# - Normallik sağlanmıyorsa direkt 2 numara. Varyans homojenliği sağlanmıyorsa 1 numraya argüman girilmeli.
# - Normallik incelenmesi öncesi aykırı değer incelenmesi ve düzeltilmesi yapmak faydalı olabilir.

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_control = pd.read_excel(r"C:\Users\Hp\Desktop\ab_testing\ab_testing.xlsx",
                           sheet_name="Control Group")

df_test = pd.read_excel(r"C:\Users\Hp\Desktop\ab_testing\ab_testing.xlsx",
                        sheet_name="Test Group")

#################################
# Görev 1
#################################

# A/B testinin hipotezini tanımlayınız.

# HO: M1=M2
# H1: M1!=M2
df_control["Purchase"].mean()
df_test["Purchase"].mean()

###################################
#Görev 2:
###################################

#Hipotez testini gerçekleştiriniz. Çıkan sonuçların istatistiksel olarak anlamlı olup olmadığını yorumlayınız.

##################
# Normallik Varsayımı
##################

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:...sağlanmamaktadır.

test_stat,pvalue=shapiro(df_test["Purchase"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
# p-value < 0.05 ise HO RED.
# p-value > 0.05 değilse HO REDDEDİLEMEZ.
# p - value = 0.1541 olduğu için HO REDDEDİLEMEZ.

#####################
# Varyans Homojenliği Varsayımı
#####################

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir.

test_stat, pvalue = levene(df_test["Purchase"], df_control["Purchase"])

print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
# p - value = 0.1083 olduğu için HO REDDEDİLEMEZ.

# Bağımsız iki örneklem t testi uygulanmalıdır.

test_stat, pvalue = ttest_ind(df_control["Purchase"],
                              df_test["Purchase"],
                              equal_var=True)
#  equal_var=True, varyansların homojen olduğunu ifade eder.
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
# p - value = 0.3493 olduğu için HO REDDEDİLEMEZ.

###############################################
# Görev 3
###############################################

# Hangi testi kullandınız, sebeplerini belirtiniz.

# Normallik varsayımı için shapiro testi kullandım.
# Varyans homojenliği için levene testi kullandım.
# Varsayımlar sağlandığı için bağımsız iki örneklem t testi(parametrik test) kullandım.

###############################################
# Görev 4 Görev 2’de verdiğiniz cevaba göre, müşteriye tavsiyeniz nedir?
###############################################

# Görev 2’de verdiğiniz cevaba göre, müşteriye tavsiyeniz nedir?

# Bu iki sistem arasında istatiksel olarak büyük farklar yoktur.
# Önerilen yeni sisteme geçmek fayda sağlamaktan ziyade zarara neden olabilir.(Bütçe vs.)

