from functions.database import connect_database, disconnect_database
from functions.get_data import get_data
from functions.format_data import format_data
from functions.export_data import export_data

get_data()

connection, pg = connect_database("dimensao","postgres","3038","localhost","5432")

array_list = format_data('temp/data.xml')

export_data("temperatura", array_list, connection)

disconnect_database()
