"""
This script reads data from a JSON file and writes specific fields to a CSV file.

The script performs the following steps:
1. Imports the necessary json module.
2. Opens and reads the JSON file 'data_book.json'.
3. Extracts specific fields from each JSON object.
4. Writes the extracted fields to a CSV file 'data.csv' with semicolon-separated values.

Fields extracted from each JSON object:
- empresa: The name of the company.
- direccion: The address of the company.
- pais: The country where the company is located.
- ciudad: The city where the company is located.
- provincia: The province where the company is located.
- llamar: The contact number for the company.
- codigoPostal: The postal code of the company's address.
- distrito: The district where the company is located.

Each line in the CSV file corresponds to one JSON object and contains the extracted fields in the following order:
empresa;direccion;distrito;ciudad;provincia;codigoPostal;pais;llamar
"""

import json

with open('data_book.json', 'r') as file:
    data_books = json.load(file)

with open('data.csv', 'w') as file:
    for data in data_books:
        empresa = data.get("empresa", "")
        direccion = data.get("Direcci\u00f3n", "")
        pais = data.get("Pais ", "")
        ciudad = data.get("Ciudad ", "")
        provincia = data.get("Provincia ", "")
        llamar = data.get("Llamar ", "")
        codigoPostal = data.get("Codigo Postal", "")
        distrito = data.get("Distrito", "")
        line = empresa + ";" + direccion + ";" + distrito + ";" + ciudad + ";" + provincia + ";" + codigoPostal + ";" + pais + ";" + llamar

        file.write(line + '\n')