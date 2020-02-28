from flask import Flask, render_template, url_for
app = Flask(__name__)       #special variable that is just the name of the module __name__ is same as __main__

class custom_post:
    title = ''
    image_link = ''
    num_posts = 0
    each_posts = []
    
    def __init__(self, title, image_link, num_posts, posts):
        self.title = title
        self.image_link = image_link
        self.num_posts = num_posts
        self.each_posts = posts
        return
    
    def __append_post__(post):
        self.each_posts.append(post)
        self.num_posts = self.num_posts + 1
        return
        
        
embedded_initial_posts = [
    {
        'subclass': 'Software',
        'link': 'https://www.eecs.umich.edu/courses/eecs473/labs.html',
        'link_about': 'Advanced Embedded Systems',
        'more_on_topic': ': University of Michigan. ',
        'date': 'December 2017',
    },
    {
        'subclass': 'Tools',
        'link': 'http://www.kicad-pcb.org/',
        'link_about': 'KiCad PCB Design',
        'more_on_topic': ': free tool for designing PCBs',
        'date': 'December 2017',
    },
    {
        'subclass': 'Libraries',
        'link': 'https://www.freertos.org/',
        'link_about': 'freeRTOS',
        'more_on_topic': ': free real time operating system protected under open source license',
        'date': 'December 2017',
    }
]
embedded_posts = custom_post('Embedded Systems', '', 3, embedded_initial_posts)


ai_inital_posts = [
	{
		'subclass': 'Reinforcement Learning',
		'link': 'https://xaviergeerinck.com/bellman-equations',
		'link_about': 'Bellman Equations',
                'more_on_topic': ': Allows us to write an equation that will represent State-Value function as a recursive relationship between value of state and value of its successor state.',
		'date': 'February 2020',
	},
]
ai_posts = custom_post('AI/ML', 'static/aigif.gif', 1, ai_inital_posts)


app_posts = [
	{ 
		'subclass': 'iOS Applications',
		'link': '',
		'link_about': '',
		'more_on_topic': 'Here lays all my applications which is 0 right now',
                'date': 'December 2017',
	}
]
app_posts = custom_post('Mobile Applications', 'static/codegif.gif', 1, app_posts)

galactic_posts = [
    { 
        'subclass': 'Fly to space',
        'link': '',
        'link_about': '',
        'more_on_topic': 'Galactic discoveries.',
                'date': 'December 2017',
    }
]
galactic_posts = custom_post('Galactic Report', 'static/earth.gif', 1, galactic_posts)


@app.route('/')             # handle all background for home page of website
@app.route('/home')   		# 
@app.route('/about') 
def hello():
	return render_template('home.html', )


@app.route('/embedded')     # Behind on the link http://127.0.0.1:5000/projects
def embedded():
	return render_template('projects/embedded/index.html', posts=embedded_posts)


@app.route('/apps')
def apps():
	return render_template('projects/apps/index.html', posts=app_posts)


@app.route('/ai')
def ai():
	return render_template('projects/ai/index.html', posts=ai_posts)

@app.route('/galactic')
def galactic():
    return render_template('projects/galactic/index.html', posts=galactic_posts)

if __name__ == '__main__': 	# True only if this module is run directly 
	app.run(debug=True)



