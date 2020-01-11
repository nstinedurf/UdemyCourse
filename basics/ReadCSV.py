import csv

with open('trialCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    listOfLists = csv_reader
    #printing listOfLists for fun and proof
    for row in listOfLists:
        for column in row:
            print(column)