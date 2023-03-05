import requests
from bs4 import BeautifulSoup

google_images_url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fc8.alamy.com%2Fcomp%2FBE7EHD%2Fyoung-man-looking-at-camera-with-head-tilted-and-brow-furrowed-BE7EHD.jpg&imgrefurl=https%3A%2F%2Fwww.alamy.com%2Fstock-photo-young-man-looking-at-camera-with-head-tilted-and-brow-furrowed-25980681.html&tbnid=Pgr1fGbkgn0u7M&vet=12ahUKEwi7r_n3mMT9AhUUQnwKHQA1CVMQMygLegUIARDnAQ..i&docid=TVDyw1dJdUacnM&w=1300&h=957&q=Man%20Tilted%20faces&ved=2ahUKEwi7r_n3mMT9AhUUQnwKHQA1CVMQMygLegUIARDnAQ"

res = requests.get(google_images_url)
soup = BeautifulSoup(res.text, 'html.parser')
img_url = soup.find('img')['src']
print(img_url)
