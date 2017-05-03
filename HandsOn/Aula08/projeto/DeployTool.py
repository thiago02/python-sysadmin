from Modulos.DockerModulo import DockerModulo
from Modulos.SSHModulo import SSHModulo
import json

if __name__ =='__main__':
	try:
		with open ("deployment.json", 'r') as f:
			job_json = json.loads(f.read())
	
		Docker = DockerModulo()
		#container = Docker.createContainer(job_json['name'])
		#Docker.startContainer(container)

		ssh = SSHModulo()


		for c in job_json['commands']:
			command = "docker exec %s %s" % (job_json['name'], c)

			ssh.execCommand(c)
			



		print 'deploy finalizado com sucesso'

	except Exception as e:
		print e 

