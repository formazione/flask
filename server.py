from flask import Flask, render_template
from flask import Markup
import re
from keyword import kwlist
app = Flask(__name__)


# global variables


menu = [
  {"home" : "Home"}
]


def highlight(code):
	"pass a string and it will be highlighted"
	
	# keywords to be colored in orange
	kw = kwlist
	for k in kw:
		k = k + " "
    
		code = code.replace(k, "<b style='color:orange'>" + k + "</b>")
	code = code.replace("\n","<br>")
	#print(code)

	# The 'indentation'
	code = code.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")

	# functions to be clored in blue
	_def= re.findall("\w+\(", code)
	for w in _def:
		code = code.replace(w, "<b style='color:blue'>" + w[:-1] + "</b>(")
	return code


def markup(posts):
  # bold instead of asteriscs
  for p in posts:
    # print(p)
    for k in p:
      p[k] = p[k].split(" ")
      print(p[k])
      for n,w in enumerate(p[k]):
        if "." in w:
          w = w.split(".")
          for nn,sub in enumerate(w):
            if "*" in sub:
              sub = sub.replace("*","")
              w[nn] = "<b>" + sub + "</b>"
            if "^" in sub:
              sub = sub.replace("^","")
              w[nn] = "<b style='color:blue'>" + sub + "</b>"
            if "#" in sub:
              sub = sub.replace("#","")
              w[nn] = "<b style='color:coral'>" + sub + "</b>"
          w = ".".join(w)
          p[k][n] = w
        elif "*" in w:
          w = w.replace("*","")
          p[k][n] = "<b>"+w+"</b>"
        elif "^" in w:
          w = w.replace("^","")
          p[k][n] = "<b style='color:blue'>"+w+"</b>"
        elif "#" in w:
          w = w.replace("#","")
          p[k][n] = "<b style='color:coral'>"+w+"</b>"
      p[k] = " ".join(p[k])
  
  # Markup everything
  for post in posts:
    testo = post["body"].splitlines()
    for line in testo:
      if line != "":
        if line[0] == ">":
          testo[testo.index(line)] = Markup(highlight(line))
    testo = "".join(testo)
    post["body"] = Markup(testo)
    #post["body"] = Markup(highlight(post["body"]))




      
@app.route("/")
def homepage():
  """The main page"""
  
  title = "PIL Python Image Library"
  
  subtitle = "Elaborate image with Python"
  
  posts = [
    
    {"title" : "What is PIL",
      "body" :  """*PIL is a powerful module for *Python that allows you to create and elaborate *images coding in Python. You can do almost anything, building the perfect image tools for your needs.
We will take a fast look at the main functions of this very useful module."""},
    
    {"title" : "Install",
    "body" : """First you need to install pil's fork pillow:
pip install pillow
<img src="https://cdn.glitch.com/8f79309f-0a88-41bb-bfd9-ccac7007a188%2Fpip_install_pil.PNG?v=1569514131173" />
"""},
 
    {"title" : "Import",
    "body" : """
    The first thing you need to import is the Class Image
    <br>
>>> from PIL import Image"""},
    
    # CREATE A NEW IMAGE
    
    {"title" : "Create",
    "body" : """>>> img = Image.new('RBG', (200,200), 'yellow')
<br><br>
This will *create a yellow square image of 200 px of *width and 200 px of *height. *RGB is for Red, Green and Blue, aka the image is in color. If you want to use *transparency you have to use *RGBA instead of RGB.
"""},
    
    {"title" : "Open",
     "body" : """>>> img = Image.open('existing.png')"""},
    
    {"title" : "Save",
     "body" : ">>> img.save('myimage.png')"},
    
    {"title" : "Show",
     "body" : ">>> img.show()"},
    
    {"title" : "Resize",
     "body" : """>>> img.resize((100,100), Image.ANTIALIAS)"""},
    
    {"title" : "Filters for the images",
     "body" : """
>>> img.filter(ImageFilter.BLUR)
<br><br>
There's a much smoother blur called SMOOTH
<br>
>>> i = i.filter(ImageFilter.SMOOTH )
<br><br>
You can then create a 'contour' effect
<br>
>>> i = i.filter( ImageFilter.CONTOUR )
"""},
    

  
    {"title" : "Blend 2 images together",
     "body" : """>>> img = Image.blend(Image.open('image1.png','image2.png', 0.5) )"""},
    
    {"title" : "Pasting an image on another",
     "body" : """>>> img.paste((0,0),'image2.png')"""},
    
    {"title" : "Write text on an image (ImageDraw)",
     "body" : """
>>> draw = ImageDraw.Draw(img)
<br>
>>> draw.text(0,0,'This text goes on top of the image')"""},
    
    {
      
      "title" : "Thumbnail",
      "body" : """>>> im.thumbnail((128, 128), Image.ANTIALIAS)"""
      
    },
    
    
    {
      "title" : "text and font",
      
      "body" : """
To add a *text to an *image after you created an image:
<br>
>>> im = img.new("RGBA", (600,400), "yellow")
<br>
You create a ^ImageDraw.Draw object to wich you pass the ^im object you created and on wich you draw:
<br>
>>> d = ImageDraw.Draw(im)
<br><br>
Now you are ready to add a text to the ^d object, but you can define the *size and *family of the text, using the ^ImageFont *class (that you need to import from PIL) together with the method ^truetype:
<br>
>>> font = ImageFont.truetype("Arial 20")
<br><br>
Now, you can finally add this font to the ^font ^argument when you add the text like this:
>>> d.text((10,10), "text to show", (255,255,255), font=font)
      """
      
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
    Markup("""I got the python blog <a href='https://pythonprogramming.altervista.org'>https://pythonprogramming.altervista.org</a>
    <br>
    <img src='https://i1.wp.com/pythonprogramming.altervista.org/wp-content/uploads/2019/06/cropped-altervista2.png?fit=156%2C55&ssl=1'
/>
<br>
I have also a <a href="https://www.youtube.com/channel/UCzbxq5e9gLiY-je2-br1rvg?view_as=subscriber">Youtube channel with hundreds of videos about Python</a> with a lot of examples and live coding videos.
"""),
  }
    
  ]

  return render_template("info.html",
                         menu=menu,
                         title = title,
                         posts=posts,
                         showinfo=showinfo)

if __name__ == "__main__":
  app.run()