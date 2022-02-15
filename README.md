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
. ## GET/books

    GENERAL:
        Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 
    
        
    EXEMPLE: curl https://bookapi-v1.herokuapp.com/books
```
        {
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
            "auteur": "Louis Saulnier, Théodore Gringoire",
            "code_ISBN": "978-2-0802",
            "date_publication": "26-02-2022",
            "editeur": "Flammarion",
            "id": 3,
            "titre": "Le répertoire de la cuisine"
        },
        {
            "auteur": "Katia Bricka",
            "code_ISBN": "978-2-8977",
            "date_publication": "25-02-2022",
            "editeur": "Modus Vivendi",
            "id": 4,
            "titre": "La recette parfaite"
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
    "status_code": 200,
    "success": true,
    "total_books": 4
}
```

.##GET/books(book_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: https://bookapi-v1.herokuapp.com/books/3
```
    {
        "auteur": "Louis Saulnier, Théodore Gringoire",
        "code_ISBN": "978-2-0802",
        "date_publication": "26-02-2022",
        "editeur": "Flammarion",
        "id": 3,
        "titre": "Le répertoire de la cuisine"
    }
```


. ## DELETE/books (book_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE https://bookapi-v1.herokuapp.com/books/4
```
    {
        "id_book": 4,
        "new_total": 3,
        "success": true
    }
```

. ##PATCH/books(book_id)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH https://bookapi-v1.herokuapp.com/books/1 -H "Content-Type:application/json" -d '{"auteur": "Azychika, Takumi Fukui","editeur": "Ki-oon","titre": "Jujutsu Kaisen"}'
  ```
  ```
    {
        "auteur": "Azychika, Takumi Fukui",
        "code_ISBN": "979-1-0327",
        "date_publication": "03-02-2022",
        "editeur": "Ki-oon",
        "id": 1,
        "titre": "Jujutsu Kaisen"
    }
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
    
        
    EXEMPLE: curl https://bookapi-v1.herokuapp.com/categories

        {
    "category": [
        {
            "categorie": "Litterature",
            "id": 1
        },
        {
            "categorie": "Humour",
            "id": 2
        },
        {
            "categorie": "Tourisme et voyage",
            "id": 3
        },
        {
            "categorie": "Histoire",
            "id": 5
        },
        {
            "categorie": "Cuisine",
            "id": 6
        },
        {
            "categorie": "Droit et Economie",
            "id": 7
        },
        {
            "categorie": "Informatique et internet",
            "id": 8
        },
        {
            "categorie": "Sciences sociales",
            "id": 9
        },
        {
            "categorie": "Essais et documents",
            "id": 10
        },
        {
            "categorie": "Religion et spiritualité",
            "id": 11
        },
        {
            "categorie": "Art, musique et cinéma",
            "id": 12
        },
        {
            "categorie": "Bandes Dessinées",
            "id": 4
        }
    ],
    "status_code": 200,
    "success": true,
    "total": 12
}
```

.##GET/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: https://bookapi-v1.herokuapp.com/categories/6
```
    {
        "categorie": "Cuisine",
        "id": 6
    }
```

. ## DELETE/categories (categories_id)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE https://bookapi-v1.herokuapp.com/categories/11
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
  ``` curl -X PATCH 'https://bookapi-v1.herokuapp.com/categories/4' -H "Content-Type:application/json" -d '{"categorie": "Bandes Dessinées"}'
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

    EXEMPLE: https://bookapi-v1.herokuapp.com/categories/4/books
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
