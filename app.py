from crypt import methods
import psycopg2
from flask import Flask, jsonify, request, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lorna:password@localhost:5432/projet_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)
# class Person(db.Model):
#      __tablename__ = 'persons'
#      id = db.Column(db.Integer, primary_key=True)
#      name = db.Column(db.String(), nullable=False)


class Categorie(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    libelle = db.Column(db.String(), nullable=False)
    livres = db.relationship('Livre', backref="categories", lazy=True)

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

    def __init__(self, isbn, titre, datepublication, autheur, editeur, categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.datepublication = datepublication
        self.autheur = autheur
        self.editeur = editeur
        self.categorie_id = categorie_id

    def deleter(self):
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
    <h1> ARCHIVE DE LECTURE A DISTANCE</h1>
    <p>Un prototype d'API pour les  romans .</p>

    '''


@app.route('/livres/', methods=['GET'])
def get_all_livres():
    livres = Livre.query.all()
    books = [livre.format() for livre in livres]
    return jsonify({
        'succes': True,
        'Livre': books,
        'total': Livre.query.count()
    })


@app.route('/categories/', methods=['GET'])
def get_all_categories():
    cate = Categorie.query.all()
    categorie = [cat.forma() for cat in cate]
    return jsonify({
        'succes': True,
        'Categorie': categorie,
        'total': Categorie.query.count()
    })

# @app.route('/newbook',methods=['POST'])
# def newbook():
#     isbn=request.form.get('isbn','')
#     titre=request.form.get('titre','')
#     datepublication=request.form.get('datepublication','')
#     autheur=request.form.get('autheur','')
#     editeur=request.form.get('editeur','')
#     livre=Livre(isbn=isbn,titre=titre,datepublication=datepublication,autheur=autheur,editeur=editeur)
#     livre.insert()
#     return redirect(url_for('index'))


# @app.route('/newcategorie',methods=['POST'])
# def newcategorie():
#     libelle=request.form.get('libelle','')
#     categorie=Livre(libelle=libelle)
#     categorie.inser()
#     return redirect(url_for('index'))


# @app.route('/newlivre',methods=['POST'])
# def newlivre():
#     body=request.get_json()
#     isbn=body.get('nom',None)
#     titre=body.get('nom',None)
#     datepublication=body.get('nom',None)
#     autheur=body.get('nom',None)
#     editeur=body.get('email',None)
#     etudiant=Livre(isbn=isbn,titre=titre,datepublication=datepublication,autheur=autheur,editeur=editeur)
#     etudiant.insert()
#     etudiants=Livre.query.all()
#     etu=[etudiant.format() for et in etudiants]
#     return jsonify({
#                 'succes':True,
#                 'Livre':etu,
#                 'total':Livre.query.count()

#             })


# @app.route('/newcat',methods=['POST'])
# def newcat():
#     body=request.get_json()
#     libelle=body.get('nom',None)
#     lib=Livre(libelle=libelle)
#     lib.insert()
#     ca=Livre.query.all()
#     categ=[c.forma() for c in ca]
#     return jsonify({
#                 'succes':True,
#                 'Categorie':categ,
#                 'total':Categorie.query.count()

#             })

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
       
    # p = Livre.query.filter_by(categorie_id=i).all()
    # if p is None:
    #         abort(404)
    # else:
    #         pq=[cat.format() for cat in p]
    #         return jsonify({
    #             'succes': True,
    #             'books': pq,
    #             'total': Livre.query.count()

    #         })
    
@app.route('/livres/<int:i>', methods=['GET'])
def recherchelivre(i):
    p = Livre.query.get(i)
    pq = p.format()
    return jsonify({
        'succes': True,
        'Livre': pq,
    })


@app.route('/categories/<int:i>', methods=['GET'])
def recherchecategorie(i):
    p = Categorie.query.get(i)
    pq = p.forma()
    return jsonify({
        'succes': True,
        'Categorie': pq,
    })


@app.route('/delete_livre/<int:i>', methods=['GET','DELETE'])
def delete_livre(i):
    try:
        p = Livre.query.get(i)
        if p is None:
            abort(404)
        else:
            p.deleter()
            return jsonify({
                'succes': True,
                'delete id': i,
                'total': Livre.query.count()

            }) + '''
            
            <h1>SUPPRESSION EFFECTUÉE</h1>
            '''
    except:
        abort(400)


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


@app.route('/update_livre/<int:i>', methods=['GET','PATCH'])
def update_livre(i):
    try:
        body = request.get_json()
        livre = Livre.query.get(i)
        livre.isbn = body.get("nom", None)
        livre.titre = body.get("adresse", None)
        livre.datepublication = body.get("email", None)
        livre.autheur = body.get("nom", None)
        livre.editeur = body.get("adresse", None)
        if (livre.isbn is None or livre.titre is None or livre.datepublication is None or livre.auteur is None or livre.editeur is None):
            abort(400)
        else:
            livre.update()
            return jsonify({
                'succes': True,
                'update id': i,
                'new': livre.format()

            })
    except:
        abort(400)


@app.route('/update_categorie/<int:i>', methods=['PATCH'])
def update_categorie(i):
    try:
        body = request.get_json()
        categorie = Categorie.query.get(i)
        categorie.libelle = body.get("libelle", None)
        if (categorie.libelle in None):
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

if __name__ == '__main__':
    app.run(debug=True)
