from  flask import *
a=Flask("_name_")
@a.route('/')
@a.route('/home')
def home():
    return "this is home page"
@a.route('/about')
def aboutus():
    return "this is about page"
@a.route('/contact')
def contact():
    return render_template('contact.html')
a.run()
