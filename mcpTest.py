
import Adafruit_MCP3008 as MCP


def main():
    CLK  = 18
    MISO = 23
    MOSI = 24
    CS   = 25
    mcp = MCP.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
    x = mcp.read_adc(5)
    print("5 reading is: ", x)
	
main()
