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


def create_1700(data):

    # Leere Listen erstellen
    liste_dict_1800_1809 = []
    liste_dict_1810_1819 = []
    liste_dict_1820_1829 = []
    liste_dict_1830_1839 = []
    liste_dict_1840_1849 = []
    liste_dict_1850_1859 = []
    liste_dict_1860_1869 = []
    liste_dict_1870_1879 = []
    liste_dict_1880_1889 = []
    liste_dict_1890_1899 = []

    # jeden Dateneintrag zu Liste mit zugehörigem Entstehungsdatum hinzufügen
    for entry in data:
        if 1800 <= int(entry["objektjahr"]) <= 1809:
            liste_dict_1800_1809.append({"name": entry["name"], "value": 1})
        elif 1810 <= int(entry["objektjahr"]) <= 1819:
            liste_dict_1810_1819.append({"name": entry["name"], "value": 1})
        elif 1820 <= int(entry["objektjahr"]) <= 1829:
            liste_dict_1820_1829.append({"name": entry["name"], "value": 1})
        elif 1830 <= int(entry["objektjahr"]) <= 1839:
            liste_dict_1830_1839.append({"name": entry["name"], "value": 1})
        elif 1840 <= int(entry["objektjahr"]) <= 1849:
            liste_dict_1840_1849.append({"name": entry["name"], "value": 1})
        elif 1850 <= int(entry["objektjahr"]) <= 1859:
            liste_dict_1850_1859.append({"name": entry["name"], "value": 1})
        elif 1860 <= int(entry["objektjahr"]) <= 1869:
            liste_dict_1860_1869.append({"name": entry["name"], "value": 1})
        elif 1870 <= int(entry["objektjahr"]) <= 1879:
            liste_dict_1870_1879.append({"name": entry["name"], "value": 1})
        elif 1880 <= int(entry["objektjahr"]) <= 1889:
            liste_dict_1880_1889.append({"name": entry["name"], "value": 1})
        elif 1890 <= int(entry["objektjahr"]) <= 1899:
            liste_dict_1890_1899.append({"name": entry["name"], "value": 1})
        else:
            print("")


    #Dictionaries dritter Ebene erstellen aus vorher generierten Listen der Objekte
    dict_1800_1809 = {
     "name": "1800-1809",
     "children": liste_dict_1800_1809}
    dict_1810_1819 = {
     "name": "1810-1819",
     "children": liste_dict_1810_1819}
    dict_1820_1829 = {
        "name": "1820-1829",
        "children": liste_dict_1820_1829}
    dict_1830_1839 = {
        "name": "1830-1839",
        "children": liste_dict_1830_1839}
    dict_1840_1849 = {
        "name": "1840-1849",
        "children": liste_dict_1840_1849}
    dict_1850_1859 = {
        "name": "1850-1859",
        "children": liste_dict_1850_1859}
    dict_1860_1869 = {
        "name": "1860-1869",
        "children": liste_dict_1860_1869}
    dict_1870_1879 = {
        "name": "1870-1879",
        "children": liste_dict_1870_1879}
    dict_1880_1889 = {
        "name": "1880-1889",
        "children": liste_dict_1880_1889}
    dict_1890_1899 = {
        "name": "1890-1899",
        "children": liste_dict_1890_1899}


    #Dictionaries zweiter Ebene erstellen, indem die vorherigen Dictionaries zusammengefasst werden
    dict_1800_1849 = {
        "name": "1800-1849",
        "children": [dict_1800_1809, dict_1810_1819, dict_1820_1829, dict_1830_1839, dict_1840_1849]}
    dict_1850_1899 = {
        "name": "1850_1899",
        "children": [dict_1850_1859, dict_1860_1869, dict_1870_1879, dict_1880_1889, dict_1890_1899]}


    #oberste Ebene erstellen, indem die vorherigen Dictionaries zusammengefasst werde
    dict_total = {
            "name": "flare",
            "children": [dict_1800_1849, dict_1850_1899]
    }
    return dict_total


def write_file(data):

    # JSON-Datei schreiben lassen, die dann in D3JS verwendet wird
    file_name = "my-data.json"
    file = open(file_name, "w")
    json.dump(data, file)
    file.close()


def main():
    raw_data = read_file()
    cleaned_data = extract_info(raw_data)
    final_data = create_1700(cleaned_data)
    write_file(final_data)


if __name__ == "__main__":
    main()