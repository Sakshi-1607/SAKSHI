# csv file create 
import csv

with open("Book12.csv",mode="w",newline='')as csvfile:
    add_csv=csv.writer(csvfile)
    add_csv.writerow(['Name','Address','Trade'])
    add_csv.writerow(['vamshi','beside_vamshi','AIPA'])
    add_csv.writerow(['Diwakar','Behind_vamshi','AIPA'])
print("CSV created successfully.")

# open csv file.
import csv
with open("Book12.csv",newline='') as csvfile:
    csv1=csv.reader(csvfile)
    for row in csv1:
        print(row)