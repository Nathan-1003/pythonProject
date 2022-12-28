import json
from dash import Dash ,dash_table  #pip install dash
import pandas as pd #pip install pandas
import dash_bootstrap_components as dbc

db_connection = 'mysql+pymysql://root:oh_my_ody!@34.142.180.39:13306/data_center'
#db_connection = 'mysql+pymysql://default:oh_my_ody!@34.142.180.39:18123/data_center'  #click hourse
#db_connection_str = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'

#sql_cash_10 = pd.read_sql('SELECT * FROM data_center.cash LIMIT 10', con=db_connection)
#sql_channel_id = pd.read_sql('SELECT channel_id,count(*) AS count FROM data_center.channel GROUP BY channel_id ORDER BY channel_id', con=db_connection)
sql_channel_id = pd.read_sql('SELECT * FROM data_center.channel LIMIT 10 ', con=db_connection)

print(sql_channel_id)
# js = sql_channel_id.to_json(orient = 'columns')
# print(js)
# print(type(sql_channel_id))
app = Dash(__name__)
app.layout = dash_table.DataTable(sql_channel_id .to_dict('records'), [{"name": i, "id": i} for i in sql_channel_id]) #排版
if __name__ == '__main__':
    app.run_server()
