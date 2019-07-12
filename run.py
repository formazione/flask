from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():  
  posts = [
    
    {
      "title" : "Welcome to my blog/tutorial",
      "body" : "This blog was born to give you the essential knowledge to create a blog with Flask in glitch.com. You can take a look at my video on my channel."
      
    },
    
    {"title": "1. How to use Python in Glitch",
    "body": "First you need an account on glitch.com, then you create a new project."
    },
    {"title": "2. Your first flask blog",
     "body": "First of all create a start.sh file with python run.py in it."
    },
    
    {
      "title": "3. The run.py file",
      "body": "In this  file you will import Flask and render_template from the module flask (that will be listed in the file requirement.txt (we will talk about it in the next post)). We will create an istance of Flask, named app. Then we will create the views. We will also launch the app.run() method to start the blog."
    }
  ]
  
  return render_template("index.html", posts=posts)

@app.route("/info")
def info():
  return """
  <h2>I'm Giovanni....</h2>
  <a href="/">Home</a>
  """

if __name__ == "__main__":
  app.run()