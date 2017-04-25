import requests 
import json 


token = "PuQePKrdyhzbdfQ5J--7"

url = "http://gitlab.dexter.com.br/api/v3"

def getUsers():
	global url,token
	return json.loads(requests.get("%s/users?private_token=%s" % (url, token)).content)

def createUser(name, user, pswd, email):
	global url, token
	data = {"name": name, "username": user, "password": pswd, "email": email}
	headers = {"Content_type": "application/json"}

	return json.loads(requests.post("%s/users?private_token=%s" %(url,token), data=data, headers=headers).content)

def getProjects():
	global url, token
	return json.loads(requests.get("%s/projects"))

def creatWebHook(project_id, hook_url):
	global url, token
	data = {"url": hook_url, "push_events": True}

	return json.loads(requests.post("%s/projects/%s/hooks?private_token=%s" %(url, project_id, token)))






#response = json.loads(requests.get("%s/users?private_token=%s" % (url, token)).content)


#print dict ([ (u['username'], u['email']) for u in response ]) #dicionario 
#print json.dumps ([ (u['username'], u['id']) for u in response ]) #Json 


# http://gitlab.dexter.com.br/api/v3/users?private_token=PuQePKrdyhzbdfQ5J--7 

#data = {"name": "Pelexx", "username": "pelezinho", 
#"password": "4linux123456", "email": "pelezinho@4linux.com.br"}

#response = requests.post("%s/users?private_token=%s" % (url, token), 
#	data=data, headers= {'Content_Type': 'application/json'})

#print response._content


