from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route("/")
def index():
    # Get all PNG files in the static folder
    png_files = [f for f in os.listdir('static') if f.endswith('.png')]
    
    # Select a random PNG file
    random_file = random.choice(png_files)
    
    # Render the index.html template with the random PNG file
    return render_template('index.html', random_png=random_file)

if __name__ == "__main__":
    app.run(debug=True)
