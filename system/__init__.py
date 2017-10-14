from flask import Flask
from flask_script import Server
from flask_sqlalchemy import SQLAlchemy
import sys , json
from datetime import datetime

app = Flask(__name__)

try:
	with open('config.json') as data:
		data_json = json.loads(data.read())
		db_host = data_json['db']['db_host']
		db_user = data_json['db']['db_user']
		db_pass = data_json['db']['db_pass']
		db_name = data_json['db']['db_name']
		host = data_json['host']
		port = data_json['port']
		debug = data_json['debug']
		secret = data_json['secret']
		
except Exception as err:
	print err	

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://%s:%s@%s/%s' % (db_user,db_pass,db_host,db_name)
db = SQLAlchemy(app)

running = Server(host=host,port=port,use_debugger=debug,use_reloader=True)
import manager

