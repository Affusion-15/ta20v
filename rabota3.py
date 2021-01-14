#Александр Шанчук ТА-20V
#Задача ( №8.1) / Вариант ( №22 ) / Страница ( №129 )
#Одесса  2011
#В  заданной  строке  заменить  каждый  символ  «No»  строкой  «номер  по порядку».


import csv
with open("list2.csv", encoding="utf8" , newline = '') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=";")
    for row in reader:
        print(row['surname'], '|' ,row['name'], '|' ,row['othcestvo'], '|' ,row['pol'], '|' ,row['nachio'], '|' ,row['rost'], '|' ,row['ves'], '|' ,row['rozdenie'], '|' ,row['mesto'])