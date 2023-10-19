from functions.database import connect_database, disconnect_database
from functions.get_data import get_data
from functions.format_data import format_data
from functions.export_data import export_data
import time

get_data()
time.sleep(0.2)
connection, pg = connect_database("bancodedados","user","pass","localhost","5432")
time.sleep(0.2)
array_list = format_data('temp/data.xml')
time.sleep(0.2)
export_data("temperatura", array_list, connection)
time.sleep(0.2)
disconnect_database()
