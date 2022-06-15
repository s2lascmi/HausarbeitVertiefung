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
        data[i]["name"] = str(name + ", ID: " + str(id) + " https://www.landesmuseum-stuttgart.de/sammlung/sammlung-online/dk-details?dk_object_id=" + str(id))
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
            data.pop(i)
        i +=1
    print(data)
    return data


def sort_entries(data):
    # Liste der Dictionarys nach Wert des Keys "objekt_jahr" sortieren
    sorted_data = sorted(data, key=lambda x: x['objektjahr'])
    return sorted_data

def create_third_layer(data):
    anz_dict1 = 0   #0-249
    anz_dict2 = 0   #250-499
    anz_dict3 = 0   #500-749
    anz_dict4 = 0   #750-999
    anz_dict5 = 0   #1000-1100
    anz_dict6 = 0   #1100-1249
    anz_dict7 = 0   #1250-1400
    anz_dict8 = 0   #1400-1499
    anz_dict9 = 0  # 1500-1600
    anz_dict10 = 0  # 1600-1749
    anz_dict11 = 0  # 1750-1900
    anz_dict12 = 0  # 1900-1999

    liste_dict1 = []
    liste_dict2 = []
    liste_dict3 = []
    liste_dict4 = []
    liste_dict5 = []
    liste_dict6 = []
    liste_dict7 = []
    liste_dict8 = []
    liste_dict9 = []
    liste_dict10 = []
    liste_dict11 = []
    liste_dict12= []

    for entry in data:
        if 0 <= int(entry["objektjahr"]) <= 249:
            liste_dict1.append({"name": entry["name"], "value": 1})
            anz_dict1 += 1
        if 250 <= int(entry["objektjahr"]) <= 499:
            liste_dict2.append({"name": entry["name"], "value": 1})
            anz_dict2 += 1
        if 500 <= int(entry["objektjahr"]) <= 749:
            liste_dict3.append({"name": entry["name"], "value": 1})
            anz_dict3 += 1
        if 750 <= int(entry["objektjahr"]) <= 999:
            liste_dict4.append({"name": entry["name"], "value": 1})
            anz_dict4 += 1
        if 1000 <= int(entry["objektjahr"]) <= 1100:
            liste_dict5.append({"name": entry["name"], "value": 1})
            anz_dict5 += 1
        if 1100 <= int(entry["objektjahr"]) <= 1249:
            liste_dict6.append({"name": entry["name"], "value": 1})
            anz_dict6 += 1
        if 1240 <= int(entry["objektjahr"]) <= 1400:
            liste_dict7.append({"name": entry["name"], "value": 1})
            anz_dict7 += 1
        if 1400 <= int(entry["objektjahr"]) <= 1499:
            liste_dict8.append({"name": entry["name"], "value": 1})
            anz_dict8 += 1
        if 1500 <= int(entry["objektjahr"]) <= 1600:
            liste_dict9.append({"name": entry["name"], "value": 1})
            anz_dict9 += 1
        if 1600 <= int(entry["objektjahr"]) <= 1749:
            liste_dict10.append({"name": entry["name"], "value": 1})
            anz_dict10 += 1
        if 1750 <= int(entry["objektjahr"]) <= 1900:
            liste_dict11.append({"name": entry["name"], "value": 1})
            anz_dict11 += 1
        if 1900 <= int(entry["objektjahr"]) <= 1999:
            liste_dict12.append({"name": entry["name"], "value": 1})
            anz_dict12 += 1
        else:
            print("not in list")


    #Einteilung nach Epochen:
    # 0-999 --- 0-499; 500-999; --- 0-249; 250-499; 500-749; 750-999
    # 1000-1499 --- 1000-1249; 1250-1499; --- 1000-1100; 1100-1249; 1250-1400; 1400-1499
    # 1500-1999 --- 1500-1749; 1759-1999; --- 1500-1600; 1600-1749; 1750-1900; 1900-1999
    # 2000-2022 --- 2000-2010; 2010-2020;

    #     overall = {"name": "flare", "children": [{"name" : "Jahre 0-999", "children": },
    #                                              {"name": "Jahre 1000-1499","children":}
    #                                              {"name": "Jahre 1500-1999", "children":}
    #                                              {"name": "Jahre 2000-2022", "children": }]}



def main():
    json = read_file()
    cleaned_data = extract_info(json)
    delete_false(cleaned_data)
    create_third_layer(cleaned_data)


if __name__ == "__main__":
    main()