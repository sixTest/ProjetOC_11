# Description de l'application

Cette application est une plateforme numérique pour coordonner des competitions de force
(deadlifting, strongman) en Amérique du Nord et en Australie.

## Lancement de l'application

* Ouvrez un invite de commande
* Placez-vous dans le dossier contenant le répertoire Python_Testing
* Création de l'environnement virtuel : ```python -m venv env```
* Activation de l'environnement virtuel :
    * Pour Windows : ```env\Scripts\activate.bat```
    * Pour Linux   : ```env/bin/activate```
* Installation des dépendances : ```pip install -r requirements.txt```
* Creation de la variable d'environnement APP pour flask : ```set FLASK_APP=server.py```
* Si vous souhaité lancer l'environnement de test tapez :  ```set TESTING=1```
  * L'environnement de test est utile uniquement pour lancer les tests d'intégrations (integrations_test.py)
    ou les tests locust (locust_test.py)
  * Les tests unitaires peuvent etre lancer sur l'environnement par default  
  * Lorsque que vous souhaité re-basculer sur l'environnement par default tapez : ```set TESTING=0```  
* Lancement du serveur local : ```flask run```
* Ouvrez votre navigateur web a l'url : ```http://127.0.0.1:5000/```

### Details de connexion 

Environnement par default:
* Emails :
    * john@simplylift.co
    * admin@irontemple.com
    * kate@shelifts.co.uk
    * Ajoutez un club dans le fichier clubs.json (zone clubs)

Environnement test:
* Email:
    * club@test.com
