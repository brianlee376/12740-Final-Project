# Smart Home Automation - Sensing & Controlling
## 12740 Data Aquisition Fall 2021
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


# Introduction
This project demonstrates the applications of smart home technology. Using a Raspberry Pi to control a system of sensors and actuators, various functions in the home can be automated. For instance, temperature and humidity sensor can be programmed to turn on a fan when reaching a certain threshold. The benefit of automating these functions is improving both personal comfort and safety in the home. 

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
Smoke Sensor Testing | <img src="images/MQ2 Sensor Testing.jpg" alt="MQ2 sensor testing"  width="400"/>
Model House | <img src="images/model_house_inital.jpg" alt="model house"  width="400"/>

Highlights: In particular, articulate thing(s) you have learned / solved outside of what was taught in class
## Problems Encountered - Articulate the problems you have encountered
- Wiring the sensors correctly - having the wires going to the correct pinouts on the GPIO, determining whether resistors need to be added to the circuit, wiring the 5v relay, needing to double check wiring
- Frying sensors - caused by incorrect wiring
- Debugging code - understanding why the sensor is not giving an ouptut, why the controlling event is not being triggered
- Using multithreading to pull data from sensors simlutaneously
- Understanding how to use Github pages - figuring out how to add images that are from the web or local, formatting content

## Future Plan - Describe what you plan to do in the next two weeks
### This Week
1. Finish testing all sensors w/ functional code
2. Wire sensors into structure - this will be especially time consuming because of the extensive wiring that will be run under the model house
3. Wire sensors to raspberry pi
4. Record live demo video
5. Start Github page report

### Next Week
1. Finish report



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

Sensor             | Control |Image
:-------------------------:|:-------------------------:|:-------------------------:
Buzzer | NA | <img src="http://cdn.shopify.com/s/files/1/0068/3399/5894/products/DSC_1892_grande.jpg?v=1590559539" alt="buzzer sensor"  width="200"/>
Carbon Monoxide | Fan & Buzzer | <img src="https://www.twinschip.com/image/cache/catalog/Products%20Twins%20Chip%20Store%202020/Shield%20Modules/Sensors/MQ-7%20Sensitive%20Detecting%20Carbon%20CO%20Gas%20Porduct/MQ-7%20Sensitive%20Detecting%20CO%20Gas%20Twins%20Chip%201-550x550.jpg" alt="carbon monoxide sensor"  width="200"/>
DHT11 Temperature & Humidity | Fan |  <img src="https://www.robotshop.com/media/catalog/product/cache/image/1350x/9df78eab33525d08d6e5fb8d27136e95/d/h/dht11-temperature-humidity-sensor-module.jpg" alt="dht11 temperature & humidity sensor"  width="200"/>
Flame | LED & Buzzer | <img src="https://www.pcboard.ca/image/cache/catalog/products/flame-sensor/Flame-Sensor-Module-800x800.jpg" alt="carbon monoxide sensor"  width="200"/>
MQ2 Smoke | Fan & Buzzer | <img src="https://img.joomcdn.net/21d689accaa9b832d434936c1b8058a4e05b16a5_original.jpeg" alt="smoke sensor"  width="200"/>
Passive Infrared (PIR) | LED | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/b2267b506d4e4594666ef83a79896a9a/p/e/perspective_3_3.jpg" alt="carbon monoxide sensor"  width="200"/>
Photoresistive | LED | <img src="https://osoyoo.com/wp-content/uploads/2017/09/14.jpg" alt="photoresistive sensor"  width="200"/>
Touch | LED | <img src="https://imgaz3.staticbg.com/thumb/large/upload/2012/lidanpo/SKU117322%20(1).jpg" alt="touch sensor"  width="200"/>



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

