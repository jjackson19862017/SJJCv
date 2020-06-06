import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	""" Access langKnowledge json file """
	langKnow = []
	with open("data/langKnowledge.json", "r") as json_data:
		langKnow = json.load(json_data)
	return render_template("index.html", page_title="Profile", langKnow=langKnow)

@app.route('/experience')
def experience():
	return render_template("experience.html", page_title="Work Experience")

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
	""" Access Further education json file """
	furtEduc = []
	with open("data/further.json", "r") as json_data:
		furtEduc = json.load(json_data)
	return render_template("education.html", page_title="Education", educ=educ, furtEduc=furtEduc)

@app.route('/skills')
def skills():
	return render_template("skills.html", page_title="Work Experience")

@app.route('/interests')
def interests():
	return render_template("interests.html", page_title="Work Experience")

@app.route('/awards')
def awards():
	return render_template("awards.html", page_title="Work Experience")



if __name__ == '__main__':
	app.run(host=os.environ.get('IP'),
					port=os.environ.get('PORT'),
					debug=True)