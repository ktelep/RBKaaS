from PIL import Image
from StringIO import StringIO
from flask import Flask, send_file
import os

port = os.getenv('VCAP_APP_PORT', '4999')

def serve_pil_image(pil_img):
    img_io = StringIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

app = Flask(__name__)


@app.route('/')
@app.route('/<int:num_kittens>')
def index(num_kittens=1):

    kitten = Image.open("./static/kitten2.png").resize((128, 128))
    kitten.convert('RGBA')

    rainbow = Image.open("./static/Rainbow.jpg")

    kitten_x = 0
    for i in (range(num_kittens)):
        rainbow.paste(kitten, (kitten_x, 190), kitten)
        kitten_x = kitten_x + (rainbow.size[0]/num_kittens)
    return serve_pil_image(rainbow)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(port))
