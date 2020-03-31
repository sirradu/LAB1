import csv
array = []


with open('data.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        array.append(row)

call = -20
sms = 0

for i in range(1,10):
    if '915783624' in array[i][1]:
        call+=float(array[i][3])
        sms+=float(array[i][4])

print("%.2f" % (call*2+sms*2))











