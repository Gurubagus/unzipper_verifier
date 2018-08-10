import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
name = ''
kbsize = 0

def send_email():
    
	global name
	global ksize
    
	msg = MIMEMultipart()
	
	# create message object instance
	message = "%s has failed size verification." % name

	# setup the parameters of the message
	msg['From'] = "donotreply@benemen.com"
	username = "d5b31c0427bf3c"
	password = "b4ffb995bb08e2"
	#msg['From'] = "zachary.mark.taylor@gmail.com"
	msg['To'] = "zachary.taylor@benemen.com"
	msg['Subject'] = """
	Unzipper file verification failed. File is registering %s KB
	""" % kbsize
    
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
    
	# create server
	server = smtplib.SMTP('smtp.mailtrap.io: 2525')
	#server = smtplib.SMTP('smtp.gmail.com: 587')
	server.starttls()
    
	#Login Credentials for sending the mail
	server.login(username, password)
    
	# send the message via the server
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()
	print('email successfully sent')

def main(self):

	global name
	global kbsize
    
	#lists stats of incoming file
	statinfo = os.stat(self)
	size = statinfo.st_size
	kbsize = size/1000
	name = self
    
	if size < 200000:
		send_email()
	else:
		print 'its big'