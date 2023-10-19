import csv

def insert_date_into_csv(date,hour):
    
    filename = "temp\date_in_the_bank.csv"

    with open(filename, 'a', newline='') as file:

        writer = csv.writer(file, delimiter=',')

        line_writed = [date, hour]

        writer.writerow(line_writed)
