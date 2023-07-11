from bs4 import BeautifulSoup
import requests
import os
from PIL import Image


def compare_images(image_path1, image_path2):
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    if image1.size != image2.size:
        return False

    image1_pixels = image1.load()
    image2_pixels = image2.load()

    width, height = image1.size
    for x in range(width):
        for y in range(height):
            if image1_pixels[x, y] != image2_pixels[x, y]:
                return False

    return True


def get_amazon_product_id(product_name):
    formatted_product_name = product_name.replace(' ', '+')
    search_url = f"https://www.amazon.fr/s?k={formatted_product_name}"
    headers = ({
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    })
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all(
        'div', {'data-component-type': 's-search-result'})
    for result in search_results:
        if 'AdHolder' in result['class']:
            continue
        product_id = result['data-asin']
        return product_id
    return None


def get_history_chart(product_id, chart_type):
    if chart_type == 'amazon':
        chart_url = f'https://charts.camelcamelcamel.com/fr/{product_id}/amazon.png?force=1&zero=0&w=854&h=512&desired=false&legend=1&ilt=1&tp=all&fo=0&lang=fr_FR'
    else:
        chart_url = f'https://charts.camelcamelcamel.com/fr/{product_id}/new.png?force=1&zero=0&w=854&h=512&desired=false&legend=1&ilt=1&tp=all&fo=0&lang=fr_FR'
    chart_image_path = os.path.join('static', 'images', 'chart.png')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    }
    response = requests.get(chart_url, headers=headers)
    if response.status_code == 200:
        with open(chart_image_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image. Status code: {response.status_code}")
    if compare_images(chart_image_path, "static/images/unavailable.png"):
        get_history_chart(product_id, 'new')
