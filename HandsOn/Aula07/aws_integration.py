import boto3




class AwsManager:
	def __init__(self):
		self.ec2 = boto3.resource("ec2")

	def getInstances(self):
		return self.ec2.instances.all()

	def getInstance(self,id):
		return self.ec2.instances.filter(InstanceIds=[id])


if __name__=='__main__':
	aws = AwsManager()

	for i in aws.getInstances():
		instance_id = i.instance_id

print aws.getInstance(instance_id).public_dns_name



#for i in ec2.instances.all():
#	print i.public_ip_address