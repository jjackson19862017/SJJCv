import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	
	return render_template("index.html", page_title="Profile")

@app.route('/experience')
def experience():
	""" Access Work Experience json file """
	workExp = []
	with open("data/workExp.json", "r") as json_data:
		workExp = json.load(json_data)
	return render_template("experience.html", page_title="Work Experience", workExp=workExp)

@app.route('/projects')
def projects():
	""" Access piProjects json file """
	piProjects = []
	with open("data/piProjects.json", "r") as json_data:
		piProjects = json.load(json_data)
	""" Access program project json file """
	programs = []
	with open("data/programs.json", "r") as json_data:
		programs = json.load(json_data)
	return render_template("projects.html", page_title="Projects", piProjects=piProjects, programs=programs)

@app.route('/education')
def education():
	""" Access education json file """
	educ = []
	with open("data/education.json", "r") as json_data:
		educ = json.load(json_data)
	
	
	return render_template("education.html", page_title="Education", educ=educ)

@app.route('/skills')
def skills():
	return render_template("skills.html", page_title="Skills")

@app.route('/interests')
def interests():
	""" Access interests json file """
	data = []
	with open("data/interests.json", "r") as json_data:
		data = json.load(json_data)
	return render_template("interests.html", page_title="Interests", interests=data)

@app.route('/awards')
def awards():
	""" Access Further education json file """
	furtEduc = []
	with open("data/further.json", "r") as json_data:
		furtEduc = json.load(json_data)
	return render_template("awards.html", page_title="Work Experience", furtEduc=furtEduc)



if __name__ == '__main__':
	app.run(host=os.environ.get('IP'),
					port=os.environ.get('PORT'),
					debug=True)