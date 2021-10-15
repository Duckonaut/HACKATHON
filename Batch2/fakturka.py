
import csv
with open('fakturka.csv', newline='') as csvfile:
    product_list = []
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        cena = round(int(row[1])*0.01*(1+int(row[2])*0.01)*(1+int(row[3])*0.01),2)
        print(row[0])
        print("Cena netto = ", int(row[1])/100)
        print("podatek VAT = ", row[2], "%")
        print ("narzut = ", row[3], "%")
        print ("CENA SKLEPOWA = ", cena)
        print (30*"-")
