import csv as c
csv_f=open("studentsdetails.csv")
csv_read=c.reader(csv_f)
for line in csv_read:
    print(line)