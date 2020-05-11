import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder
#tạo tập dữ liệu
dtset = [['Sua','Cu_hanh','Banh_quy','Keo','Trung','Sua_chua'],['Thuoc_la','Cu_hanh','Banh_quy','Keo','Trung','Sua_chua'],['Sua','Tao','Keo','Trung'],['Sua','Bo','Bap','Keo','Sua_chua'],['Bap','Cu_hanh','Keo','Kem','Trung']]
#chuyển đổi dữ liệu
te = TransactionEncoder()
te_ary = te.fit(dtset).transform(dtset)
df = pd.DataFrame(te_ary, columns=te.columns_)
df
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
#sinh luật
prequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
print(prequent_itemsets)
#tạo cột độ dài luật
prequent_itemsets['lenght'] = prequent_itemsets['itemsets'].apply(lambda x: len(x))
#loc lai luat
prequent_itemsets[(prequent_itemsets['lenght']==2) & (prequent_itemsets['support']>=0.6)]
prequent_itemsets[prequent_itemsets['itemsets']=={'Cu_hanh','Trung'}]
prequent_itemsets[prequent_itemsets['itemsets']=={'Cu_hanh'}]
prequent_itemsets[prequent_itemsets['itemsets']=={'Keo'}]
rules2 = association_rules(prequent_itemsets,metric="confidence",min_threshold=0.7)
rules = association_rules(prequent_itemsets,metric="lift", min_threshold=1.2)
#cau5

#Tạo phần thử mới

ptmoi = "Keo"

#Tạo danh sách gợi ý theo Confident 0.7
DSgoiyConfident = []
for  i in range(len(rules2.antecedents)):
    for item in list(rules2.antecedents[i]):
        if (ptmoi == item):
            for itemgoiy in list(rules2.consequents[i]):
                DSgoiyConfident.append(itemgoiy)
                DSgoiyConfident = list(set(DSgoiyConfident))

print (DSgoiyConfident)

#Tạo danh sách gợi ý theo lift >= 1.2
DSgoiyLift = []

for  i in range(len(rules.antecedents)):
    for item in list(rules.antecedents[i]):
        if (ptmoi == item):
            for itemgoiy in list(rules.consequents[i]):
                DSgoiyLift.append(itemgoiy)

print (DSgoiyLift)
#BT   

###
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
#tạo tên cột
column_names_attribute = ["bill_id", "item_name","quantity","price"]
data0 = pd.read_csv('details.csv', encoding='utf-8', header=0,names = column_names_attribute)
#xóa dữ liệu trùng lắp
data1 = data0.drop_duplicates()
#sắp xếp tăng dần theo bill_id
data = data1.sort_values(['bill_id'], ascending=[True])
#tạo tập dữ liệu mang
j = 0
k = 0
mang = [[]]
mang[0] = [data.item_name[0]]
for j in range(0,20914):
    if(data.bill_id[j] == data.bill_id[j+1]):
        mang[k].append(data.item_name[j+1])
    else:
        mang2 = []
        mang2.append(data.item_name[j+1])
        mang.append(mang2)
        k = k + 1

print(mang)
#chuyển đổi dữ liệu
te = TransactionEncoder()
te_ary = te.fit(mang).transform(mang)
df = pd.DataFrame(te_ary, columns=te.columns_)
df
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
#sinh luật
prequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
print(prequent_itemsets)
prequent_itemsets['lenght'] = prequent_itemsets['itemsets'].apply(lambda x: len(x))
#loc lai luat
prequent_itemsets[(prequent_itemsets['lenght']==2) & (prequent_itemsets['support']>=0.05)]
rules0 = association_rules(prequent_itemsets,metric="confidence",min_threshold=0.7)
rules = association_rules(prequent_itemsets,metric="lift", min_threshold=1.2)
#danhsachgoiy
#Tạo phần thử mới

ptmoi = "Cơm Rang Hãi Sãn"

#Tạo danh sách gợi ý theo Confident = 0.7
DSgoiyConfident = []
for  i in range(len(rules0.antecedents)):
    for item in list(rules0.antecedents[i]):
        if (ptmoi == item):
            for itemgoiy in list(rules0.consequents[i]):
                DSgoiyConfident.append(itemgoiy)
                DSgoiyConfident = list(set(DSgoiyConfident))

print (DSgoiyConfident)

#Tạo danh sách gợi ý theo lift >= 1.2
ptmoi= "Nước Ngọt.Suối"
DSgoiyLift = []

for  i in range(len(rules.antecedents)):
    for item in list(rules.antecedents[i]):
        if (ptmoi == item):
            for itemgoiy in list(rules.consequents[i]):
                DSgoiyLift.append(itemgoiy)
                DSgoiyLift = list(set(DSgoiyLift))

print (DSgoiyLift)



