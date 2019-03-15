import csv
exFile = open('sample.csv')
exReader = csv.reader(exFile)
#for row in exReader:
    #print('Row #' + str(exReader.line_num) + ' ' + str(row))
exData = list(exReader)

#print exData[0][1]

for i in exData:
    print('fruit' + str(i[0,5][0,1]))

    
