from PIL import Image
import os
# converts all jpg in the folder to png
try:
    os.makedirs("PNG")
except FileExistsError:
    pass
for f in os.listdir("."):
    if f.endswith(".jpg"):
        Image.open(f).save(f"PNG/{f.replace('.jpg','.png')}")
        print(f+" done")
