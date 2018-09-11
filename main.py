import csv
import math
#by saying firstline = True you let it know that that it doesnt have to count the information
firstline = True

electiondict = {}

with open ('election_data.csv','r') as csvelection:
    csvreader = csv.reader(csvelection)
    for row in csvreader:
        tempname = row[2]
        #tempname is going to read the name it is were we are going to store the information
        if firstline
            firstline = False
        elif tempname in electiondict:
            electiondict[tempname] +=1
        else:
            electiondict[tempname] = 1

    subtotal = 0
    for name in electiondict:
        subtotal += electiondict[name]

    print ('Election Results')
    print ('----------------')
    print (f'Total Value {subtotal}')
    print ('----------------')

    for name in electiondict:
        print (f'{name}: {math.floor (100*1000* electiondict[name]/subtotal)/1000}%({electiondict[name]})')
        print ('----------------')

    
