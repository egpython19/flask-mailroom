import os

# import the Flask class from the flask module
from flask import Flask, render_template, request, redirect, url_for, session

# import custom classes
from model import Donation, Donor

# create the application object
app = Flask(__name__)

# use decorator routing to map handler functions to URLs (jinja2 templates)
@app.route('/')
def home():
    # return all()
    return redirect(url_for('all'))


@app.route('/donations/')  # implicit GET supported
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/new/', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.jinja2')
    else:
        donor_name = request.form['name']
        donation_amount = request.form['donation']

        # Find the donor
        donor = Donor.select().where(Donor.name == donor_name).get()

        # Make a donation entry
        donation = Donation(value=donation_amount, donor=donor)
        donation.save()
        
        return redirect(url_for('all'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
