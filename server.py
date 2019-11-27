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
  
  title = "Appunti di Economia aziendale"
  
  subtitle = "Appunti quotidiani"
  
  posts = [
    
    

    {"title" : "Ruolo dell'Italia nel turismo (classe 5a)",
     "body" : "Assodato il fatto che il turismo alimenta il 10% del PIL, che risente meno della crisi rispetto ad altri settori dell'economia di un Paese e che l'Italia è al quinto posto per arrivi internazionali, bisogna capire che per intercettare i turisti anche in futuro si devono comprendere le nuove tendenze quali il progressivo invecchiamento della papolazione, i nuovi stili di vita (lavoro più flessibile, periodi di vacanza più brevi e distribuiti nel tempo, ricera di esperienze diverse da quelle del turismo di massa, bisogno di conoscere nuove culture. Una parte dei turisti utilizza Internet ed è più indipendente nella composizione della propria vacanza. Le nuove tecnologie pongono nuove sfide, così come l'aumentare del reddito dei Paesi in via di sviluppo). La Russia, l'India, la Cina, sono aree che rappresenteranno una fetta sempre maggiore del mercato turistico italiano (e mondiale). L'offerta, quindi, deve adeguarsi ai cambiamenti della domanda."},
    {
      "title" : "Analisi SWOT",
      "body" : "Un metodo per analizzare le opportunità del mercato è l'analisi SWOT che analizza i punti di forza e debolezza della sua stessa organizzazione e le opportunità e le minacce derivanti dal mercato e dalle scelte politiche. Per questo le informazioni (abbiamo parlato degli enti che forniscono dati statistici sul turismo) sono fondamentali per orientare la gestione di un'impresa. La sigla SWOT, in inglese, sta per Strengths (punti di forza), weaknesses (debolezze), opportunities e threats (minacce)."
    },
    
    {"title": "Flussi turistici",
     "body" : "Negli ultimi anni c'è stato un forte aumento di turisti russi, indiani, brasiliani e cinesi, in quanto in questi Paesi il reddito pro capite è aumentato fortemente. È importante anche il turismo di prossimità, proveniente dalla Francia, dalla Svizzera e dall'Austria, perché questi turisti possono raggiungere il nostro Paese facilmente e con diversi mezzi (auto, treno, aereo). Il turismo in Italia, dati del 2019, è in equilibrio tra presenze dei residenti (48%) e non residenti (52%)."
      
    },
    
    {
      "title": "Motivazioni del viaggio",
      "body": "Per le vacanze in Italia, le motivazioni principali sono la bellezza del paesaggio, la possibilità di rilassarsi, i fattori relazionali (ritrovarsi tra amici e parenti), la visita al Papa. Per gli italiani che si recano all'estero è fondamentale conoscere posti nuovi, ammirare il patrimonio artistico della destinazione, divertirsi. Meno importanti sono le motivazioni legate alla natura o alla cucina (essendo l'Italia il Paese con la maggiore tradizione enogastronomica, gli italiani non si adattano all'enogastronomia di altri Paesi facilmente). Il prezzo è sicuramente una delle motivazioni principali."
      
    },
    
    {
      "title": "Turismo in Italia 2019",
      "body" : "<a href='https://www.corriere.it/cronache/19_agosto_18/03-interni-sopcorriere-web-sezioni-21e68bd8-c1f5-11e9-b61c-c8d9a9699826.shtml'><img src='https://www.corriere.it/methode_image/2019/08/19/Interni/Foto%20Interni%20-%20Trattate/turismo%20grafico-k03B-U31301899356699KJF-656x492@Corriere-Web-Sezioni.JPG'></a>"
      
    },
    
    {
      "title": "Statistiche sulla Russia dell'Enit",
      "body" : """<a href='http://www.enit.it/en/studi/focus-paese/category/6-rapporti-enitmae-rapporti-enitmae-europa.html?download=2549:russia&start=20'>Link al file pdf</a><br>
<a href="https://www.giuliogargiullo.it/turisti-russi/">Articolo sulle statistiche sui turisti russi</a>"""
      
    }
    
    
    
    
    

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