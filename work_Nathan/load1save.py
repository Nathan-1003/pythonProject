from unicodedata import name
import pandas as pd
import logging
from sqlalchemy import create_engine
    
conf = {
    "user": "root",
    "password": "oh_my_ody!",
    "server_host": "34.142.180.39",
    "port": "13306",
    "db": "data_center"
}

# mysql
engine = create_engine("mysql+pymysql://root:oh_my_ody!@34.142.180.39:13306/data_center?charset=utf8mb4")

#xls = pd.ExcelFile("./test.xlsx")
xls = pd.ExcelFile("./SQL.xlsx")
df  = pd.read_excel(xls, 'game_club_member')
pdf = pd.DataFrame(df)
print(pdf)
pdf.to_sql('game_club_member', engine, if_exists='append', index=False)
