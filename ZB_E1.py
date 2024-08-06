# Changement de valeur en fonction de la réponse de l'utilisateur
from asyncio.windows_events import NULL


def continue_or_not():
    response = input("Voulez-vous entrer un nouveau fichier? O/N  ")
    if('o' == response or 'O' == response):
        condition = True
        link = input("Entrez un lien de fichier csv ou xml : ")
    else:
        condition = False
        link = NULL
    return(condition, link)

def if_contains(data, tab_index):
    contiens = False
    for el_index in tab_index:
        if el_index == data:
            contiens = True
            break 
    return(contiens)

# Get csv datas
def read_csv(csv_link):
    import re
    import csv
    # ouverture du csv
    with open(csv_link) as csvfile:
        csv_reader  = csv.reader(csvfile, delimiter=';')
        clients = {}
        tab_index = []
        # on parcoure toute les lignes
        for index, row in enumerate(csv_reader): 
            lenght = len(row)
            client = {}
            # on parcoure les colonnes on ommettant la 1ère
            for i in range(lenght):
                if i+1<lenght:
                    data = row[i+1]
                    if index == 0:
                        if any(char.isdigit() for char in data):
                            data = data[:-1]
                        if not tab_index:
                            tab_index = [data]
                        else:
                            contiens = if_contains(data, tab_index)
                            if not contiens:
                                tab_index.append(data)
                    client_data = data
                    if i>2:
                        i=2
                    j = i
                    while not data: 
                        j = j+1
                        data = row[j] 
                    if (data != tab_index[i]):
                        not_same = True
                        client[tab_index[i]] = data
                    else:
                        not_same = False
            if (not_same):
                clients[index] = client
    return(clients)

# Get xml datas
def read_xml(xml_link):
    # import du xml 
    import xml.etree.ElementTree as ET
    tree = ET.parse(xml_link)
    root = tree.getroot()
    clients = {}
    i=1
    for client in root:
        client_data = {}
        for data in client:
            # on fait un tableau des données de chaque client
            client_data[data.tag] = data.text
        # on regroupe les données de chaque client dans un tableau global des clients
        clients[i] = client_data
        i = i+1
    return(clients)

# fusion des dictionnaires
def merge_datas(datas, data):
    if not datas:
        datas = data
    else:
        i=0
        for client_existant in enumerate(datas):
            i = i+1

        for client_encours, key in enumerate(data):
            datas[i] = data[key]
            i = i+1
    return(datas)

# conversion du dictionnaire en json
def dict_to_json(dict):
    import json
    json = json.dumps(dict, indent=4)  
    return(json)

link = input("Entrez un lien de fichier csv ou xml : ")
condition = True
datas = {}

while(condition):
    if(link.find(".")):
        extension = link[link.find(".")+1:]
        if (extension == "csv"):
            data_csv = read_csv(link) 
            datas = merge_datas(datas, data_csv)
            condition, link = continue_or_not()
        elif (extension == "xml"):
            data_xml = read_xml(link) 
            datas = merge_datas(datas, data_xml)
            condition, link = continue_or_not()
        else:
            print("Format non pris en charge")
            link = input("Entrez un lien de fichier csv ou xml : ")
        
json = dict_to_json(datas)

import json
where = input("Entrez le chemin de votre nouveau fichier JSON : ")    
path = where+"/data.json"
with open(path, 'w') as f:
    json.dump(datas, f, indent=4)
print("Votre fichier data.json à bien été enregistrer au dossier : \n"+where)
#data_csv = read_csv('C:/Users/mrvav/Desktop/liste1.csv')
#data_xml = read_xml('C:/Users/mrvav/Desktop/liste2.xml')