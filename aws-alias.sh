alias aws-get-g3='export instanceId=`aws ec2 describe-instances --filters "Name=instance-state-name,Values=stopped,Name=instance-type,Values=g3s.xlarge" --query "Reservation[0].InstanceId"` && echo $instanceId'
alias aws-start='aws ec2 start-instances --instance-ids $instanceId && aws ec2 wait instance-running --instance-ids $instanceId && export instanceIp=`aws ec2 describe-instances --filters "Name=instance-id,Values=$instanceId" --query "Reservation[0].Instances[0].PublicIpAddress" && echo $instanceIp'
alias aws-ip='export instanceIp=`aws ec2 describe-instances --filters "Name=instance-id,Values=$instanceId" --query "Reservation[0].Instances[0].PublicIpAddress"` && echo $instanceIp'
alias aws-ssh='ssh -i /cygdrive/d/key/KirubelAWS.pem ubuntu@instanceid' 
alias aws-stop='aws ec2 stop-instances --instance-ids $instanceId'
alias aws-state='aws ec2 describe-instance --instance-ids $instanceId --query "reservations[0].Instances[0].State.Name"'

if [[ `uname` == *"CYGWIN"* ]]
then
	# This is cygwin. use cygstart to open the notebook
	alias aws-nb='cygstart http://$instanceIp:8888'
fi

if [[ `uname` == *"Linux"* ]]
then 
	# This is linux. Use xdg-open to open the notebook
	alias aws-nb='xdg-open http://$instanceIp:8888'
fi

if [[ `uname` == *"Darwin"* ]]
then
	# This is Mac. Use open to open the notebook
	alias aws-nb='open http://$instanceIp:8888'
fi
