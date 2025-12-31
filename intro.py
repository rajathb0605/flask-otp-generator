import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("styling.html")

@app.route('/home/generate-4', methods=["GET", "POST"])
def fourdigit():
    otps = []

    if request.method == "POST":
        how_many = request.form.get("how_many")

        if how_many and how_many.isdigit():
            how_many = int(how_many)

            for _ in range(how_many):
                otp = "".join(str(random.randint(0, 9)) for _ in range(4))
                otps.append(otp)

    return render_template("four_digit.html", otps=otps)

@app.route('/home/generate-6', methods=["GET", "POST"])
def sixdigit():
    otps = []

    if request.method == "POST":
        how_many = request.form.get("how_many")

        if how_many and how_many.isdigit():
            how_many = int(how_many)

            for _ in range(how_many):
                otp = "".join(str(random.randint(0, 9)) for _ in range(6))
                otps.append(otp)

    return render_template("six_digit.html", otps=otps)

@app.route('/home/contact')
def contact():
    return render_template("contact.html")

@app.route('/home/donate')
def donate():
    return render_template("donote.html")  

if __name__ == "__main__":
    app.run(debug=True)
