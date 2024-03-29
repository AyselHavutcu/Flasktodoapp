from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/HP/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
    todos  = Todo.query.all()#veriler sozluk seklinde sırayla gelecek
    return render_template("index.html",todos = todos)
@app.route("/add",methods =["POST"])
def addTodo():
    title = request.form.get("title")

    newTodo = Todo(title = title ,complete =False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/complete/<string:id>")
def complete(id):
    todo = Todo.query.filter_by(id = id).first()
    todo.complete = not todo.complete#bu bize if condition ı saglıyor yani eger true ise false false ise true yapıyor
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/delete/<string:id>")
def delete(id):
     todo = Todo.query.filter_by(id = id).first()
     db.session.delete(todo)
     db.session.commit()
     return redirect(url_for("index"))
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

if __name__ == "__main__":
    db.create_all() #olusmus tabloları bu arkadas bidaha olusturmuyor zaten o yuzden bu buraya bırakablirz

    app.run(debug = True)


