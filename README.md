# API D'AFFICHAGE DES LIVRES VERSION 1

## Création d'une api pour l'affichage des livres et leurs categories notamment ,la modification ,l'affichage,la suppression


#### Python 3.8.10


Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/windows/#getting-and-installing-the-latest-version-of-python)


## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur linux, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
``` 

## REFERENCE DE L'API

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sou forme d'objet au format Json:
{
    "success":False
    "error": 400
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request ou ressource non disponible
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## /livres

    GENERAL:
        Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 
    
        
    EXEMPLE: curl https://127.0.0.1:5000/livres
```
        {
    "Livre": [
        {
            "ISBN": "978-2-8891-5263-6",
            "cat": 1,
            "date_publication": "Fri, 01 Mar 2019 00:00:00 GMT",
            "nomAuteur": "Walter Issacson",
            "nomEditeur": "Quanto",
            "titre": "LÉONARDO DE VINCI"
        },
        {
            "ISBN": "978-2-3657-7710-0",
            "cat": 2,
            "date_publication": "Fri, 11 Feb 2022 00:00:00 GMT",
            "nomAuteur": " O'Neil Dennis",
            "nomEditeur": "Urban Comics",
            "titre": "Batman - Tales of the Demon"
        },
        {
            "ISBN": "1222",
            "cat": 2,
            "date_publication": "Sat, 01 Feb 2020 00:00:00 GMT",
            "nomAuteur": "alko",
            "nomEditeur": "ki",
            "titre": "jjd"
        },
        {
            "ISBN": "127-022-021-202-10",
            "cat": 1,
            "date_publication": "Wed, 02 Feb 2022 00:00:00 GMT",
            "nomAuteur": "Ferdinand OYONO",
            "nomEditeur": "David PILON",
            "titre": "une vie de boy"
        }
    ],
    "succes": true,
    "total": 4
}
```

.##GET/livre(id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: https://127.0.0.1:5000/livres/3
```
    {
    "Livre": {
        "ISBN": "978-2-8891-5263-6",
        "cat": 1,
        "date_publication": "Fri, 01 Mar 2019 00:00:00 GMT",
        "nomAuteur": "Walter Issacson",
        "nomEditeur": "Quanto",
        "titre": "LÉONARDO DE VINCI"
    },
    "succes": true
}
```


. ## DELETE/books (book_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE https://127.0.0.1:5000/books/4
```
    {
        "id_book": 4,
        "new_total": 3,
        "success": true
    }
```

. ##PATCH/livre(livre_id)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH https://127.0.0.1:5000/livres/3-H "Content-Type:application/json" -d '{
        "id_book": 4,
        "new_total": 3,
        "success": true
    }'
  ```
  ```
   {
        "id_book": 4,
        "new_total": 3,
        "success": true
    }
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
    
        
    EXEMPLE: curl https://127.0.0.1:5000/categories

        {
    "Categorie": [
        {
            "id": 2,
            "libelle": "Bande dessinée"
        },
        {
            "id": 4,
            "libelle": "Cuisine"
        },
        {
            "id": 5,
            "libelle": "Developpement  personnel"
        },
        {
            "id": 6,
            "libelle": "Droit et economie"
        },
        {
            "id": 7,
            "libelle": "Humour"
        },
        {
            "id": 8,
            "libelle": "Jeunesse"
        },
        {
            "id": 10,
            "libelle": "Théâtre"
        },
        {
            "id": 13,
            "libelle": "Informatique et Internet"
        },
        {
            "id": 14,
            "libelle": "fiction"
        },
        {
            "id": 9,
            "libelle": "policier"
        },
        {
            "id": 1,
            "libelle": "film et serie"
        },
        {
            "id": 19,
            "libelle": "testrer"
        }
    ],
    "succes": true,
    "total": 12
}
```

.##GET/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: https://127.0.0.1:5000/categories/6
```
    {
    "Categorie": {
        "id": 6,
        "libelle": "Droit et economie"
    },
    "succes": true
}
```

. ## DELETE/categories (categories_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE https://127.0.0.1:5000/categories/11
```
    {
        "id_cat": 11,
        "new_total": 10,
        "status": 200,
        "success": true
    }
```

. ##PATCH/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'https://127.0.0.1:5000/categories/4' -H "Content-Type:application/json" -d '{"categorie": "Bandes Dessinées"}'
  ```
  ```
    {
        "categorie": "Bandes Dessinées",
        "id": 4
    }

.##GET/books/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée.
  Il renvoie la classe de la categorie et les livres l'appartenant.

    EXEMPLE: https://127.0.0.1:5000/categories/4/books
```
    {
    "Status_code": 200,
    "Success": true,
    "books": [
        {
            "auteur": "Gege Atakumi",
            "code_ISBN": "979-1-0328",
            "date_publication": "03-02-2022",
            "editeur": "Ki-oon",
            "id": 2,
            "titre": "Jujutsu Kaisen T13"
        },
        {
            "auteur": "Azychika, Takumi Fukui",
            "code_ISBN": "979-1-0327",
            "date_publication": "03-02-2022",
            "editeur": "Ki-oon",
            "id": 1,
            "titre": "Jujutsu Kaisen"
        }
    ],
    "classe": {
        "categorie": "Bandes Dessinées",
        "id": 4
    }
}
```

