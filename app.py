from flask import Flask, render_template, request
import pickle
import numpy

app = Flask(__name__)

def AirbnbPricePredictor(user_inputs):
    predict_input = numpy.array(user_inputs).reshape(1,3)
    model = pickle.load(open('ml_model.pkl','rb'))
    predicted_price = model.predict(predict_input)
    return predicted_price[0]

@app.route('/owner')
def owner():
    return "Phuong Pham"

@app.route('/')
def index():  # put application's code here
    return render_template('main.html')

@app.route('/price', methods = ['POST'])
def result():
    if request.method == 'POST':
        user_inputs = list(request.form.to_dict().values())
        user_inputs = [float(i) for i in user_inputs]
        predicted_price = AirbnbPricePredictor(user_inputs)
    return render_template('price.html', prediction=str(predicted_price))


if __name__ == '__main__':
    app.run(debug=True)
