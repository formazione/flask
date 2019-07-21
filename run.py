from flask import Flask, render_template

app = Flask(__name__)


# global variables


menu = [
  {"home" : "Home"}
]

@app.route("/")
def homepage():
  """The main page"""
  title = "A free Blog with Python, Flask and Glitch"
  posts = [
    
    {"title" : "Welcome to my Python blog/tutorial",
      "body" : "In this blog we will talk about basic stuffs about Python programming language."},
    
    {"title" : "start.sh",
    "body" : "This is the file that makes everything starts. It contains just this command: 'python run.py', where run.py is the second file you will create and it's the whole 'brain' of your site in Python."},
    
    {"title": "run.py",
    "body" : "This is the main file, responsible for the site's behaviour. Here you can put all the data you need to be shown in the site, while the other file will just be needed to show the data in the desired way."},
    
    {
      "title" : "Folder",
      "body" : "We have two folders: static that contains css files and templates that contains html pages"
    },
    
    {"title" : "Jinja",
    "body" : "This module allows you to use the data from run.py into the rendered html pages of the site. When you use render_template, you pass as argument, the name of the html page and the variables you can use in the code of the page itself, as we will soon explain."}
    

  ]
  showinfo = 1
  return render_template("index.html",
                         menu = menu,
                         title=title,
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
    "Hi. I'm Giovanni Python. Subscribe to my channel on Youtube if you want more tutorial like this.",
  }
    
  ]

  return render_template("info.html",
                         menu=menu,
                         title = title,
                         posts=posts,
                         showinfo=showinfo)

if __name__ == "__main__":
  app.run()