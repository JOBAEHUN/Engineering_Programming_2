import csv
with open("E:/MyPythonProject/Week5_lec/singerA.csv", "r") as inFpA:
    with open("E:/MyPythonProject/Week5_lec/singerB.csv", "r") as inFpB:
        with open("E:/MyPythonProject/Week5_lec/singerSum.csv", "w", newline='') as outFp:
            csvReaderA= csv.reader(inFpA)
            csvReaderB= csv.reader(inFpB)
            csvWriter= csv.writer(outFp)
            header_list= next(csvReaderA)
            header_list= next(csvReaderB)
            csvWriter.writerow(header_list)
            
            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')
