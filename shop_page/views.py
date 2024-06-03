import flask
from registration_page.models import User
from login_page.views import log
import os
import pandas
from admin_app.models import Product
from project.settings import DATABASE

def render_shop():
    global product

    if len(list(Product.query.all())) == 0:

        excel_path = os.path.abspath(__file__ + '/../static/Product.xlsx')
        data_excel = pandas.read_excel(io = excel_path, header = None, names = ["name", "price", "image", "count", "final_price"])
        for row in data_excel.iterrows():
            row_data = row[1]
            product = Product(
                name = row_data['name'],
                price = row_data['price'],
                image = row_data['image'],
                count = row_data['count'],
                final_price = row_data["final_price"]
            )
            DATABASE.session.add(product)
        DATABASE.session.commit()



    print(Product.query.get(3))

    name = flask.session.get('log')





    return flask.render_template(template_name_or_list= "shop.html", log = name, products = Product.query.all())

def new_func():
    print(f"Test: {User.query.get(True)}")