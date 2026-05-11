import random as r

feet_in_miles = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon","Paul McCartney","George Harrison","Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".")+ 1:]

def roll_dice(num):
    return r.randint(1,num)
