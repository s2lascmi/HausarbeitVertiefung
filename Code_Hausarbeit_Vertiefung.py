import json


def read_file():

    # Datei einlesen
    filename = "lmwallobjects.json"
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def extract_info(data):

    # JSON-Datei mit allen Objekten der Sammlung Online einlesen
    # Je Dictionary (also je Objekt) in JSON-Datei einen Dateneintrag für (Erstellungs-) Jahr und ID hinzufügen
    i = 0
    for data[i] in data:

        # Jahr als Dictionary-Eintrag hinzufügen (aus Name des Objekts extrahieren über letzte vier Zeichen)
        year = data[i]["objekt_name"]
        year = year[-4:]

        # Prüfen, ob year auch wirklich Jahreszahl ist oder nicht, wenn nicht "102983" einfügen
        if year.isdigit():
            data[i]["objektjahr"] = year
        else:
            data[i]["objektjahr"] = 102983

        # ID extrahieren und für Enddatei als "Name" speichern, um Struktur des vorhandenen D3JS-Skripts zu imitieren
        # (in Enddatei wird das Sammlungsobjekt über die ID referenziert)
        id = data[i]["objekt_id"]
        data[i]["name"] = "ID: " + str(id)

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

    # bereinigte Daten zurückgeben, bestehend aus Objektjahr und ID
    return data


def create_1800(data):
    
    # Erstellt die Gesamtstruktur der JSON-Datei, die dann in D3JS-Skript eingelesen wird
    # Die Struktur besteht aus ineinander geschachtelten Dictionarys, welche letztendlich die einzelnen Detailebenen des Kuchendiagramms ergeben

    # Leere Listen für Jahrzehnte erstellen, in die die Objekte nach Jahr einsortiert werden
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
    # Objekt wird hier schon als Dictionary eingefügt mit Key "name" und Value 1, um Struktur des D3JS-Skripts zu imitieren
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


    # Dictionaries dritter Ebene erstellen aus vorher generierten Listen der Objekte
    # für Enddarstellung in Kuchendiagramm: zweite, detailliertere Zoomstufe
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


    # Dictionaries zweiter Ebene erstellen, indem die vorherigen Dictionaries zusammengefasst werden
    # für Enddarstellung in Kuchendiagramm: erste Zoomstufe
    dict_1800_1849 = {
        "name": "1800-1849",
        "children": [dict_1800_1809, dict_1810_1819, dict_1820_1829, dict_1830_1839, dict_1840_1849]}
    dict_1850_1899 = {
        "name": "1850_1899",
        "children": [dict_1850_1859, dict_1860_1869, dict_1870_1879, dict_1880_1889, dict_1890_1899]}


    # oberste Ebene erstellen, indem die vorherigen Dictionaries zusammengefasst werde
    # für Enddarstellung in Kuchendiagramm: Anfangsansicht
    dict_total = {
            "name": "flare",
            "children": [dict_1800_1849, dict_1850_1899]
    }
    return dict_total


def write_file(data):

    # JSON-Datei schreiben, die dann in D3JS-Skript verwendet wird
    file_name = "objects-1800-1899.json"
    file = open(file_name, "w")
    json.dump(data, file)
    file.close()


def main():
    raw_data = read_file()
    cleaned_data = extract_info(raw_data)
    final_data = create_1800(cleaned_data)
    write_file(final_data)


if __name__ == "__main__":
    main()
