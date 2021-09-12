import json

def extract_route(requisicao):
    if requisicao.startswith('GET'):
        lista1 = requisicao.split("GET /")
    else:
        lista1 = requisicao.split("POST /")

    lista2 = lista1[1].split(" ")
    return lista2[0]
    
def read_file(path):
    lista = str(path).split(".")
    if lista[-1] == 'txt' or lista[-1] == 'html' or lista[-1] == 'css' or lista[-1] == 'js':
        with open(path,"rt") as file:
           text = file.read() 
           return text
    else:
        with open(path,'rb') as file:
            binary = file.read()
            return binary

def load_data(nomeJson):
   filepath =  "data/" +nomeJson
   with open(filepath,"rt",encoding="utf-8") as text:
       content = text.read()
       contentPython = json.loads(content)
       return contentPython

def load_template(filepath):
    file = open("templates/"+filepath)
    content = file.read()
    file.close()
    return content

def addlist(params):
    filename = 'data/notes.json'
    entry ={
    "titulo": params['titulo'],
    "detalhes": params['detalhes']
  }
    with open(filename, "r") as file:
        data = json.load(file)
    data.append(entry)
    with open(filename, "w") as file:
        json.dump(data, file)

def build_response(body,code,reason,headers):
    return('x')