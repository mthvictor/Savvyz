from flask import Flask, render_template, request, redirect, url_for, flash
from price_history import get_amazon_product_id, get_history_chart

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/product', methods=['POST'])
def get_product():
    product_name = request.form['product_name']
    product_id = get_amazon_product_id(product_name)
    if product_id:
        get_history_chart(product_id, 'amazon')
    else:
        print('Product not found')

    return render_template('product.html', product_name=product_name, product_id=product_id)


if __name__ == '__main__':
    app.run()
