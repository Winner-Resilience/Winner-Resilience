import hashlib
import requests
import speech_recognition as sr
from urllib.request import urlopen


#declaration des variables
departure = "Douala"
arrival = "yaounde"
date = "13-07-2023"
language    = "fr";
version     = "1.0";
hash_value      = "md5(api_key+departure+arrival+date+language+version)";
api_key = "rh8b2v4tLJ2avDBZ"
url_api = "https://www.lohce.com"

#Importation des fichier vocaux

fichier_vocal1 = "c:\\Users\\USER\\Downloads\\query_voice_fr.wav" 

fichier_vocal2 = "c:\\Users\\USER\\Downloads\\query_voice_en.wav"

#Utilisation de la  technique de reconnaissance vocale pour extraire la requête audio
reconnaissance = sr.Recognizer()
with sr.AudioFile(fichier_vocal1) as source:
    audio = reconnaissance.record(source)
    texte_reconnu1 = reconnaissance.recognize_google(audio, language="fr-FR")
    
    reconnaissance = sr.Recognizer()
with sr.AudioFile(fichier_vocal2) as source:
    audio = reconnaissance.record(source)
    texte_reconnu2 = reconnaissance.recognize_google(audio, language="en-EN")
    
    # formulation de la requête à envoyer à l'API LOHCE
    requete1 = {"requete": texte_reconnu1,
                "departure":"departure" ,
                "arrival":"arrival",
                "date":"date",
                "version":"version",
                "language":"language"}
    
    requete2 = {"requete": texte_reconnu2}

# Calcul du hash
hash_string = api_key + departure + arrival + date + language + version
hash_value = hashlib.md5(hash_string.encode()).hexdigest()
   
headers={
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}",
  "Hash": hash_value
}  


# URL de l'API LOHCE
#url_api = "https://lohce.com/apiusers/gettravels"
#url_api = f"https://lohce.com/apiusers/gettravels?departure={departure}&arrival={arrival}&date={date}"
#url_api = "https://www.lohce.com"

# Envoi de la requête post
response1 = requests.post(url_api,headers=headers,json=requete1)
response2 = requests.post(url_api,headers=headers,json=requete2)

print(texte_reconnu1)
print(texte_reconnu2)  
print(response1)
print(response2)