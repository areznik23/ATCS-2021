mtns = {"Everest": 8848, "K2": 8611, "Kangchenjunga": 8586, "Lhotse": 8516, "Makula": 8485}
for name in mtns.keys():
    print(name)
for elev in mtns.values():
    print(elev)
for name, elev in mtns.items():
    print(name + " is " + str(elev) + " meters tall")
