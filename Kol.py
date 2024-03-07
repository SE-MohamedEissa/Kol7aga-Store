from flask import Flask, render_template, url_for, flash, redirect
from Form import RegisterForm, LoginForm
import random

app = Flask(__name__)
app.config['SECRET_KEY'] ='4e8e3595fc5ed95b4a9d7160affe958829d6bd2c35deca446d6b5a260c23bff9'


categories = [
    {
        'name': 'Electronic Devices',
        'icon': 'devices.jpg',
        'description': 'Upgrade your computing experience with the latest computer hardware essentials. From powerful processors and graphics cards to high-speed memory modules, find the components you need to enhance your system performance and capabilities'
    },

    {
        'name': 'Home & Kitchen',
        'icon': 'kit.jpg',
        'description': 'Transform your living space with our diverse collection of home and kitchen essentials. Discover stylish decor, functional appliances, and innovative gadgets that make daily chores a breeze. Elevate your home environment with our curated selection of quality product'
    },

    {
        'name': 'Bags',
        'icon': 'bages.jpg',
        'description': 'Stay connected and in style with our range of cutting-edge smartphones. Explore the latest models boasting advanced features, stunning cameras, and powerful processors. Find the perfect device to suit your lifestyle and stay ahead in the fast-paced world of mobile technology.'
    },

    {
        'name': 'Clothes',
        'icon': 'clothes.jpg',
        'description': 'Dive into the world of electronic hardware innovation. Whether you are a DIY enthusiast or a professional, our collection includes a variety of electronic components and tools. From circuit boards to connectors, we have got what you need to bring your electronic projects to life'
    },

    {
        'name': 'Books',
        'icon': 'book.jpg',
        'description': 'Immerse yourself in captivating stories and knowledge with our diverse collection of books. From gripping novels to insightful non-fiction, our library offers a literary journey for every reader. Explore new worlds, gain fresh perspectives, and let the magic of words transport you.'
    },

    {
        'name': 'Toys & Games',
        'icon': 'toys.jpg',
        'description': 'Spark joy and creativity with our delightful range of toys for all ages. From educational playsets that enhance learning to whimsical toys that inspire imagination, our collection brings smiles to little faces. Discover a world of play where fun meets development, and let the adventure begin with our carefully curated selection of toys'
    }

]
Founders = [
    {
        'name':'Reem Mohsen',
        'image':'Reem1.jpeg',
    },

    {
        'name':'Mohamed Eissa',
        'image':'Mohamed.jpg',
    },

    {
        'name':'Mahmod Morad',
        'image':'mahmod.jpg',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title = "Home", categories=categories)

@app.route("/about")
def about():
    return render_template('about.html', title="About", founders = Founders)

@app.route("/register",methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("home"))
    return render_template('register.html', title="Register", random = random.random(), form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if((form.email.data == "mohamed@gmail.com" and form.password.data == "Mohamed123!?") or (form.email.data == "mahmod@gmail.com" and form.password.data == "Mahmod123!?") or (form.email.data == "reem@gmail.com" and form.password.data == "Reem123!?")):
            return redirect(url_for("home"))
    return render_template('login.html', title="Login", random = random.random(), form=form)

if __name__=="__main__":
    app.run(debug=True)