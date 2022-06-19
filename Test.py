import json

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
        data[i]["name"] = str("https://bit.ly/3xvZi3a" + str(id))
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
    return data


def sort_entries(data):
    # Liste der Dictionarys nach Wert des Keys "objekt_jahr" sortieren
    sorted_data = sorted(data, key=lambda x: x['objektjahr'])
    return sorted_data


def create_third_layer(data):
    anz_dict_0_249 = 0   #0-249
    anz_dict_250_499 = 0   #250-499
    anz_dict_500_749 = 0   #500-749
    anz_dict_750_999 = 0   #750-999
    anz_dict_1000_1099 = 0   #1000-1099
    anz_dict_1100_1249 = 0   #1100-1249
    anz_dict_1250_1399 = 0   #1250-1399
    anz_dict_1400_1499 = 0   #1400-1499
    anz_dict_1500_1599 = 0  # 1500-1599
    anz_dict_1600_1749 = 0  # 1600-1749
    anz_dict_1750_1899 = 0  # 1750-1899
    anz_dict_1900_1999 = 0  # 1900-1999
    anz_dict_2000_2009 = 0  # 2000-2009
    anz_dict_2010_2022 = 0  # 2010-2022

    liste_dict_0_499 = []
    liste_dict_500_999 = []
    liste_dict_1000_1249 = []
    liste_dict_1250_1499 = []
    liste_dict_1500_1799 = []
    liste_dict_1800_1999 = []
    liste_dict_2000_2022 = []


    for entry in data:
        if 0 <= int(entry["objektjahr"]) <= 499:
            liste_dict_0_499.append({"name": entry["name"], "value": 1})
            anz_dict_0_249 += 1
        if 500 <= int(entry["objektjahr"]) <= 999:
            liste_dict_500_999.append({"name": entry["name"], "value": 1})
            anz_dict_500_749 += 1
        if 1000 <= int(entry["objektjahr"]) <= 1249:
            liste_dict_1000_1249.append({"name": entry["name"], "value": 1})
            anz_dict_1000_1099 += 1
        if 1250 <= int(entry["objektjahr"]) <= 1499:
            liste_dict_1250_1499.append({"name": entry["name"], "value": 1})
            anz_dict_1250_1399 += 1
        if 1500 <= int(entry["objektjahr"]) <= 1799:
            liste_dict_1500_1799.append({"name": entry["name"], "value": 1})
            anz_dict_1500_1599 += 1
        if 1800 <= int(entry["objektjahr"]) <= 1999:
            liste_dict_1800_1999.append({"name": entry["name"], "value": 1})
            anz_dict_1750_1899 += 1
        if 2000 <= int(entry["objektjahr"]) <= 2022:
            liste_dict_2000_2022.append({"name": entry["name"], "value": 1})
            anz_dict_2000_2009 += 1
        else:
            print("\n")

    #Dictionaries zweiter Ebene erstellen
    dict_0_499 = {
     "name": "0-499",
     "children": liste_dict_0_499}
    dict_500_999 = {
     "name": "500-999",
     "children": liste_dict_500_999}
    dict_1000_1249 = {
        "name": "1000-1249",
        "children": liste_dict_1000_1249}
    dict_1250_1499 = {
        "name": "1250-1499",
        "children": liste_dict_1250_1499}
    dict_1500_1799 = {
        "name": "1500_1749",
        "children": liste_dict_1500_1799}
    dict_1800_1999 = {
        "name": "1750_1999",
        "children": liste_dict_1800_1999}
    dict_2000_2022 = {
        "name": "2000-2022",
        "children": liste_dict_2000_2022}


    #Dictionaries erster Ebene erstellen
    dict_0_999 = {
        "name": "0-999",
        "children": [dict_0_499, dict_500_999]}
    dict_1000_1499 = {
        "name": "1000_1499",
        "children": [dict_1000_1249, dict_1250_1499]}
    dict_1500_1999 = {
        "name": "1500-1999",
        "children": [dict_1500_1799, dict_1800_1999]}
    dict_2000_2022 = {
        "name": "2000-2022",
        "children": dict_2000_2022}


    #oberste Ebene erstellen
    dict_total = {
            "name": "flare",
            "children": [dict_0_999, dict_1000_1499, dict_1500_1999, dict_2000_2022]
    }
    print(dict_total)
    return dict_total


    #Einteilung nach Epochen:
    # 0-999 --- 0-499; 500-999; --- 0-249; 250-499; 500-749; 750-999
    # 1000-1499 --- 1000-1249; 1250-1499; --- 1000-1099; 1100-1249; 1250-1399; 1400-1499
    # 1500-1999 --- 1500-1749; 1750-1999; --- 1500-1599; 1600-1749; 1750-1899; 1900-1999
    # 2000-2022 --- 2000-2009; 2010-2020;


def write_file(data):
    file_name = "my-data.json"
    file = open(file_name, "w")
    json.dump(data, file)
    file.close()


def main():
    raw_data = read_file()
    cleaned_data = extract_info(raw_data)
    delete_false(cleaned_data)
    final_data = create_third_layer(cleaned_data)
    write_file(final_data)


if __name__ == "__main__":
    main()