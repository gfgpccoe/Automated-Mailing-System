from Google import Create_Service
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def create_draft( html, to, subject ):		
	CLIENT_SECRET_FILE='credentials.json'
	API_NAME='gmail'
	API_VERSION='v1'
	SCOPES=['https://mail.google.com/']

	service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
	mimemsg= MIMEMultipart()
	mimemsg['to']=to
	mimemsg['subject']=subject

	part2 = MIMEText(html, 'html')
	mimemsg.attach(part2)
	raw_string=base64.urlsafe_b64encode(mimemsg.as_bytes()).decode()

	service.users().drafts().create(
		userId='me',
		body={'message':{'raw':raw_string}}
	).execute()