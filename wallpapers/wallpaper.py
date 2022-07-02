#!/bin/python3

import random, subprocess

path = "/home/user0/wallpapers/"
pref = "wallpaper"

counter0 = subprocess.check_output("ls /home/user0/wallpapers/ | wc -l", shell=True)
counter1 = int(counter0)

check = True
while check == True:
    n = random.random()
    counter = int(counter1 * n)
    if counter <= 0 or counter >= counter1:
        check = True
    else:
        check = False

nfile = str(counter)

png = ("7", "8", "14", "16")

if nfile in png:
    ext = ".png"
else:
    ext = ".jpg"

file = str(path + pref + nfile + ext)

cmd = str("feh --bg-fill " + file)
error = subprocess.check_output(cmd, shell=True)
#print(error)
