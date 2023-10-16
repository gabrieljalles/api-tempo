import psycopg2
   
def export_data(sheet,array, connection): # ele conseguiu identificar a temperatura sheet 
     
     pg = connection.cursor()
   
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
          
               pg.execute(f"INSERT INTO {sheet} (date, tempmin, tempmax, hour, temp, wind, rain, windchill, clouds_percent, uv_index) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (date, tempmin, tempmax, hour, temp, wind,rain, windchill, clouds, uv_index))
               connection.commit()

          except psycopg2.Error as e:
               if isinstance(e, psycopg2.errors.UniqueViolation):
                    pass
          else:
               print(f"unknown error: {e}")
          

     print(f"Data imported successfully to {sheet} sheet") 