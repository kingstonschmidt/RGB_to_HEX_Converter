# _________________________________________________6.RGB to HEX__________________________________________________ #

# Variables
count = 0
hex_code = ""
first_number = 0
hex_frame = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F"]


# User input
number = int(input("choose r:\n> "))
number1 = int(input("choose g:\n> "))
number2 = int(input("choose b:\n> "))


# ------------------------------------------------CONVERT TO HEX----------------------------------------------------- #

rgb_numbers = number, number1, number2

for rgb in rgb_numbers:
    if rgb > 255:
        rgb = 255
    elif rgb < 0:
        rgb = 0

    for i in range(rgb):
        count += 1
        if count > 15:
            first_number += 1
            count = 0

    left = hex_frame[first_number][1]
    right = hex_frame[count][1]
    hex_code += left + right
    count = 0
    first_number = 0

print(f"rbg:{rgb_numbers}")
print(f"hex_code:{hex_code}")
