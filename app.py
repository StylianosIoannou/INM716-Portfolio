from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('Homepage.html')

# About Page
@app.route('/about')
def about():
    return render_template('About.html')

# Sales Page
@app.route('/sales')
def sales():
    return render_template('Sales.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('Contact.html')

# Portfolio Pages
@app.route('/portfolio')
def portfolio():
    return render_template('Portfolio.html')

@app.route('/portfolio2')
def portfolio2():
    return render_template('portfolio2.html')

@app.route('/portfolio3')
def portfolio3():
    return render_template('portfolio3.html')

if __name__ == '__main__':
    app.run(debug=True)
