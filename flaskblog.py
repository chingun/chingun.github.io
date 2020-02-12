from flask import Flask, render_template, url_for
app = Flask(__name__)       #special variable that is just the name of the module __name__ is same as __main__


embedded_posts = [
	{
		'class': 'Embedded Systems',
		'subclass': 'Software',
		'link': 'https://www.eecs.umich.edu/courses/eecs473/labs.html',
		'link_about': 'Advanced Embedded Systems',
		'more_on_topic': ': University of Michigan. ',
		'date': 'December 2017',
	},
	{
		'class': 'Embedded Systems',
		'subclass': 'Tools',
		'link': 'http://www.kicad-pcb.org/',
		'link_about': 'KiCad PCB Design',
		'more_on_topic': ': free tool for designing PCBs',
		'date': 'December 2017',
	},
	{
		'class': 'Embedded Systems',
		'subclass': 'Libraries',
		'link': 'https://www.freertos.org/',
		'link_about': 'freeRTOS',
		'more_on_topic': ': free real time operating system protected under open source license',
		'date': 'December 2017',
	}
]

ai_posts = [
	{
		'class': 'AI/ML',
		'subclass': 'Reinforcement Learning',
		'link': 'https://www.freertos.org/',
		'link_about': 'freeRTOS',
		'more_on_topic': ': free real time operating system protected under open source license',
		'date': 'December 2017',
	}
]

app_posts = [
	{
		'class': 'AI/ML',
		'subclass': 'Reinforcement Learning',
		'link': 'https://www.freertos.org/',
		'link_about': 'freeRTOS',
		'more_on_topic': ': free real time operating system protected under open source license',
		'date': 'December 2017',
	}
]

@app.route('/')             # handle all background for home page of website
@app.route('/home')   		# 
@app.route('/about') 
def hello():
	return render_template('home.html', )

@app.route('/embedded')     # Behind on the link http://127.0.0.1:5000/projects
def embedded():
	return render_template('projects/embedded/index.html', title="Embedded Systems", posts=embedded_posts)

@app.route('/apps')
def apps():
	return render_template('projects/apps/index.html', title='Applications', posts=app_posts)

@app.route('/ai')
def ai():
	return render_template('projects/ai/index.html', title='Artificial Intelligence', posts=ai_posts)


if __name__ == '__main__': 	# True only if this module is run directly 
	app.run(debug=True)



