from flask import Flask, render_template

app = Flask(__name__)

# global variables


menu = [
  {"home" : "Home"}
]

@app.route("/")
def homepage():
  """The main page"""
  title = "Quinta"
  image1 = "https://cdn.glitch.com/8c2f7a3d-e74c-4f36-8d5e-089c50dcc752%2FIS_tech_class_group.jpg?v=1568692442522"
  posts = [
    
    {"title" : "Il Bilancio",
      "body" : "Il bilancio e' formato da tre documenti: Stato patrimoniale, Conto economico e Nota integrativa."},
    

  ]
  showinfo = 1
  return render_template("index.html",
                         menu = menu,
                         title=title,
                         image1=image1,
                         posts=posts,
                         showinfo=showinfo)

@app.route("/info")
def info():
  """The info about myself page"""
  showinfo = 0
  title = "Info page"
  posts = [
  { 
    "title" : "Info about me",
    "body" : 
    "This is a blog for the 5ce students.",
  }
    
  ]

  return render_template("info.html",
                         menu=menu,
                         title = title,
                         posts=posts,
                         showinfo=showinfo)

if __name__ == "__main__":
  app.run()