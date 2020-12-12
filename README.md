# plant_watering_script
script to read water levels and send readings by email

This project utilitzes a raspberry pi + moisture detector to take digitized reading through an SPI Interface device, MCP_3008. 

It leverages the AdaFruit_MCP3008 python library to take readings and send messaging notifications.

In order to correctly set up the hardware as well as the necessary libraries please reference: 
https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008

The values used for email addresses and email account keys are stored in a protected property file not in source control. 
Add this file to your local project directory and name it '.env'. 
