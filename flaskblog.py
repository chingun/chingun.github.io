from flask import Flask, render_template, url_for
app = Flask(__name__) # special variable that is just the name of the module __name__ is same as __main__

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
        'subclass': 'My Projects:',
        'link': 'https://www.youtube.com/watch?v=RmNvX2cUl6A&ab_channel=ElectricalandComputerEngineeringatMichigan',
        'link_about': 'Crowd Sourced Rescue Robot',
        'more_on_topic': 'Sending rescue robots into disaster struck areas to aid rescue workers through crowd help. The deep dive into the project is written in the presentation.',
        'has_more': True,
        'sensors': ['Poison Gas Sensor', '3D view camera module', 'GPS'],
        'techs': ['I2C', 'SPI', 'WiFi'],
        'actions': ['Embedded Software in C/C++', 'PCB Hardware with Eagle', 'Circuit Simulation using Cadence'],
        'date': 'December 2017',
        'image_link': 'static/crowdDev.png',
        'image_link1': 'static/slide.png',
    },
    {
        'link': 'https://www.youtube.com/watch?v=RmNvX2cUl6A&ab_channel=ElectricalandComputerEngineeringatMichigan',
        'link_about': 'Virtual Reality Human Interface Device for tracking head movement',
        'more_on_topic': 'Giving an intuitive and immersive control for the rescue worker with VR control.',
        'has_more': True,
        'sensors': ['IMU'],
        'techs': ['I2C', 'SPI', 'Bluetooth'],
        'actions': ['Firmware with FreeRTOS in C/C++', 'PCB Hardware with Eagle', 'Circuitry Simulation using Cadence'],
        'image_link': 'static/VR.png',
    },
    {
        'link': 'https://www.lookingbus.com',
        'link_about': 'Looking Bus',
        'more_on_topic': 'A beacon device that make bus travel easy and safe for visually impaired people.',
        'has_more': True,
        'sensors': ['Bluetooth'],
        'techs': ['I2C'],
        'actions': ['Firmware with Texas Instruments RTOS in C', 'PCB Hardware with Eagle', 'Power Circuitry with Solar Panels'],
        'image_link': 'static/lookingbus.png',
    },
    {
        'subclass': 'Resources:',
        'link': 'https://www.eecs.umich.edu/courses/eecs473/labs.html',
        'link_about': 'Advanced Embedded Systems',
        'more_on_topic': 'University of Michigan. ',
        'date': 'December 2017',
    },
    {
        'link': 'http://www.kicad-pcb.org/',
        'link_about': 'KiCad PCB Design',
        'more_on_topic': 'free tool for designing PCBs',
        'date': 'December 2017',
    },
    {
        'link': 'https://www.freertos.org/',
        'link_about': 'freeRTOS',
        'more_on_topic': 'free real time operating system protected under open source license',
        'date': 'December 2017',
    }
]
embedded_posts = custom_post('Embedded Systems', 'static/crowdDev.png', 3, embedded_initial_posts)


ai_inital_posts = [
	{
        'subclass': 'Resources:',
		'ml_class': 'Reinforcement Learning',
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
app_posts = custom_post('Software', 'static/codegif.gif', 1, app_posts)

galactic_posts = [
    { 
        'subclass': 'Game',
        'title': 'Flappy Bird',
        'link': '',
        'link_about': '',
        'more_on_topic': 'Press any key to play.',
        'date': 'December 2017',
    }
]
galactic_posts = custom_post('Galactic Report', 'static/earth.gif', 1, galactic_posts)

@app.route('/')             # handle all background for home page of website
@app.route('/home')   		# 
@app.route('/about')  # Decorator! Patterns for routing Function that operates on a function but is not used in C or C++ 
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



