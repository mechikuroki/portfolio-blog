import sys, os
from PIL import Image

if len(sys.argv) < 2:
    print("Too few arguments, proper syntax should be 'python image_formatter.py /PATH/TO/FILE")
    sys.exit(1)

img = Image.open(sys.argv[1])
res = img.resize((512, 512), Image.Resampling.LANCZOS)
os.remove(sys.argv[1])
res.show()
res.save(sys.argv[1])
