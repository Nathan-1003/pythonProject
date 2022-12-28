from dash import Dash ,dash_table  #pip install dash
import pandas as pd #pip install pandas
import dash_bootstrap_components as dbc
import seaborn as sns



db_connection = 'mysql+pymysql://root:oh_my_ody!@34.142.180.39:13306/data_center'
#db_connection_str = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'

sql_channel_id = pd.read_sql('SELECT channel_id FROM data_center.channel GROUP BY channel_id ORDER BY channel_id', con=db_connection)
#sql_channel_id = pd.read_sql('SELECT channel_id FROM data_center.channel GROUP BY channel_id ORDER BY channel_id', con=db_connection)

#sql_channel_id = pd.read_sql('SELECT channel_id,count(*) AS count FROM data_center.channel GROUP BY channel_id ORDER BY channel_id', con=db_connection)

#print(sql_cmd)

sql_channel_id.insert(0, '#', sql_channel_id.index)

app = Dash(__name__)

#app.layout = dash_table.DataTable(sql_channel_id .to_dict('records'), [{"name": i, "id": i} for i in sql_channel_id .columns]) #排版

app.layout = dbc.Container(
    [
        dash_table.DataTable(
            id='dash-table',
            data=sql_channel_id.to_dict('records'),
            columns=[
                {'name': column, 'id': column}
                for column in sql_channel_id.columns
            ],
            page_size=10,  # 頁數顯示
            style_header={
                'font-family': 'Times New Roman',
                'font-weight': 'bold',
                'text-align': 'center'
            },
            style_data={
                'font-family': 'Times New Roman',
                'text-align': 'center'
            }
        )
    ],
    style={
        'margin-top': '50px'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True)
