from flask import Flask, render_template
from flask import Markup
import re

app = Flask(__name__)


# global variables


menu = [
  {"home" : "Home"}
]

def markup(posts):
  # bold instead of asteriscs
  for p in posts:
    # print(p)
    for k in p:
      p[k] = p[k].split(" ")
      print(p[k])
      for n,w in enumerate(p[k]):
        if "*" in w:
          w = w.replace("*","")
          p[k][n] = "<b>"+w+"</b>"
      p[k] = " ".join(p[k])
  
  # Markup everything
  for post in posts:
    for k in post:
      post[k] = Markup(post[k])

  
      
@app.route("/")
def homepage():
  """The main page"""
  
  title = "PIL Python Image Library"
  
  subtitle = "Elaborate image with Python"
  
  posts = [
    
    {"title" : "What is PIL",
      "body" :  """*PIL is a powerful module for *Python that allows you to create and elaborate *images by conding in Python. You can do almost anything, building the perfect image tools for your needs.
We will take a fast look at the main functions of this very useful module."""},
    
    {"title" : "Install",
    "body" : """First you need to install pil's fork pillow:
pip install pillow"""},
 
    {"title" : "Import",
    "body" : """from PIL import Image"""},
    
    {"title" : "Create",
    "body" : """img = Image.new('RBG', (600,400), 'yellow')"""},
    
    {"title" : "Open",
     "body" : """img = Image.open('existing.png')"""},
    
    {"title" : "Save",
     "body" : """img.save('myimage.png')"""},
    
    {"title" : "Show",
     "body" : """img.show()"""},
    
    {"title" : "Resize",
     "body" : """img.resize((100,100), Image.ANTIALIAS)"""},
    
    {"title" : "Blur (from PIL import ImageFilter)",
     "body" : """img.filter(ImageFilter.BLUR)"""},
    
    {"title": "A smooth blur",
    "body" : 
      """This is much softer than BLUR
i = i.""filter(ImageFilter.SMOOTH)"""
    },
  
    {"title" : "Blend 2 images together",
     "body" : """img = Image.blend(Image.open('image1.png','image2.png', 0.5))"""},
    
    {"title" : "Pasting an image on another",
     "body" : """img.paste((0,0),'image2.png')"""},
    
    {"title" : "Write text on an image (ImageDraw)",
     "body" : """draw = ImageDraw.Draw(img)
               draw.text(0,0,'This text goes on top of the image')"""},
    
    {
      
      "title" : "Thumbnail",
      "body" : """im.thumbnail((128, 128), Image.ANTIALIAS)"""
      
    }
    

    # {"title" : "", "body" : ""},
    

  ]

  
  for p in posts:
    # print(p)
    for k in p:
      p[k] = p[k].split(" ")
      print(p[k])
      for n,w in enumerate(p[k]):
        if "*" in w:
          w = w.replace("*","")
          p[k][n] = "<b>"+w+"</b>"
      p[k] = " ".join(p[k])      
    
  
  markup(posts) # substitute * and add Markup
  
  showinfo = 1
  return render_template("index.html",
                         menu = menu,
                         title = title,
                         subtitle = subtitle,
                         posts = posts,
                         showinfo = showinfo)

@app.route("/info")
def info():
  """The info about myself page"""
  showinfo = 0
  title = "Info page"
  posts = [
  { 
    "title" : "Info about me",
    "body" : 
    "Welcome in our school!",
  }
    
  ]

  return render_template("info.html",
                         menu=menu,
                         title = title,
                         posts=posts,
                         showinfo=showinfo)

if __name__ == "__main__":
  app.run()