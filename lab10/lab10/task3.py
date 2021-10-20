import click
from PIL import Image, ImageFont, ImageDraw
from gfxhat import lcd, backlight, fonts
mydict = {}


def generateDictionary():
    file = open("font3.txt", "r")

    while True:
        fi = file.readline()
        if fi == "":
            break
        fi2 = fi.split(",")
        fi2[1] = fi2[1].replace("\n", "", 1) #remove a newline \n

        test = list(fi2[0][2:])
        myValList = []
        myFinalList = []
        outList = []
        for n in test:
            val = bin(int(n, 16))[2:] #use base 16 for integer conversion (i.e. C = 12)
            for i in range(4-len(val)):
                val = "0" + val
                i += 1
            myValList.append(val)
        for j in range(0, int(len(myValList)), 2):
            myFinalList.append(myValList[j] + myValList[j+1])
        for k in range(len(myFinalList)):
            outList.append(list(myFinalList[k]))
        for i in range(len(outList)):  #str change to int
            for j in range(len(outList[i])):
                outList[i][j] = int(outList[i][j])
                j += 1
            i += 1
        #print(outList)
        mydict[fi2[1]] = outList
        '''
        print(myFinalList)
        print(myValList)
        print(fi2)
        print(test)
        
        for i in range(len(outList)):
            for j in range(len(outList[i])):
                outList[i][j] = int(outList[i][j])
                j += 1
            i += 1
        '''
    file.close()



def displayObject(obj, x, y):
    lcd.clear()
    xp = x
    for y1 in obj:
        for x2 in y1:
            lenY = len(obj)
            lenX = len(y1)
            if x2 == 1:
                pixel = 1
            else:
                pixel = 0
            lcd.set_pixel(xp, y, pixel)
            xp += 1
        y += 1
        lcd.set_pixel(xp, y, pixel)
        xp = x
    lcd.show()

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    backlight.set_all(120,120,120)
    backlight.show()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
            lcd.show()

generateDictionary()
#print(mydict["#"])


print("Please press a key: ")
k = click.getchar()

#print(k)
n = 0
for key in mydict.keys():
    #print("key is:", key, "k is:", k)
    if key == k:
        binVal = mydict[key]
        displayObject(binVal, 20, 10)
        n = 1
        break
if n == 0:
    message = "The key you entered is not in the dictionary of the record."
    clearScreen(lcd)
    displayText(message, lcd, 20, 10)
    print(message)



'''
list(test)
["8","0","8","0",....]
! : ["bin(0x80)", "bin(0x80)", "bin(0x80)", "bin(0x80)", "bin(0x00)", "bin(0x80)", "bin(0x00)", "bin(0x00)"]
'''