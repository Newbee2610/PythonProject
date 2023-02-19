from PIL import Image

img = Image.open('paper.png')
new_width  = 219
new_height = 231
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('roky.png')