from blog.views import app, db
from blog.models import Category, Author, Paper
from datetime import datetime

app.run()

# db.session.add(Author(name="Allan Carneiro", email="allanvitor.carneiro@gmail.com",
#                       website="allancarneiro.webbly.com", photo="fotoperfil.jpeg",
#                       bio="Sou estudante de Física na UFRJ, e participo do Programa de Ensino Python Café"))
# db.session.add(Author(name="Joao Vitor", email="joao.vitor@yahoo.com.br", website="facebook.com/joao.vitor",
#                       photo="foto_joao.jpeg", bio="Sou um exemplo de pessoa, estudo e trabalho e ainda tenho "
#                                                   "tempo para jogar futebol"))
#
#
# autor_exemplo = Author.query.filter_by(name="Allan Carneiro").first()
# categoria_exemplo = Category.query.filter_by(name="fisica").first()
# data = datetime.strptime("10-10-2017", "%d-%m-%Y")
#
#
#
# db.session.add(Paper(title="Python é uma linguagem", text="Python é uma linguagem de programação de alto nível, "
#                                                           "interpretada, de script, imperativa, orientada a objetos, funcional, "
#                                                           "de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.",
#                      abstract="Aqui é um resumo sobre python", cover="imagem.png", published_date=data,
#                      author=autor_exemplo,
#                      last_modified=data, category=categoria_exemplo, published="Sim",
#                      slug="python_e_uma_linguagem"))
#
#
# #db.session.add(Category(name='fisica'))
# #db.session.add(Category(name='Programacao'))
# db.session.commit()

