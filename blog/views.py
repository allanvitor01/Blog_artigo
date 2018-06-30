from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)



from .models import Paper
from .models import Author
from .models import Category

@app.route("/")
def pagina_home():

    artigo = Paper.query.all()
    autor = Author.query.all()
    id_autor = Author.query.all()
    categoria = Category.query.all()

    return render_template("index.html", artigo=artigo, autor=autor, categoria=categoria)



@app.route("/blog/")
def pagina_blog_geral():

    artigo = Paper.examples()

    return render_template("blog_geral.html", artigo_exibir=artigo)



@app.route("/blog/<slug>")
def pagina_blog(slug):

    artigo = Paper.query.filter_by(slug=slug)
    tamanho = len(Paper.query.all())

    for i in range(tamanho):
        if artigo[i].slug == slug:
            return render_template("blog.html", artigo_exibir=artigo[0])



