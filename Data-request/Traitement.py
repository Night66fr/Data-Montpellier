import json
import re

def nettoyer_nom_variable(nom):
    nom = nom.replace(" ", "_").replace("-", "_").replace("'", "_")
    nom = re.sub(r'[^\w]', '', nom) 
    return nom

def generer_donnees_py(nom_fichier_source, nom_fichier_py):
    try:
        with open(nom_fichier_source, "r", encoding="utf8") as f:
            donnees_brutes = json.load(f)
        dictionnaire_temp = {}
        for entree in donnees_brutes:
            nom_objet = entree.get("id") or entree.get("type")
            if nom_objet and "place" in entree:
                occ_str = entree["place"]["occupation"]
                valeur = float(occ_str.replace('%', ''))
                
                if nom_objet not in dictionnaire_temp:
                    dictionnaire_temp[nom_objet] = []
                dictionnaire_temp[nom_objet].append(valeur)

        with open(nom_fichier_py, "w", encoding="utf8") as f_out:
            f_out.write("# Fichier de données généré automatiquement\n\n")
            for nom, liste_valeurs in dictionnaire_temp.items():
                nom_var = nettoyer_nom_variable(nom)
                f_out.write(f"{nom_var} = {liste_valeurs}\n")
        
        print(f"✅ Terminé ! Le fichier '{nom_fichier_py}' est prêt.")

    except Exception as e:
        print(f"❌ Erreur : {e}")
        
generer_donnees_py("Donnée_SAE_Parking", "donnees_parking.py")
generer_donnees_py("Donnée_SAE_velo", "donnees_velo.py")