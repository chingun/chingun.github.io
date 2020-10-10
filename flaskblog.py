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
        'subclass': 'Projects:',
        'link': 'https://www.youtube.com/watch?v=RmNvX2cUl6A&ab_channel=ElectricalandComputerEngineeringatMichigan',
        'link_about': 'Crowd Sourced Rescue Robot',
        'more_on_topic': 'Sending rescue robots into disaster struck areas to aid rescue workers through crowd help. The deep dive into the project is written in the presentation.',
        'has_more': True,
        'sensors': ['Poison Gas Sensor', '3D view camera module', 'GPS'],
        'techs': ['I2C', 'SPI', 'WiFi'],
        'actions': ['Embedded Software in C/C++', 'PCB Hardware with Eagle', 'Circuit Simulation using Cadence'],
        'date': 'December 2017',
        'image_link': 'static/pictures/crowdDev.png',
        'image_link1': 'static/pictures/slide.png',
    },
    {
        'link': 'https://www.youtube.com/watch?v=RmNvX2cUl6A&ab_channel=ElectricalandComputerEngineeringatMichigan',
        'link_about': 'Virtual Reality Controller Headset',
        'more_on_topic': 'Giving an intuitive and immersive control for the rescue worker with VR control.',
        'has_more': True,
        'sensors': ['IMU'],
        'techs': ['I2C', 'SPI', 'Bluetooth'],
        'actions': ['Firmware with FreeRTOS in C/C++', 'PCB Hardware with Eagle', 'Circuitry Simulation using Cadence'],
        'image_link': 'static/pictures/VR.png',
    },
    {
        'link': 'https://www.lookingbus.com',
        'link_about': 'Looking Bus Beacon',
        'more_on_topic': 'A beacon device that make bus travel easy and safe for visually impaired people.',
        'has_more': True,
        'sensors': ['Bluetooth'],
        'techs': ['I2C'],
        'actions': ['Firmware with Texas Instruments RTOS in C', 'PCB Hardware with Eagle', 'Power Circuitry with Solar Panels'],
        'image_link': 'static/pictures/lookingbus.png',
    },
    {
        'subclass': 'Favorite Tools:',
        'link': 'http://www.kicad-pcb.org/',
        'link_about': 'KiCad PCB Design',
        'more_on_topic': 'I use KiCAD and Eagle to design the PCBs of the embedded systems.',
        'has_more': False,
        'date': 'December 2017',
    },
    {
        'link': 'https://www.freertos.org/',
        'link_about': 'C/C++',
        'more_on_topic': 'Fluency and professional experience in Multithreading, Data Structures and Algorithms',
        'has_more': False,
        'date': 'December 2017',
    },
    {
        'link': 'https://www.freertos.org/',
        'link_about': 'FreeRTOS',
        'more_on_topic': 'Regularly used Real Time Operating Systems for different shipping project to meet tight deadlines and guaranteed reliability.',
        'has_more': False,
        'date': 'December 2017',
    },
    {
        'link': 'https://www.freertos.org/',
        'link_about': 'Communication Protocols',
        'more_on_topic': 'Utilized I2C, SPI, CAN, Bluetooth and WiFi in shipping projects.',
        'has_more': False,
        'date': 'December 2017',
    }
]
embedded_posts = custom_post('Embedded Systems', 'static/pictures/crowdDev.png', 3, embedded_initial_posts)


ai_inital_posts = [
    { 
        'subclass': 'Projects:',
        'ml_class': 'Reinforcement Learning',
        'link': '#',
        'link_about': 'Machine Learning',
        'more_on_topic': 'Coming soon',
        'date': 'February 2020',
    },
    { 
        'ml_class': 'Reinforcement Learning',
        'link': '#',
        'link_about': 'Generative Adverserial Network',
        'more_on_topic': 'Coming Soon',
        'date': 'February 2020',
    },
    { 
        'ml_class': 'Reinforcement Learning',
        'link': '#',
        'link_about': 'Deep Neural Network',
        'more_on_topic': 'Coming soon',
        'date': 'February 2020',
    },
]

ai_posts = custom_post('AI/ML', 'static/pictures/aigif.gif', 1, ai_inital_posts)
app_posts = [
    { 
        'subclass': 'Projects:',
        'link_about': 'Git Journal',
        'link': 'gitjournal.com',
        'more_on_topic': 'A version controlled journalling application, built using the MERN stack, that attempts to offer a new kind of writing and authoring experience.',
        'has_more': True,
        # 'sensors': ['Poison Gas Sensor', '3D view camera module', 'GPS'],
        'techs': ['React.js'],
        'actions': ['MongoDB: primarily used for database management.', 
			        'ExpressJS: Minimal NodeJS web application framework.', 
			        'ReactJS: JavaScript library for building user interfaces and front-end components. ', 
			        'NodeJS: back end runtime environment that execytes javascript code on the back end server.', 
			        'Redux: Used in combination with ReactJS to manage application state.', 
			        'DraftJS: To develop a beautiful rich text editor for the best writing and reading experience.'],
        'date': 'December 2020',
        # 'image_link': 'static/pictures/insta485.png',
        # 'image_link1': 'static/pictures/slide.png',
    },
    { 
        'link_about': 'Insta 485',
        'more_on_topic': 'It is almost instagram, you can create profile, login, logout, upload pictures, see newseed, follow, comment, and like.',
        'has_more': True,
        # 'sensors': ['Poison Gas Sensor', '3D view camera module', 'GPS'],
        'techs': ['Flask', 'Jinja', 'React.js', 'Webpack', 'SQLite'],
        'actions': ['Flask', 'Jinja', 'SQLite'],
        'date': 'December 2019',
        'image_link': 'static/pictures/insta485.png',
        # 'image_link1': 'static/pictures/slide.png',
    },
	{ 
        'link': 'https://www.lookingbus.com/',
        'link_about': 'Looking bus',
        'more_on_topic': 'An Android application that communicates with street beacon devices to make travel on buses easier and safer for blind or visually impaired people.',
        'has_more': True,
        # 'sensors': ['Poison Gas Sensor', '3D view camera module', 'GPS'],
        'techs': ['Java'],
        'actions': ['Java','Android Studio'],
        'date': 'December 2019',
        # 'image_link': 'static/pictures/insta485.png',
        # 'actions': ['Flask', 'React.js', 'SQLite', 'Hadoop', 'Socket', 'Multithreading'],
        # 'date': 'December 2019',
        # 'image_link': 'static/pictures/insta485.png',
        # 'image_link1': 'static/pictures/slide.png',
	}
]
app_posts = custom_post('Software', 'static/pictures/codegif.gif', 1, app_posts)

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
galactic_posts = custom_post('Galactic Report', 'static/pictures/earth.gif', 1, galactic_posts)

@app.route('/')             # handle all background for home page of website
@app.route('/home')   		# 
@app.route('/about')        # Decorator! Patterns for routing Function that operates on a function but is not used in C or C++ 
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

@app.route('/websurfer')
def websurfer():
    return render_template('projects/websurfer/index.html')

if __name__ == '__main__': 	# True only if this module is run directly 
	app.run(debug=True)



