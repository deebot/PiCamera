import os
firstName= " Deepankar"
lastName= " Maithani"
email= " deepankar19910@gmail.com"
def index():
	temp_conf_file = open('recepientData.txt.tmp', 'a')
	temp_conf_file.write('firstName="' + firstName + '"\n')
	temp_conf_file.write('lastName="' + lastName + '"\n')
	temp_conf_file.write('email="' + email + '"\n')
	temp_conf_file.write('Newuser\n')
	os.system('mv recepientData.txt.tmp /home/pi/recepientData.txt')
index()