import os
# pip install pillow
from PIL import Image
from pathlib import Path

from flask import url_for, current_app


def add_profile_pic(pic_upload, username):
    filename = pic_upload
    # Grab extension type .jpg or .png
    ext_type = filename.split('.')[-1]
    storage_filename = str(username) + '.' + ext_type

    filepath = os.path.join(current_app.root_path, 'static\Profile_Pic', storage_filename)
    openingFile = os.path.join(current_app.root_path, 'static\Profile_Pic', filename)
    # Play Around with this size.
    output_size = (200, 200)

    # Open the picture and save it
    pic = Image.open(openingFile)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
