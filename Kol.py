from flask import Flask, render_template, url_for

app = Flask(__name__)

lessons = [{
    'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'Omar',
    'thumbnail': 'thumbnail.jpg'
},
]

categories = [
    {
        'name': 'Electronics',
        'icon': 'electronic.jpg',
        'description': 'Top-notch gadgets for all your tech needs.'
    },

    {
        'name': 'Home & Kitchen',
        'icon': 'analysis.png',
        'description': 'Stylish decor and kitchen essentials.'
    },

    {
        'name': 'Fashion & Apparel',
        'icon': 'machine-learning.png',
        'description': 'Trendy clothing and accessories.'
    },

    {
        'name': 'Health & Beauty',
        'icon': 'web.png',
        'description': 'Beauty and wellness products for you.'
    },

    {
        'name': 'Sports & Outdoors',
        'icon': 'blockchain.png',
        'description': 'Gear for active lifestyles and adventures.'
    },

    {
        'name': 'Toys & Games',
        'icon': 'idea.png',
        'description': 'Fun and educational toys for all ages.'
    },

]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', lessons=lessons, categories=categories)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__=="__main__":
    app.run(debug=True)