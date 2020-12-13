
import Adafruit_MCP3008 as MCP
import send_mail

CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = MCP.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

class Plant:
    def __init__(self, name, recommended_moisture_level, current_moisture_level):
        self.name = name
        self.recommended_moisture_level = recommended_moisture_level
        self.current_moisture_level = current_moisture_level
    def summary(self):
        return("Your " + self.name + " has a water level of " + str(self.current_moisture_level))  

plant_ports = {
    5: "Dill"
}        
        

def main():
    port_readings = {
        5: .2
    }
    plants =[] 
    for p in port_readings:
        plant = Plant(plant_ports[p], port_readings[p], mcp.read_adc(p))
        plants.append(plant)
    for p in plants:
        send_mail.send_reading_mail(p.summary())

main()