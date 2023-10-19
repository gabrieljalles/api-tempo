import csv
import os

def search_date(date, hour):

    filename = "temp\date_in_the_bank.csv"

    with open(filename, 'r', newline='') as file:

        reader = csv.DictReader(file)

        found = 0

        for  line in reader:
            if line['Date'] == date and line['Hour']== hour:
                return True
                
        return False
        





    # if not os.path.isfile(filename):
    #                 with open(filename, 'w', newline='') as file:

    #                     writer = csv.writer(file, delimiter=';')

    #                     writer.writerow('Data', 'Hora')
                
    #                     writer.writerow(date, hour)

    #             else:
    #                     with open(filename, 'w', newline='') as file:
    #                     writer.writerow(date,hour)