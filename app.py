from blog.views import app, db
from blog.models import Category, Author, Paper
from datetime import datetime

app.run()


# autor_exemplo = Author.query.filter_by(name="Allan Carneiro").first()
# categoria_exemplo = Category.query.filter_by(name="fisica").first()
# data = datetime.strptime("10-10-2017", "%d-%m-%Y")
#
# db.session.add(Paper(title="C++ é uma linguagem", text="C++ é uma linguagem de programação compilada multi-paradigma"
#                           " e de uso geral. Desde os anos 1990 é uma das linguagens comerciais mais populares, "
#                           "sendo bastante usada também na academia por seu grande desempenho e base de "
#                           "utilizadores.",
#                       abstract="Resumo sobre +CC", cover="imagem2.png", published_date=data,
#                       author=autor_exemplo,
#                       last_modified=data, category=categoria_exemplo, published="Sim",
#                       slug="c++_e_uma_linguagem"))
#
# db.session.commit()

