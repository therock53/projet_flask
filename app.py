from crypt import methods
import psycopg2
from flask import Flask, jsonify, request, url_for, abort#importer Flask
from flask_sqlalchemy import SQLAlchemy#importer SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)#Créer une instance de l'application

#connexion à la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lorna:password@localhost:5432/projet_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

#Créer une instance de BD
db = SQLAlchemy(app)

#Creation de la table categories
class Categorie(db.Model):

    __tablename__ = 'categories'#nom de la table

    #Attributs de la table
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(), nullable=False)
    livres = db.relationship('Livre', backref="categories", lazy=True)


    #Constructeur
    def __init__(self, id, libelle):
        self.id = id
        self.libelle = libelle

    def delet(self):
        db.session.delete(self)
        db.session.commit()

    def forma(self):
        return {
            'id': self.id,
            'libelle': self.libelle
        }

    def updat(self):
        db.session.commit()

    def inser(self):
        db.session.add(self)
        db.session.commit()

#Création de la classe Livre
class Livre(db.Model):
    __tablename__ = 'livres'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(5), unique=True, nullable=False)
    titre = db.Column(db.String(), nullable=False)
    datepublication = db.Column(db.DateTime, nullable=False)
    autheur = db.Column(db.String(), nullable=False)
    editeur = db.Column(db.String(), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)
    #Constructeur
    def __init__(self, isbn, titre, datepublication, autheur, editeur, categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.datepublication = datepublication
        self.autheur = autheur
        self.editeur = editeur
        self.categorie_id = categorie_id

    def delet(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'ISBN': self.isbn,
            'titre': self.titre,
            'date_publication': self.datepublication,
            'nomAuteur': self.autheur,
            'nomEditeur': self.editeur,
            'cat': self.categorie_id
        }

    def update(self):
        db.session.commit()

    def insert(self):
        db.session.add(self)
        db.session.commit()


db.create_all()


@app.route('/', methods=['GET'])
def Accueil():
    return '''
    <h1>
    Projet de construction d'une Application de Progammation d'Interface</br> permettant de gérer les livres d'une bibliothèque.
     Cette API a pour but </br>de classer les livres par catégories, de rechercher les livres par leur titre,</br> d'enregistrer un nouveau livre, de créer des catégories.
    </h1>
    '''

#Affichage de tous les livres
@app.route('/livres/', methods=['GET'])
def get_all_livres():
    livres = Livre.query.all()
    books = [livre.format() for livre in livres]
    return jsonify({
        'succes': True,
        'Livre': books,
        'total': Livre.query.count()
    })

#Affichage de toutes les categories de livres
@app.route('/categories/', methods=['GET'])
def get_all_categories():
    cate = Categorie.query.all()
    categorie = [cat.forma() for cat in cate]
    return jsonify({
        'succes': True,
        'Categorie': categorie,
        'total': Categorie.query.count()
    })

#Affichage des livres par categorie
@app.route('/categories/<int:i>/livres', methods=['GET'])
def livre_by_categorie(i):
    try:
        p=Livre.query.filter_by(categorie_id=i)
        if p is None:
            return abort(404)
        else:
            pq=[cat.format() for cat in p]
            return jsonify({
                'succes': True,
                'books': pq,
                'total': len(pq)

            })
    except:
       return abort(400)
       
 
#Affichage d'un livre spécifiques 
@app.route('/livres/<int:i>', methods=['GET'])
def recherchelivre(i):
    p = Livre.query.get(i)
    pq = p.format()
    return jsonify({
        'succes': True,
        'Livre': pq,
    })

#Affichage d'une categorie spécifique
@app.route('/categories/<int:i>', methods=['GET'])
def recherchecategorie(i):
    p = Categorie.query.get(i)
    pq = p.forma()
    return jsonify({
        'succes': True,
        'Categorie': pq,
    })

#Suppression d'un livre
@app.route('/delete_livre/<int:i>', methods=['GET','DELETE'])
def delete_livre(i):
    try:
        p = Livre.query.get(i)
        print(p)
        if p is None:
            abort(404)
        else:
            p.delet()
            return jsonify({
                'succes': True,
                'delete id': i,
                'total': Livre.query.count()

            }) 
    except:
         abort(400)
        

#Suppression d'une categorie
@app.route('/delete_categorie/<int:i>', methods=['GET','DELETE'])
def delete_categorie(i):
    try:
        p = Categorie.query.get(i)
        if p is None:
            abort(404)
        else:
            p.delet()
            return jsonify({
                'succes': True,
                'delete id': i,
                'total': Categorie.query.count()

            })
    except:
        abort(400)

#Modification d'un livre
@app.route('/update_livre/<int:i>', methods=['GET','PATCH'])
def update_livre(i):
    body = request.get_json()
    livre = Livre.query.get(i)
    try:
        livre.isbn = body.get('isbn', None)
        livre.titre = body.get('titre', None)
        livre.datepublication = body.get('date_publication', None)
        livre.autheur = body.get('nomAuteur', None)
        livre.editeur = body.get('nomEditeur', None)
        print('bonjour')
        if (livre.isbn is None or livre.titre is None or 
        livre.datepublication is None or livre.autheur is None or livre.editeur is None):
            abort(400)
        else:
            
            livre.update()
            return jsonify({
                'succes': True,
                'update id': i,
                'nouveau livre': livre.format()

            })
    except:
        abort(400)
        

#Modification d'une categorie
@app.route('/update_categorie/<int:i>', methods=['GET','PATCH'])
def update_categorie(i):
    try:
        body = request.get_json()
        categorie = Categorie.query.get(i)
        categorie.libelle = body.get("libelle", None)
        if (categorie.libelle is None):
            print(categorie)
            abort(400)
        else:
            categorie.updat()
            return jsonify({
                'succes': True,
                'update id': i,
                'new': categorie.forma()

            })
    except:
        abort(400)

# try:
#         body = request.get_json()
#         categorie = Categorie.query.get(i)
#         categorie.libelle = body.get("libelle", None)
#         if (categorie.libelle is None):
#             print(categorie)
#             abort(400)
#         else:
#             categorie.updat()
#             return jsonify({
#                 'succes': True,
#                 'update id': i,
#                 'new': categorie.forma()

#             })
#     except:
#         abort(400)

                
@app.errorhandler(404)
def not_found(error):
            return jsonify(
                    {
                            "success":False,
                            "error":404,
                            "Cause":"Elément non trouvé"
                    }
            ),404
        
        
@app.errorhandler(400)
def erreur_client(errror):
            return jsonify(
                    {
                            "success":False,
                            "error":400,
                            "Cause":"Elément envoyé non valide"
                    }
            ),400
        
@app.errorhandler(500)
def erreur_serveur(error):
            return jsonify(
                    {
                            "success":False,
                            "error":500,
                            "Cause":"L'appli a crashé"
                    }
            ),500        
# @app.errorhandler(None)
# def erreur_serveur(error):
#             return jsonify(
#                     {
#                             "success":False,
#                             "error":NoneType,
#                             "Cause":"Identifiant invalide"
#                     }
#             )
if __name__ == '__main__':
    app.run(debug=True)
