from PIL import Image, ImageDraw, ImageFont
from PIL import PSDraw
im = Image.open("pic.jpg")
#myfont = ImageFont.truetype('C:/windows/Fonts/Arial.ttf', size=40)
myfont = ImageFont.truetype('/Librart/fonts/Arial.ttf', size=40)
draw = ImageDraw.Draw(im)
print(im.size[0]-40)
draw.text((im.size[0]-40,0),"4",font=myfont,fill="#ff0000")
im.save('result.jpg','jpeg')