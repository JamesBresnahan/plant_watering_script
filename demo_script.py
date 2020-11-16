class Plant:
    def __init__(self, name, water_level):
        self.name = name
        self.water_level = water_level
    def summary(self):
        print("Your " + self.name + " has a water level of " + str(self.water_level))  

plant_ports = {
    0: "Dill",
    5: "Basil"
}        
        

def main():
    port_readings = {
        0: .8,
        5: .2
    }
    plants =[] 
    for p in port_readings:
        plant = Plant(plant_ports[p], port_readings[p])
        plants.append(plant)
    for p in plants:
        p.summary()

main()