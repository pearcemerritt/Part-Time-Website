from flask import Flask, jsonify
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("coffee_shop_menu.html")

@app.route('/menu_item/<item>', methods=['GET', 'POST'])
def fetch_menu_item(item):

  menu = { "latte": { "price": "$3.00", "image": "http://silvestregustolatino.com/magento/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/l/a/latte.jpg" },
           "coffee": { "price": "1.50", "image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTiZvw2eR-q2Dr_00NVTu6jwxPDaImuJ1O9RVuGxleJ_K_6YF1K" },
           "expresso": { "price": "$2.00", "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTHHYlW6C-taIfk0xZzotYieEvFytNPfLS3gCUzbyzefC6BrVkE4Q" }
          }

  return jsonify(menu[item])

if __name__ == "__main__":
  app.run()