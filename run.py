from flask import Flask, render_template
from flask import Markup

app = Flask(__name__)

# global variables

def html(x):
  return x


menu = [
  {"home" : "Home"}
]

@app.route("/")
def homepage():
  """The main page"""
  title = "Quinta C E - Home Page"
  image1 = "https://cdn.glitch.com/8c2f7a3d-e74c-4f36-8d5e-089c50dcc752%2FIS_tech_class_group.jpg?v=1568692442522"
  posts = [
    
    {"title" : "News",
      "body" : "Iniziamo ripassando alcuni concetti fondamentali sul bilancio.",
      "img" : ""
    },

 
] # end of posts
  for post in posts:
    for k in post:
      post[k] = Markup(post[k])
  showinfo = 1
  
  return render_template("index.html",
                         menu = menu,
                         title=title,
                         image1=image1,
                         posts=posts,
                         showinfo=showinfo)

#================================================ BILANCIO ================================
# =========================================================================================

@app.route("/bilancio")
def bilancio():
  """The main page"""
  title = "Quinta C E - Il Bilancio"
  image1 = "https://www.informazionefiscale.it/IMG/arton26.jpg"
  posts = [
    
    # introduzione
    
    {"title" : "Il Bilancio",
      "body" : 
        """
Il bilancio e' formato da tre documenti: Stato patrimoniale, Conto economico e Nota integrativa.
I primi due documenti sono di natura contabile, il terzo e' di natura descrittiva.
<img src='https://imgur.com/OWfR594.png'>"""},
    
    
    
# lo Stato patrimoniale
    
    {
      "title" : "Lo Stato patrimoniale",
      "body" : """

E' un prospetto che rappresenta il patrimonio dell'azienda.
I beni facenti parte dell'attivo patrimoniale si trovano nella sezione sinistra.
I debiti ed il Patrimonio netto si trovano nella sezione destra.

<img src='https://imgur.com/mBFDBoB.png' />"""},
    
    
    # ATTIVO
    
    {
      "title": "Attivo",
      "body" : "L'attivo si divide in due parti: l'attivo fisso e l'attivo circolante."
    },
    
    
    # Attivo Fisso
    
    {
      "title": "Attivo fisso",
      "body" : 
               """L'attivo fisso e' costituito da tutti i beni immateriali, materiali e finanziari che resteranno nell'azienda per piu' anni.
               Questi beni sono classificati in tre raggruppamenti:
              Immobilizzazioni immateriali: brevetti, software, costi d'impianto ecc.
               Immobilizzazioni materiali: Fabbricati, arredi, attrezzature, automezzi, computer ecc.
               Immobilizzazioni finanziarie: titoli finanziari (azioni, obbligazioni) 
che l'azienda ha acquistato per controllare altre aziende e non a scopo speculativo, oppure 
per investire liquidita' in eccesso a lungo termine."""
    },
    
    
    # Attivo circolante
    
        {"title": "Attivo circolante",
    "body" : 
            """L'attivo circolante e' costituito da tutte le attivita' 
            che sono in forma monetaria (Denaro in cassa o Disponibita' in banca) o che ritorneranno in tale forma entro un anno al massimo (crediti e merci).
            Questi beni sono classificati in tre raggruppamenti:
            Magazzino
            Liquidita' differite (crediti a breve termine: crediti v/clienti)
            Liquidita' immediate (Denaro in cassa e Banca c/c)

            <img src='https://static.docsity.com/documents_pages/2017/10/26/a6ef3a3d3bab5755499e594f4bea0669.png' width='100%'/>
            """,
},
    

    {
      "title" : "Passivita'",
      "body": ""
      
    },
    
    {
      "title" : "Es.1 La Situazione patrimoniale",
      "body" : 
"""
      La situazione patrimoniale presenta lo stesso contenuto dello Stato patrimoniale,
ma viene redatto nel corso dell'anno, mentre lo Stato patrimoniale viene redatto dopo la fine dell'anno 
e fa parte del Bilancio. Serve a monitorare la situazione dell'azienda.
<br><br>
<b>Esercizio</b>:
<br>
Presenta la situazione patrimoniale in base ai seguenti dati:
<br>
I soci dell'azienda hanno conferito 300.000 euro sul conto corrente dell'azienda.
<br>
Altri 100.000 euro sono stati ottenuti con un mutuo dalla stessa banca.
<br>
La nostra azienda ha acquistato attraverso il conto corrente bancario:
Impianti (300.000 euro), automezzi per 100.000 euro, 
attrezzature per 40.000 euro,
merci in magazzino per 20.000 euro.
<br>
Le attrezzature e le merci in magazzino sono state acquistate concordando una dilazione di pagamento con i fornitori.
La banca ha concesso un ulteriore prestito a breve termine di 10.000 euro per le spese correnti con un apertura di credito in c/c.
5.000 euro vengono prelevati dal conto corrente e depositati nella cassa dell'azienda.
<br>
Rappresenta la situazione patrimoniale distinguendo tra immobilizzazioni, attivo circolante, passivita' e Patrimonio netto.
<br>
<b>Rispondi alle seguenti domande:</b>
<br>
<ul>
<li>Cos'e' il bilancio?
<li>Cosa rappresentiamo nello Stato patrimoniale?
<li>Quando si presenta il bilancio?
                """,
    }
    
 
] # end of posts

  for post in posts:
    for k in post:
      post[k] = Markup(post[k])
  
  
  showinfo = 1
  return render_template("page.html",
                         menu = menu,
                         title=title,
                         posts=posts,
                         showinfo=showinfo)


# ================================================ INFO =================================
# =======================================================================================

@app.route("/info")
def info():
  """The info about myself page"""
  showinfo = 0
  title = "Info page"
  posts = [
  { 
    "title" : "Info about me",
    "body" : 
    "This is a blog for the 5ce students."
    
      }
    
  ]

  return render_template("info.html",
                         menu=menu,
                         title = title,
                         posts=posts,
                         showinfo=showinfo)

if __name__ == "__main__":
  app.run()