import pandas as pd
import json
import pprint
import matplotlib.pyplot as plt
from pprint import pprint

# URL, von der die Daten abgerufen werden
# URL = "https://www.landesmuseum-stuttgart.de/lmwallobjects.json"


# Fetch JSON data from a given url
filename = "testdateiHA.json"


def read_file():
    # Read file contents
    with open(filename, "r") as file:
        data = json.load(file)
    return data

def extract_info(data):
    # Je Dictionary in JSON-Datei einen Dateneintrag für das (Erstellungs-) Jahr und Name hinzufügen
    i = 0
    for data[i] in data:
        # Jahr als Dictionary-Eintrag hinzufügen (aus Name)
        year = data[i]["objekt_name"]
        year = year[-4:]
        if year.isdigit() == True:
            data[i]["objektjahr"] = year
        else:
            data[i]["objektjahr"] = 0
        # Name als Dictionary-Eintrag hinzufügen (aus Name und ID)
        name = data[i]["objekt_name"]
        name = name[:-6]
        id = data[i]["objekt_id"]
        # nicht nötige Key-Value-Paare entfernen
        data[i]["objektname"] = str(name + ", ID: " + str(id))
        data[i].pop("objekt_id")
        data[i].pop("objekt_name")
        data[i].pop("objekt_inventarnr")
        data[i].pop("objekt_erfasst_am")
        data[i].pop("objekt_beschreibung")
        data[i].pop("institution_id")
        data[i].pop("institution_name")
        data[i].pop("image")
        data[i].pop("total")
        i += 1
    return data


def delete_false(data):
    # Einträge, die mit einer 0 als Entstehungsdatum versehen sind, werden gelöscht
    i = 0
    for data[i] in data:
        if data[i]["objektjahr"] == 0:
            print(data[i])
            data.pop(i)
        i +=1
    return data


def sort_entries(data):
    # Liste der Dictionarys nach Wert des Keys "objekt_jahr" sortieren
    sorted_data = sorted(data, key=lambda x: x['objektjahr'])
    return sorted_data

def create_dicts(data):
    anz_dict1 = 0   #0-249
    anz_dict2 = 0   #250-499
    anz_dict3 = 0   #500-749
    anz_dict4 = 0   #750-999
    anz_dict5 = 0   #1000-1100
    anz_dict6 = 0   #1100-1249
    anz_dict7 = 0   #1250-1400
    anz_dict8 = 0   #1400-1499
    


    overall = {"name": "flare", "children": [{"name" : "Jahre 0-999", "children": },
                                             {"name": "Jahre 1000-1499","children":}
                                             {"name": "Jahre 1500-1999", "children":}
                                             {"name": "Jahre 2000-2022", "children": }]}
    for entry in data:
        if 0 <= entry["objektjahr"] <= 249:

    #Einteilung nach Epochen:
    # 0-999 --- 0-499; 500-999; --- 0-249; 250-499; 500-749; 750-999
    # 1000-1499 --- 1000-1249; 1250-1499; --- 1000-1100; 1100-1249; 1250-1400; 1400-1499
    # 1500-1999 --- 1500-1749; 1759-1999; --- 1500-1600; 1600-1749; 1750-1900; 1900-1999
    # 2000-2022 --- 2000-2010; 2010-2020;



def main():
    json = read_file()
    cleaned_data = extract_info(json)
    delete_false(cleaned_data)
    sort_entries(cleaned_data)


if __name__ == "__main__":
    main()