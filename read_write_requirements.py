with open(r"C:\Development\aivision-pi\requirements.txt", "r") as file:
    data = file.readlines()


file2 = open(r"C:\Development\aivision-pi\requirements1.txt", "w")
for d in data:

    if d.find("=="):
        d = d[0 : d.find("==")]

    file2.write(d + "\n")

file2.close()
