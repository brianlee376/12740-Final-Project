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

# Motivation
The project we set out to accomplish was the successful coding, wiring, and demonstration of a mock smart home system. We chose this project to gain a better understanding of how in-home monitoring systems could work and to gain experience setting them up ourselves. As such, our group decided to use as many sensors as possible to gain familiarity with many different sensing systems. 

# Goals
By the end of the project, we hope to create a mock smart house that can respond to environmental phenomena including fire, smoke, carbon monoxide, touch, light, temperature, humidity, and movement. We will set a threshold value for each phenomena and, if that threshold is crossed, some function within the home (buzzer, fan, etc.) will be activated in response.

# Progress Report
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

## Challenges Encountered:
- Wiring and Sensor Management: Keeping track of the GPIO pin assignments to each transducer, labeling wires and ensuring that they are connected properly, connecting transducers to appropriate voltage (3.3V or 5V), as more sensors are added to the system it becomes more difficult to keep track of
- Damaged Sensors: Incorrect wiring caused us to short circuit some of our transducers
- Code Management: Learning how to pull data from multiple sensors simultaneously. Figuring out a way to get all sensors to run in the same loop while having different refresh rates. Developing a smart way to get ensure that fans, lights, etc activate at the correct time, resolving conflicts if they receive different messages from different sensors. 
- General Troubleshooting: Trying to determine if an error is occuring due to a wiring or a coding error
- Debugging code: Understanding why a sensor is not giving an ouptut, why the controlled event is not being triggered
- Understanding how to use Github pages: Figuring out how to add images that are from the web or local, formatting content

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

Sensor             | Control |Image | Description
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------
Carbon Monoxide | Fan & Buzzer | <img src="https://www.twinschip.com/image/cache/catalog/Products%20Twins%20Chip%20Store%202020/Shield%20Modules/Sensors/MQ-7%20Sensitive%20Detecting%20Carbon%20CO%20Gas%20Porduct/MQ-7%20Sensitive%20Detecting%20CO%20Gas%20Twins%20Chip%201-550x550.jpg" alt="carbon monoxide sensor"  width="200"/> | <ul><li>Analog and Digital</li></ul>
DHT11 Temperature & Humidity | Fan |  <img src="https://www.robotshop.com/media/catalog/product/cache/image/1350x/9df78eab33525d08d6e5fb8d27136e95/d/h/dht11-temperature-humidity-sensor-module.jpg" alt="dht11 temperature & humidity sensor"  width="200"/> | <ul><li>Digital Output</li><li>Accuracy: +/- 5% RH, +/- 2 deg C </li></ul>
Flame | LED & Buzzer | <img src="https://www.pcboard.ca/image/cache/catalog/products/flame-sensor/Flame-Sensor-Module-800x800.jpg" alt="carbon monoxide sensor"  width="200"/> | <ul><li>Analog and Digital Output</li><li>Working Voltage: 3.3V-5V</li><li>Sensing Range: 20cm ~ 100cm</li><li>Input: Flame/light with wavelength 760nm - 1100nm </li></li></ul>
MQ2 Smoke | Fan & Buzzer | <img src="https://img.joomcdn.net/21d689accaa9b832d434936c1b8058a4e05b16a5_original.jpeg" alt="smoke sensor"  width="200"/> | <ul><li>Analog and Digital Output</li></ul>
Passive Infrared (PIR) | LED | <img src="https://media-cdn.seeedstudio.com/media/catalog/product/cache/b2267b506d4e4594666ef83a79896a9a/p/e/perspective_3_3.jpg" alt="carbon monoxide sensor"  width="200"/> | <ul><li>Digital Output</li><li>Voltge: 5V-20V</li><li>TTL Voltage: 3.3V, 0V</li><li>Power Consumption: 65mA </li><li>Sensing Range: Within 120 degrees, 7m</li><li>Working Temperature: -15 ~ 70 F </ul>
Photosensitive | LED | <img src="https://osoyoo.com/wp-content/uploads/2017/09/14.jpg" alt="photoresistive sensor"  width="200"/> | <ul><li>Analog and Digital Output</li><li>Working Voltage: 3.3V-5V</li></ul>
Touch | LED | <img src="https://imgaz3.staticbg.com/thumb/large/upload/2012/lidanpo/SKU117322%20(1).jpg" alt="touch sensor"  width="200"/> | <ul><li>Digital Output</li></ul>

## Signal Conditioning and Processing
In order to ensure that each sensor was working as intended, we would test it before adding it to the overall system. Some of the more difficult sensors to test and implement were the smoke and carbon monoxide sensors. To test these, we figured out that cigarettes release both of these substances and decided to use them to set up these sensors. For other sensors, we also experimented with the sampling rate as it could vary greatly between different sensors. The temperature and humidity sensor, for example, was originally set up to sample at a rate of once per second. But after, experimentation, we found that a delay of 5 seconds between measurements gave us the best combination of accuracy and granularity. 

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

# References
### Code

1. Kookeye. KOOKYE Smart Home Sensor Kit for Arduino Raspberry Pi Tutorial Code https://kookye.com/2016/08/01/smart-home-sensor-kit-for-arduinoraspberry-pi/
2. 

### Images

1. MQ7 Carbon Monoxide Sensor: https://www.twinschip.com/image/cache/catalog/Products%20Twins%20Chip%20Store%202020/Shield%20Modules/Sensors/MQ-7%20Sensitive%20Detecting%20Carbon%20CO%20Gas%20Porduct/MQ-7%20Sensitive%20Detecting%20CO%20Gas%20Twins%20Chip%201-550x550.jpg
2. DHT11 Temperature & Humidity Fan: https://www.robotshop.com/media/catalog/product/cache/image/1350x/9df78eab33525d08d6e5fb8d27136e95/d/h/dht11-temperature-humidity-sensor-module.jpg
3. Flame Sensor: https://www.pcboard.ca/image/cache/catalog/products/flame-sensor/Flame-Sensor-Module-800x800.jpg
4. MQ2 Smoke Sensor: https://img.joomcdn.net/21d689accaa9b832d434936c1b8058a4e05b16a5_original.jpeg
5. Passive Infrared PIR Sensor: https://media-cdn.seeedstudio.com/media/catalog/product/cache/b2267b506d4e4594666ef83a79896a9a/p/e/perspective_3_3.jpg
6. Photoresistive Sensor: https://osoyoo.com/wp-content/uploads/2017/09/14.jpg
7. Touch Sensor: https://imgaz3.staticbg.com/thumb/large/upload/2012/lidanpo/SKU117322%20(1).jpg






