from PIL import Image
import numpy as np


an_image = Image.open("microrredes.png")
figure = an_image.convert("RGB")
figure.save('microrredes.eps', lossless = True)
