from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import csv
from cafe_form import CafeForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location = form.location.data
        open_ = dict(form.open.choices).get(form.open.data)
        close = dict(form.close.choices).get(form.close.data)
        coffee = dict(form.coffee.choices).get(form.coffee.data)
        wifi = dict(form.wifi.choices).get(form.wifi.data)
        power = dict(form.power.choices).get(form.power.data)
        new_cafe = f"{cafe},{location} ,{open_},{close},{coffee},{wifi},{power}"
        print(new_cafe)
        try:
            with open('cafe-data.csv', mode="a", encoding='utf-8') as file:
                file.write(f"\n{new_cafe}")
        except:
            return render_template('add.html', form=form, message="❌Couldn't add your cafe, please try again.")
        else:
            return redirect(url_for('cafes'))

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form, message="")


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
