import math
from PIL import Image

def is_prime(n):
    if all(n % i != 0 for i in range(2, int(math.sqrt(n))+1)):
        return True
    else:
        return False

def gen_image(width, height):
    n = width * height

    im = Image.new("RGB", (width, height))
    pix = im.load()

    for y in range(height):# [0, height - 1]
        for x in range(width): # [0, width - 1]
            n = width * y + x + 1
            #print (n)
            if n == 1:
                pix[x, y] = (0, 0, 0)
                
            elif is_prime(n):
                pix[x,y] = (255, 0, 0)
                #print(n)
            else:
                pix[x,y] = (0, 0, 0)

    im.save("prime.png", "PNG")

gen_image(141, 141)

print('Done!')
