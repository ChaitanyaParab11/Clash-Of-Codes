import os
import urllib.parse
import requests

def url_to_image(url):
    if "google" in url:
        start = url.find("imgurl=") + len("imgurl=")
        end = url.find("&", start)
        image_url = url[start:end]

        decoded_image_url = urllib.parse.unquote(image_url)

        print(decoded_image_url)


        response = requests.get(decoded_image_url)
        img_data = response.content

        with open('image.jpg', 'wb') as f:
            f.write(img_data)

        filename = "image.jpg"
        path = os.path.abspath(filename)
        return path
    else:
        response = requests.get(url)
        img_data = response.content

        with open('image.jpg', 'wb') as f:
            f.write(img_data)

        filename = "image.jpg"
        path = os.path.abspath(filename)
        return path
