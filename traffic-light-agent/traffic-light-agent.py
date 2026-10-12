table = {"Red": "Stop", "Yellow": "Slow Down", "Green": "Go" , "Flashing red ": "Proceed with Caution", "Blinking Red": "Stop and Proceed When Safe"}
percept_sequence = ["Red", "Green", "Yellow", "Red"]

def traffic_light_agent(percept):
    return table.get(percept)

print("Percept\t\tAction")
for percept in percept_sequence:
    print(percept, "\t\t", traffic_light_agent(percept))
