import json


def read_file():
    # Datei einlesen
    filename = "lmwallobjects.json"
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def extract_info(data):
    # Je Dictionary in JSON-Datei einen Dateneintrag für das (Erstellungs-) Jahr und ID hinzufügen
    i = 0
    for data[i] in data:
        # Jahr als Dictionary-Eintrag hinzufügen (aus Name)
        year = data[i]["objekt_name"]
        year_1 = year[-4:]
        year_2 = year[-3:]
        year_3 = year[-2:]
        year_4 = year[-1:]
        # Prüfen, ob year auch wirklich Jahreszahl ist oder nicht, wenn nicht "0" einfügen
        if year_1.isdigit() == True:
            data[i]["objektjahr"] = year_1
        elif year_2.isdigit() == True:
            data[i]["objektjahr"] = year_2
        elif year_3.isdigit() == True:
            data[i]["objektjahr"] = year_3
        elif year_4.isdigit() == True:
            data[i]["objektjahr"] = year_4
        else:
            data[i]["objektjahr"] = 102983
        # ID extrahieren
        id = data[i]["objekt_id"]
        data[i]["name"] = str(id)
        # nicht nötige Key-Value-Paare entfernen
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



def create_third_layer(data):
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
        elif 500 <= int(entry["objektjahr"]) <= 999:
            liste_dict_500_999.append({"name": entry["name"], "value": 1})
        elif 1000 <= int(entry["objektjahr"]) <= 1249:
            liste_dict_1000_1249.append({"name": entry["name"], "value": 1})
        elif 1250 <= int(entry["objektjahr"]) <= 1499:
            liste_dict_1250_1499.append({"name": entry["name"], "value": 1})
        elif 1500 <= int(entry["objektjahr"]) <= 1799:
            liste_dict_1500_1799.append({"name": entry["name"], "value": 1})
        elif 1800 <= int(entry["objektjahr"]) <= 1999:
            liste_dict_1800_1999.append({"name": entry["name"], "value": 1})
        elif 2000 <= int(entry["objektjahr"]) <= 2022:
            liste_dict_2000_2022.append({"name": entry["name"], "value": 1})
        else:
            print("")


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
        "name": "1500_1799",
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
    return dict_total


def write_file(data):
    file_name = "my-data.json"
    file = open(file_name, "w")
    json.dump(data, file)
    file.close()


def main():
    raw_data = read_file()
    cleaned_data = extract_info(raw_data)
    final_data = create_third_layer(cleaned_data)
    write_file(final_data)


if __name__ == "__main__":
    main()