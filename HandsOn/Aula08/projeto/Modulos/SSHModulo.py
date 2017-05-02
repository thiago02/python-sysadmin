from paramiko import SSHClient
import paramiko

Class SSHModulo
	def __init__(self):
	self.server = "192.168.0.2"
	self.client = SSHClient()
	self.client.load_system_host_keys()
	self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	self.client.connect(user='forlinux', self.server)

def execCommand(self, command):
	try:
		stdin, stdout, stderr = self.client.exec_command(command)
		if stderr.channel.recv_exit_status() !=0:
			raise Exception(stderr.read())

	except Exception as e:
		raise Exception(e)