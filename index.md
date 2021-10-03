# Smart Home Automation - Sensing & Controlling Fall 2021
Team Members: Brian Lee, Cheyu Lin, Ryan Rusali, Matt Takara

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/brianlee376/12740-Smart-Home-IoT/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.


# Introduction
Our project proves the feasibilty and demonstrates the convenience of smart home technlogy. Through the use of sensors, certain actions are triggered when the sensor has a certain reading. For example, if motion is detected at the entrace, the lights will turn on.

Write a brief summary of your project

# Motivation
Motivate the problem you plan to address
Why is the problem you are addressing important or interesting?

Want to create a controllable mock living space using inputs from sensors

# Goals
What are you going to achieve by the end of the project specifically?

Improve general living conditions in the model space
Comfort
Safety
Efficiency


# For Progress Report
## Current Progress
- Built main frame of model house
- Testing sensors we are planning on using
- Creating main code file that will pull from sensor code files

Item             |  Image
:-------------------------:|:-------------------------:
LED Control w/ Touch Sensor | <img src="images/touch_led.jpg" alt="touch sensor and LED setup"  width="400"/>
Fan Control w/ Touch Sensor & Relay | <img src="images/touch_relay_fan.jpg" alt="fan control with touch sensor & relay"  width="400"/>
Model House | <img src="images/model_house_inital.jpg" alt="model house"  width="400"/>

Highlights: In particular, articulate thing(s) you have learned / solved outside of what was taught in class
## Problems Encountered - Articulate the problems you have encountered
- Wiring the sensors correctly
- Debugging code
- Frying sensors
- Using multithreading
- Understanding how to use Github pages

This section is of the most importance in the progress report. It not only give the TA information on what help you may need, and also encourages you to think deeper about your problems.
## Future Plan - Describe what you plan to do in the next two weeks
1. Finish testing all sensors w/ functional code
2. Wire sensors into structure
3. Wire sensors to raspberry pi
4. Record live demo video
5. Start Github page report



# Methodology
## Phenomena of Interest
Describe the physical phenomena of interest, e.g. physical principles, static and dynamic behavior, and signal characteristics

Presence of fire
Touch
Light
Temperature
Smoke
Carbon-monoxide


## Sensor(s) Used
Describe the sensor(s) you used, e.g. physical principles, static and dynamic behavior, and signal characteristics

Flame sensor -> Buzzer, Slack message
Touch -> Buzzer
PIR w/ Photosensitive -> LED
Temperature -> Fan
Smoke -> Slack message
Carbon monoxide -> Slack message

Sensor             |  Image
:-------------------------:|:-------------------------:
DHT11 Temperature & Humidity | <img src="https://www.robotshop.com/media/catalog/product/cache/image/1350x/9df78eab33525d08d6e5fb8d27136e95/d/h/dht11-temperature-humidity-sensor-module.jpg" alt="dht11 temperature & humidity sensor"  width="200"/>
Touch | <img src="https://imgaz3.staticbg.com/thumb/large/upload/2012/lidanpo/SKU117322%20(1).jpg" alt="touch sensor"  width="200"/>
Photoresistive | <img src="https://osoyoo.com/wp-content/uploads/2017/09/14.jpg" alt="photoresistive sensor"  width="200"/>
MQ2 Smoke | <img src="https://img.joomcdn.net/21d689accaa9b832d434936c1b8058a4e05b16a5_original.jpeg" alt="smoke sensor"  width="200"/>
Carbon-monoxide | <img src="https://www.twinschip.com/image/cache/catalog/Products%20Twins%20Chip%20Store%202020/Shield%20Modules/Sensors/MQ-7%20Sensitive%20Detecting%20Carbon%20CO%20Gas%20Porduct/MQ-7%20Sensitive%20Detecting%20CO%20Gas%20Twins%20Chip%201-550x550.jpg" alt="carbon monoxide sensor"  width="200"/>


## Signal Conditioning and Processing
Describe the signal conditioning and processing procedures

# Experiments and Results
Describe the experiments you did and present the results; Use tables and plots if possible

# Discussion
Discuss the insights from the project

Not knowing if the carbon monoxide sensor is working properly
Being able to link up all the sensors to the board
Are there enough pinouts on the Raspberry PI?
Getting power to all the sensors + fan
Making sure the smoke sensor doesn’t get damaged and is working properly
Designing & building the model house

