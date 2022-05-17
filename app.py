# from PIL import Image

# im = Image.open("1.png")

# print(im.format, im.size, im.mode)

# # im.show()


from PIL import Image
from io import BytesIO

buffer = BytesIO()
buffer.write(open('1.png', 'rb').read())
buffer.seek(0)

image = Image.open(buffer)
print (image)
# <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=800x600 at 0x7FE2EEE2B098>

# if we try open again
image = Image.open(buffer)

# traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "/usr/lib/python2.7/dist-packages/PIL/Image.py", line 2028, in open
#    raise IOError("cannot identify image file")
# IOError: cannot identify image file