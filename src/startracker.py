from flask import Flask, render_template
from flask.helpers import url_for
from src.status.ask_status import ASKStatus
from src.status.adapter_ask_status import AdapterASKStatus
from src.status.indexer_status import IndexerStatus
from src.status.adapter_Indexer_status import AdapterIndexerStatus
from src.status.rancher_status import RancherStatus
from src.status.adapter_rancher_status import AdapterRanchertatus
from src.status.dlg_status import DLGStatus
from src.status.adapter_dlg_status import AdapterDLGStatus
from src.handlers.act_mail_gmail import ActMailGmail


app = Flask(__name__)

@app.route("/startracker/check/ask", methods=['GET'])
def render_ask_status():
    try:
        my_status_data = AdapterASKStatus(ASKStatus()).get_status()
        return render_template('index.html', obj=my_status_data, name='ASK')
    except Exception as err:
        return str(err), 400

@app.route("/startracker/check/indexer", methods=['GET'])
def render_indexer_status():
    try:
        my_status_data = AdapterIndexerStatus(IndexerStatus()).get_status()
        return render_template('index.html', obj=my_status_data, name='Indexer')
    except Exception as err:
        return str(err), 400

@app.route("/startracker/check/rancher", methods=['GET'])
def render_rancher_status():
    try:
        my_status_data = AdapterRanchertatus(RancherStatus()).get_status()
        return render_template('index.html', obj=my_status_data, name='Rancher')
    except Exception as err:
        return str(err), 400

@app.route("/startracker/check/dlg", methods=['GET'])
def render_dlg_status():
    try:
        my_status_data = AdapterDLGStatus(DLGStatus()).get_status()
        return render_template('index.html', obj=my_status_data, name='DLG')
    except Exception as err:
        return str(err), 400

@app.route("/startracker/check/email", methods=['GET'])
def send_email_status():
    try:
        my_status_data = AdapterDLGStatus(DLGStatus()).get_status()
        my_gmail_email = ActMailGmail(my_status_data)
        my_gmail_email.crate_email_message()
        my_gmail_email.act()
        return 'Email sent successfully'
    except Exception as err:
        return str(err), 400

# set FLASK_APP=C:\Users\eyal999\PycharmProjects\startracker\src\startracker.py
# $env:FLASK_APP = "C:\Users\eyal999\PycharmProjects\startracker\src\startracker.py"
# set FLASK_ENV=development
# set FLASK_DEBUG=True
# C:\Users\eyal999\AppData\Local\Programs\Python\Python311\python.exe -m flask --debug run

# install packages -> C:\Users\eyal999\AppData\Local\Programs\Python\Python311\Scripts
# run commands -> C:\Users\eyal999\PycharmProjects\startracker