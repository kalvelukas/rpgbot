import random

def rng():
    all_chars = list (("!","§","$","%","&","/","(",")","=","?","1","2","3","4","5","6","7","8","9"",0","ß","q","w","e","r","t","z","u","i","o","p","a","s","d","f","g","h","j","k","l","y","x","c","v","b","n","m","Q","W","E","R","T","Z","U","I","O","P","A","S","D","F","G","H","J","K","L","Y","X","C","V","B", "N", "M"))
    i = 0
    pwlen = 16
    pw = " "
    while i < pwlen:
        char = random.randint(0, (len(all_chars) - 1))
        charadd = all_chars [char]
        pw = pw + charadd
        i = i + 1
    return pw

if __name__ == "__main__":
    print (rng())