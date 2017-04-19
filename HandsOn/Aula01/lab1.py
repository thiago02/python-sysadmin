import requests
import json 

a = 'usuario ja existe'
nome = "Rafael medeiros"
email ="rafaelmedeiros@dexter.com.br"

url = "http://localhost:5000/usuarios/"
resultado = json.loads(requests.get(url).text)


for u in resultado['usuarios']:
	if u['email'] == email:
		print 'Usuario ja cadastrado'
		exit()

data = json.dumps({"nome": nome, "email": email}) 
headers = {"Content-Type": "application/json"}

print requests.post(url, data=data, headers=headers).text
	
