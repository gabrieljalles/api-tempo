import requests
import xml.etree.ElementTree as ET
import time


def get_data():
    request = requests.get('https://api.tempo.com/index.php?api_lang=br&localidad=13007&affiliate_id=zt7awwx217qa&v=2.0&h=1')
    time.sleep(0.2)
    # Get binary data 
    binary_data = request.content
    time.sleep(0.2)
    # transform to string
    string_data = binary_data.decode('utf-8')
    time.sleep(0.2)
    #transform to a object element
    root = ET.fromstring(string_data)
    time.sleep(0.2)
    # Create a ElementTree
    tree = ET.ElementTree(root)
    time.sleep(0.2)
    #write in  data.xml
    tree.write('temp/data.xml', encoding='utf-8', xml_declaration=True)
    time.sleep(0.2)
    print('Data created successfully')

if __name__ == '__main__':
    get_data()