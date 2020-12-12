
import Adafruit_MCP3008 as MCP

CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = MCP.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def main():
    read_port(5)
    
def read_port(port):
    current_level = mcp.read_adc(port)
    current_reading_message = str(port) + ' has a current moisture level of ' +str(current_level)
    print(current_reading_message)
	
main()
