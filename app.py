from flask import Flask, request, render_template
import pickle

with open('bodyfatmodel1.pkl', 'rb') as file1:
    rf = pickle.load(file1)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        my_dict = request.form
        try:
            density = float(my_dict['density'])
            abdomen = float(my_dict['abdomen'])
            chest = float(my_dict['chest'])
            weight = float(my_dict['weight'])
            hip = float(my_dict['hip'])
        except ValueError:
            return render_template('home.html', error="Please enter valid numbers.")

        input_features = [[density, abdomen, chest, weight, hip]]

        prediction = rf.predict(input_features)[0].round(2)

        string = 'Percentage of Body Fat Estimated is : ' + str(prediction) + '%'

        return render_template('show.html', string=string)

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
