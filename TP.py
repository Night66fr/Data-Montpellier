import requests
import json 
import time

response=requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000")
data = response.json()


with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('data.json') as file:
    data = json.load(file)

"""
with open("place_libre","w") as file : 
    for i in range(len(data)) :
        if data[i]['status']['value'] == 'Open' : 
            total_place_libre += data[i]['availableSpotNumber']['value']
            total_place += data[i]['totalSpotNumber']['value']
            pourcentage = (data[i]['totalSpotNumber']['value'] - data[i]['availableSpotNumber']['value']/data[i]['totalSpotNumber']['value'])*100
            pourcentage_arrondie = round(pourcentage,2)
            file.write(data[i]["name"]['value'] + " : " + str(data[i]['availableSpotNumber']['value']) + " place libre, " + str(pourcentage_arrondie) +"%" +" d occupation" + '\n' )  
    pourcentage_total_place = (total_place_libre/total_place)*100
    pourcentage_total_place= round(pourcentage_total_place,2)
    file.write("Le pourcentage de place libre au total est de : " + str(pourcentage_total_place) + "%")
"""
"""
def convertir_temps(temps_unix):
    structure_temps = time.localtime(temps_unix)
    date_lisible = time.strftime("%d/%m/%Y %H:%M:%S", structure_temps)
    return date_lisible

nom_fichier = "Donnée_SAE_parking"
nom_fichier1 = "Donnée_SAE_velo"

temps_arret_heure = 0
temps_arret_minutes = temps_arret_heure*60
temps_arret_seconde = 10

duree_jour = 0
duree_heure = duree_jour*24 
duree_minutes = 1
duree_secondes = duree_minutes * 60

nb_mesures = duree_secondes // temps_arret_seconde

with open(nom_fichier, "a") as file:
    for i in range(nb_mesures):
        response = requests.get("https://portail-api-data.montpellier3m.fr/offstreetparking?limit=1000") 
        data = response.json() 
        temps_mesure = int(time.time()) 
        temps = convertir_temps(temps_mesure)
        for j in range(len(data)):
            if data[j]['status']['value'] == 'Open': 
                nom = data[j]["name"]['value']
                libres = data[j]['availableSpotNumber']['value'] 
                total_place = data[j]["totalSpotNumber"]["value"]
                place_occuper = (data[j]['totalSpotNumber']['value']-data[j]['availableSpotNumber']['value']) 
                pourcentage = (place_occuper/total_place)*100
                ligne = f"{temps} | {nom} | Libres: {libres} | Total : {total_place} | {round(pourcentage, 2)}% d occupation\n"
                file.write(ligne)
            
        file.write("-" * 50 + "\n") 
        file.flush()

        if i < nb_mesures - 1:
            time.sleep(temps_arret_seconde) 

with open(nom_fichier1, "a") as file_1 : 
    for i in range(nb_mesures):
        response_1 = requests.get("https://portail-api-data.montpellier3m.fr/bikestation?limit=1000") 
        data_1 = response_1.json() 
        temps_mesure_1 = int(time.time()) 
        temps_1 = convertir_temps(temps_mesure_1)
        for j in range(len(data_1)):
            if data_1[j]['status']['value'] == 'working': 
                nom_1 = data_1[j]["name"]['value']
                libres_1 = data_1[j]['availableBikeNumber']['value'] 
                total_place_1 = data_1[j]["totalSlotNumber"]["value"]
                place_occuper_1 = (data_1[j]['totalSlotNumber']['value']-data_1[j]['availableBikeNumber']['value']) 
                pourcentage_1 = (place_occuper_1/total_place_1)*100
                ligne_1 = f"{temps_1} | {nom_1} | Libres: {libres_1} | Total : {total_place_1} | {round(pourcentage_1, 2)}% d occupation\n"
                file_1.write(ligne)
            
        file_1.write("-" * 50 + "\n") 
        file_1.flush()

        if i < nb_mesures - 1:
            time.sleep(temps_arret_seconde) 
"""