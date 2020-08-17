from PIL import Image,ImageFilter
import os,sys

os.chdir(sys.path[0])
image = Image.open('./img.jpg')
image.filter(ImageFilter.CONTOUR).show()
image.show()
