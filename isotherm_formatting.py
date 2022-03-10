

# Data manipulation
import numpy as np
import csv
import pandas as pd

#"22.03.07 JGB + FeHAP controls.csv"
name= input("type name of file (has to be in the same folder as this program) (without '.csv') and hit enter")
with open(name+".csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    rownum=1
    headers=["wavelength"]
    first = True
    n=1
    data=[[],[]]
    for row in csv_reader:
        if rownum==1:
            headers.append(row[0])

        if rownum>=4:
            try:
                if(row[0]): #once it gets to empty row, reset row number (skip 2 rows) and turn off index collection
                    data[n].append(row[1])

                    if first:
                        data[0].append(row[0])
            except:
                rownum = -1
                first = False
                n = n+ 1
                data.append([])
        rownum= rownum + 1
    arr=np.array(data).T
    ar2= pd.DataFrame(arr)
    ar2.columns = headers
    ar3= ar2.set_index('wavelength')


    print(ar3)
    ar3.to_csv(name+" formatted.csv")
