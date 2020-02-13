import csv,json
import os


csvFilePath="datos.csv"
jsonFilePath="datosJson.json"

# Leer el CSV y agregar al diccionario de datos.
data={}
with open(csvFilePath) as csvFile:
    csvReader=csv.DictReader(csvFile)
    for csvRow in csvReader:
        id = csvRow['id']
        data[id] = csvRow

#Crear un archivo JSON
with open(jsonFilePath,'w') as jsonFile:
    jsonFile.write(json.dumps(data,indent=2))        
