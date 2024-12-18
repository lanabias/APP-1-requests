import requests
from ..app import app
from flask import render_template

@app.route("/")
def accueil():
    return render_template("pages/accueil.html")

#Définition de la route retrieve_wikidata
#Il s'agit d'une route avec paramètre : ici le paramètre de la route est un entier nommé id
@app.route("/retrieve_wikidata/<string:id>")
#Définition de la fonction qui génère le contenu de la route retrieve_wikidata avec prise en compte du paramètre de la route id
def retrieve_wikidata(id:str):
   '''
    Fonction interroge l'API wikidata pour récupérer les données json d'un objet wikidata spécifique

    Paramètres d'entrée :
        id : l'identifiant de l'objet
    Paramètres de la requête :
        url_base : l'url dde base de l'API wikidata à requêter sans les paramètres
        action : Wbgetentities : réupère les informations d el'objet wikidata dont on connait l'identifiant
        format : json, format de réponse en retour, en json
        language : fr, la langue de la réponse
    
    Sortie : les données json à parser liées à l'objet wikidata id et à envoyer au template
   '''
   #construction de l'url wikidata
   url_base='https://www.wikidata.org/w/api.php?action='

   params = {
            "action": "wbgetentities",
            "ids": id,
            "format": "json"
        }

    #envoi des paramètres identifiant et réponse API Wikidata au template
   url_requete=url_base+params.get("action")+'&'+'format='+params.get("format")+'&'+'ids='+params.get("ids")
   resp=requests.get(url_requete) 
   return render_template("pages/accueil.html", code=id, reponse=resp)

