lights = ["Red" , "Yellow" , "Green"]
currentLight = lights[2]

for light in lights:
    print(light)

if currentLight == "Green":
    print("Green Light On!")
elif currentLight == "Yellow":
    print("Ready To Go!")
else:
    print("Stop!")