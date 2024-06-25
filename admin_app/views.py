import flask
from registration_page.models import User
from login_page.views import log
import os
import pandas
from .models import Product
from project.settings import DATABASE



def render_admin():
    global product, count

    






    

    if flask.request.method == "POST":
        btn = flask.request.form.get("rewrite")
        button_delete = flask.request.form.get("delete")
        add_product = flask.request.form.get("add_btn")

        print(add_product)

        if button_delete != None and btn == None and add_product == None:
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
                
            write = product.query.get_or_404(flask.request.form.get("delete"))
            DATABASE.session.delete(write)
            DATABASE.session.commit()

            

            count = 1
            index = 1



            print(int(flask.request.form.get("delete")))
            for product in Product.query.all():   
                try:         

                    product2 = Product.query.get(count + int(button_delete)) 
                    product2.id = count
                    print(product2.id)

                    print(count, index)

                    count += 1
                except:
                    pass



            DATABASE.session.commit()
            



            
            print(Product.query.all())




        if btn != None and button_delete == None and add_product == None:
            flask.session['flag'] = btn
            




            print(btn)
            return flask.redirect("/admin/redact/")

        if add_product != None and button_delete == None and btn == None:

            return flask.redirect("/shop/add/")


    name = flask.session.get('log')

    # if flask.request.method == "POST":
    #     return flask.redirect("/admin/redact/")

    
    users = User.query.filter_by(is_admin = True).all()
    
    nicknames = []






    for user in users:
        nicknames.append(str(user).split(":")[1])
        

    for nickname in nicknames:
        print(nickname)
        print(name)

        if nickname == " " + name:
            return flask.render_template(template_name_or_list= "admin.html", log = name, products = Product.query.all())
    return flask.redirect("/shop/") 

