import sys
import os
from datetime import datetime
import zope.interface
import smtplib, ssl
from flask import render_template
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
from email.mime.application import MIMEApplication

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.config.settings import Settings
from src.handlers.interface_act_handler import IActHandler

#from config.settings import Settings
#from handlers.interface_act_handler import IActHandler
#from status.dlg_status import DLGStatus
#from status.adapter_dlg_status import AdapterDLGStatus

@zope.interface.implementer(IActHandler)
class ActMailGmail:  # type: ignore

    def __init__(self, my_data) -> None:
        self.email_from = Settings.email_gmail_from
        self.email_wonder = Settings.email_gmail_wonder
        self.email_to = Settings.email_gmail_to
        self.context = None
        self.email_string = None
        self.email_data = my_data

    # Define a function to attach files as MIMEApplication to the email
        ## Add another input extra_headers default to None
    ##############################################################
    def attach_file_to_email(self, email_message, filename, extra_headers=None):
        # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
        with open(filename, "rb") as f:
            file_attachment = MIMEApplication(f.read())
        # Add header/name to the attachments
        file_attachment.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        # Set up the input extra_headers for img
        ## Default is None: since for regular file attachments, it's not needed
        ## When given a value: the following code will run
            ### Used to set the cid for image
        if extra_headers is not None:
            for name, value in extra_headers.items():
                file_attachment.add_header(name, value)
        # Attach the file to the message
        email_message.attach(file_attachment)

    def crate_email_message(self):
        now = datetime.now() # current date and time
        # Create a MIMEMultipart class, and set up the From, To, Subject fields
        email_message = MIMEMultipart()
        email_message['From'] = self.email_from
        email_message['To'] = self.email_to
        email_message['Subject'] = f'Report email - {now.strftime("%m/%d/%Y, %H:%M:%S")}'

        ##############################################################
        html = render_template('index.html', obj=self.email_data, name='DLG Status')
        ##############################################################

        # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
        email_message.attach(MIMEText(html, "html"))

        # Attach more (documents)
        ## Apply function with extra_header on chart.png. This will render chart.png in the html content
        ##############################################################
        self.attach_file_to_email(email_message, 'src\static\images\mdclone-logo.png', {'Content-ID': '<myimageid>'})
        ##############################################################

        # Convert it as a string
        self.email_string = email_message.as_string()
        self.context = ssl.create_default_context()

    def act(self):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
            server.login(self.email_from, self.email_wonder)
            server.sendmail(self.email_from, self.email_to, self.email_string)  # type: ignore


if __name__ == '__main__':
    pass
    #my_status_data = AdapterDLGStatus(DLGStatus()).get_status()
    #my_email = ActMailGmail(my_status_data)
    #my_email.crate_email_message()
    #my_email.act()