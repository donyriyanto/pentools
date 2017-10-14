from flask_script import Manager, Command, Option
import sys, os
from termcolor import colored

class Create(Command):
	
	help_args = ('-h', '--help')
	help = "Create Module"
	option_list = (
        Option('--name', '-n', dest='name'),
    )
	def create_folder(self,name):
		directory = 'modules/'+name
		if not os.path.exists(directory):
			os.makedirs(directory)
		if not os.path.exists(directory+'/views'):
			os.makedirs(directory+'/views')
		if not os.path.exists(directory+'/controller'):
			os.makedirs(directory+'/controller')
		if not os.path.exists(directory+'/model'):
			os.makedirs(directory+'/model')

		try:
			with open(directory+'/__init__.py','w') as f:
				f.write(' ')
				f.close()
		except Exception as err:
			print err

		print "Pentools ==> "+directory+" ::::>> Created"
		print "Pentools ==> "+directory+"/views ::::>> Created"
		print "Pentools ==> "+directory+"/controller ::::>> Created"
		print "Pentools ==> "+directory+"/model ::::>> Created"
		print "Pentools ==> ", colored("modules/"+name+"/model/__init__.py","red")
		print colored("		edit this model file before run init_db","red")
		print "Pentools ==> run 'python manage.py init_db' for create model table"
		return directory
	def create_template(self, name):
		try:
			with open('modules/'+name+'/views/index.html','w') as f:
				f.write('/'+name)
				f.close()
		except Exception as err:
			print err

	def add_to_route(self,name):
		try:
			with open('modules/router.py','r') as f:
				f.seek(0)
				data = f.readlines()
				a = len(data) - 1
				f.close()
				add_module = "\n\nfrom "+name+".controller import "+name+"\n"
				register_module = "app.register_blueprint("+name+")\n"
				d = open('modules/router.py','w')
				data.insert(6,add_module)
				data.insert(7,register_module)
				d.writelines(data)
				d.close()
		except Exception as err:
			print err

		self.create_template(name)

	def create_model(self, name):
		try:
			with open('modules/'+name+'/model/__init__.py', 'w') as f:
				f.write("from datetime import datetime\n")
				f.write("from system import db\n\n")
				f.write("class "+name.title()+"(db.Model):\n")
				f.write("	id = db.Column(db.Integer, primary_key=True)\n")
				f.write("	username = db.Column(db.String(80), unique=True, nullable=False)\n")
				f.write("	email = db.Column(db.String(120), unique=True, nullable=False)\n")
				f.write("	password = db.Column(db.String(255), nullable=False)\n")
				f.write("	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)\n\n")
				f.write("	def __repr__(self):\n")
				f.write("		return '<"+name.title()+" %r>' % self.username\n\n\n")
				f.write("# for usage please visit http://flask-sqlalchemy.pocoo.org/2.3/quickstart/#a-minimal-application")
				f.close()
		except Exception as err:
			print err

	def create_controller(self,name):
		directory = self.create_folder(name)
		self.add_to_route(name)
		self.create_model(name)
		try:
			with open(directory+'/controller/__init__.py', 'w') as f:
				f.write("from system.library import * \n")
				f.write("from system import db\n")
				f.write("from modules."+name+".model import "+name.title()+"\n\n")
				f.write(name+" = Blueprint('"+name+"', __name__, \n")
				f.write("				template_folder='"+directory+"' , url_prefix='/"+name+"')\n")
				f.write("@"+name+".route('/', defaults={'page': 'index'})\n")
				f.write("@"+name+".route('/<page>') \n")
				f.write("def show(page): \n")
				f.write("	try: \n")
				f.write("		return render_template('"+name+"/views/%s.html' % page) \n")
				f.write("	except TemplateNotFound: \n")
				f.write("		abort(404)\n\n")
				f.write("@users.route('/create_user',methods=['POST'])\n")
				f.write("def create_user():\n")
				f.write("	try:\n")
				f.write("		data = request.get_json()\n")
				f.write("		username = data['username']\n")
				f.write("		password = data['password']\n")
				f.write("		email = data['email']\n")
				f.write("		insert_data = "+name.title()+"(username=username,password=password,email=email)\n")
				f.write("		db.session.add(insert_data)\n")
				f.write("		db.session.commit()\n")
				f.write("		return response(data=data,code=201,message='Create new users success')\n")
				f.write("	except Exception as e:\n")
				f.write("		return e\n\n")
				f.write("@users.route('/get_user',methods=['GET'])\n")
				f.write("def get_user():\n")
				f.write("	select = "+name.title()+".query.all()\n")
				f.write("	data = []\n")
				f.write("	for d in select:\n")
				f.write("		result= {\n")
				f.write("			'id':d.id,\n")
				f.write("			'username':d.username,\n")
				f.write("			'password':d.password,\n")
				f.write("			'email':d.email\n")
				f.write("		}\n")
				f.write("		data.append(result)\n")
				f.write("	return response(data=data,code=200,message='Success get user data')\n\n")
				f.write("@users.route('/update_user',methods=['POST'])\n")
				f.write("def update_user():\n")
				f.write("	try:\n")
				f.write("		data = request.get_json()\n")
				f.write("		update = "+name.title()+".query.filter_by(id=data['id']).update(data)\n")
				f.write("		db.session.commit()\n")
				f.write("		return response(data=data,code=200,message='Succesfuly update')\n")
				f.write("	except Exception as e:\n")
				f.write("		return e\n")
				f.close()
		except Exception as err:
			print err

	def run(self, name):
		self.create_controller(name)
			
	