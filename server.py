from pydoc import render_doc
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/users")
def users():
    userList = [
   {'first_name' : 'Michael', 'last_name' : 'Choi','age': 35},
   {'first_name' : 'John', 'last_name' : 'Supsupin','age':45},
   {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age': 2},
   {'first_name' : 'KB', 'last_name' : 'Tonel','age':9000}
]
    return render_template("index.html", userList=userList)



if __name__ == "__main__":
    app.run(debug=True)

