import psycopg2
from functions.search_date import search_date
from functions.insert_date_into_csv import insert_date_into_csv


def export_data(sheet,array, connection):

     print("------------------") 
     print("starting export section ... ")

     pg = connection.cursor()

     found = 0

     for sublist in array:

          try:
               date = sublist[0]
               tempmin = sublist[1]
               tempmax = sublist[2]
               hour = str(sublist[3])
               temp = sublist[4]
               wind = sublist[5]
               rain = sublist[6]
               windchill = sublist[7]
               clouds = str(sublist[8])
               uv_index = sublist[9]

               exists = search_date(date, hour)
               
               if not exists:
                    found +=1
                    pg.execute(f"INSERT INTO {sheet} (date, tempmin, tempmax, hour, temp, wind, rain, windchill, clouds_percent, uv_index) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (date, tempmin, tempmax, hour, temp, wind,rain, windchill, clouds, uv_index))
                    connection.commit()
                    insert_date_into_csv(date,hour)

          except psycopg2.IntegrityError as e:

               if "duplicate key value violates unique constraint" in str(e):
                    print("duplicated value, ignoring insertion!")
                    
               else:
                    print("Another error:", e)

          except psycopg2.Error as e:

               if "current transaction is aborted, commands ignored until end of transaction block" in str(e):
                    pass
                    
    
     print(f"A total of {found} new data exported successfully to {sheet} sheet") 