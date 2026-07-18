from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    products = [
        {"name": "Laptop", "category": "Electronics", "price": 800, "stock": 45},
        {"name": "Mouse", "category": "Accessories", "price": 25, "stock": 180},
        {"name": "Keyboard", "category": "Accessories", "price": 75, "stock": 5},
        {"name": "Monitor", "category": "Electronics", "price": 350, "stock": 12},
    ]

    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
