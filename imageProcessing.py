from PIL import Image, ImageFilter, ImageOps
from numpy import asarray


def resize_image(path):
    img = Image.open(path)
    newsize = (28, 28)
    img = img.resize(newsize)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    img = ImageOps.invert(img)
    img.save(path)

def image_to_np(path):
    img = Image.open(path)
    numpy_img = asarray(img)
    numpy_img = numpy_img[:,:,0]
    return numpy_img

