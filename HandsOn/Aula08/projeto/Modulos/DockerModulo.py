from docker import Client

#cli = Client(base_url="tcp://192.168.0.2:2376")
cli = Client(base_url='tcp://192.168.0.2:2376', version='auto')


class DockerModulo:
	def __init__(self):
		try:
			self.cli= Client(base_url='tcp://192.168.0.2:2376', version='auto')
		except Exception as e:
			raise Exception (e)


	

	def createContainer(self, nome):
		try:
			container = self.cli.create_container(
				name=nome, image="ubuntu",
				detach=True, stdin_open=True, tty=True, command="/bin/bash"
				)
			
			return container
		except Exception as e:
			raise Exception(e)


	def startContainer(self,container):
		return self.cli.start(container=container.get('Id'))

	
	

