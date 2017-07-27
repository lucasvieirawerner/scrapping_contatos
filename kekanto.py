from bs4 import BeautifulSoup
import requests
import unidecode
import openpyxl

def getrestaurantes( pagina ):
   pagina = str(pagina)
   empresa = "https://kekanto.com.br/pr/curitiba/restaurantes/36/page:" + pagina + "?ajax=1"
   page = requests.get(empresa)
   soup = BeautifulSoup(page.content, 'html.parser')
   nomes = []
   for x in range(0,20):
      nome = soup.find_all("a", class_="color-555")[x].text
      nome = unidecode.unidecode(nome)
      nome = nome.replace("\n", "")
      nome = nome.replace(" ", "+")
      nomes.append(nome)
   return nomes

def getemail( vetor_restaurantes):
   vetor_email = []
   for x in range(0,20):
      email = "https://www.google.com.br/search?q="+vetor_restaurantes[x]+"&oq="+vetor_restaurantes[x]+"&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8"
      page = requests.get(email)
      soup = BeautifulSoup(page.content, 'html.parser')
      email = soup.find("h3", class_="r")
      if not email:
         vetor_email.append("")
      if email:
         email = unidecode.unidecode(email)
         if not email:
            vetor_email.append("")
         if email:
            stre = email.split('www.', 1000000)
            try:
               strd = stre[1].split('/', 1000000)
            except:
               vetor_email.append("")
            try:
               email = "contato@" + strd[0]
            except:
               vetor_email.append("")
            vetor_email.append(email)
   return vetor_email


for x in range(14, 234):
   vetor_restaurantes = getrestaurantes(x)
   vetor_email = getemail(vetor_restaurantes)
   print vetor_email