# Jobsite_Automation
Summer project at Graybar Innovation Lab
 to automate the material replenishment process at the jobsites.

The codes are written in Python and Arduino IDE.

You will first need to upload the Arduino IDE code into the Arduino connected to the Raspberry Pi. The code can be found in the sketch_RFmodule folder under the name sketch_jul17a.ino
Here is a direct link to the code https://github.com/kacperp94/Jobsite_Automation/blob/master/sketch_RFmodule/sketch_jul17a.ino

You would need the Radio Head library to run this code which can be downloaded from http://www.airspayce.com/mikem/arduino/RadioHead/RadioHead-1.41.zip

To run the python codes just run the main.py file and it calls the functions and other python files that are required to support it.
The other scripts that are required for this project (which are called by main.py) are in the lib folder: notification.py , read_serial.py

The sample.csv file contains details about the various products placed in different bins. It contains 7 columns:
1) ID for the different load cells/arduinos/transmitters
2) W which stands for current weight
3) InitW which provides the initial weight for the products
4) minL which gives the minimum threshold for the product in terms of percentage
5) S is just an indicator that lets you know if a notification has already been sent or not for a particular product. 0 is for not sent and 1 is for sent
6) Product is the product name
7) jsno is the jobsite number