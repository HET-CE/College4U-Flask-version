from flask import Flask,send_from_directory,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tutorials")
def tutorials():
    return render_template("tutorials.html")

@app.route("/about-team-members")
def about():
    return render_template("about.html")

@app.route("/pdf")
def pdf():
    return render_template("pdf.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")    

app.config['UPLOAD_LOC'] = 'uploads/client/'

@app.route('/uploads/client/<path:filename>')
def send_attachment(filename):
    # return app.config['UPLOAD_LOC'] + filename
    return send_from_directory(
        app.config['UPLOAD_LOC'],filename,as_attachment=True
    )

app.run(debug=True)