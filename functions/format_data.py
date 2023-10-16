import xml.etree.ElementTree as ET

def format_data(dist):

    tree = ET.parse(dist)

    root = tree.getroot()

    array_list = []
    date_list = []

    for element in root.findall("location"):

        for days in element.findall("day"):

            date = days.get("value") # dado da data
            tempmin = days.find("tempmin").get("value") #C
            tempmax = days.find("tempmax").get("value") #C

            

            for hours in days.findall("hour"):

                hours_list = []

                hour = hours.get("value") # dado da hora
                temp = hours.find("temp").get("value") # C
                wind = hours.find("wind").get("value") #km/h
                rain = hours.find("rain").get("value") #mm
                windchill = hours.find("windchill").get("value") #C
                clouds = hours.find("clouds").get("value")[:-1]# %  
                uv_index = hours.find("uv_index").get("value")
                
                hours_list.extend([date, tempmin, tempmax, hour, temp, wind, rain, windchill, clouds, uv_index])

                array_list.append(hours_list)

                #check_and_insert_to_date_checker(date, hour)

                #[[data, tempmin, tempmax, hour, temp, wind, rain, windchill, clouds, uv_index],[data, tempmin, tempmax, hour, temp, wind, rain, windchill, clouds, uv_index]]

    print( "Data fomated successfully.") 

    return array_list
                
    
          

            





            
            




    

if __name__ == '__main__':
    format_data()