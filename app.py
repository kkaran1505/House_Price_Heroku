from flask import Flask,render_template,request
import joblib
import warnings
warnings.filterwarnings('ignore')

app=Flask(__name__)

@app.route('/')

def base():
    return render_template('home.html')

@app.route('/gallary')

def galary():
    return render_template('gallary.html')

@app.route('/cart')

def cart():
    return 'Welcome to Cart Page'

@app.route('/contact')

def contact():
    return 'Welcome to Contact Page'

@app.route('/setting')

def setting():
    return 'Welcome to Setting Page'

@app.route('/predict', methods=['post'])

def predict():
    model=joblib.load('income_pred.pkl')
    yer=request.form.get('number')
    

    #print(yer)
    output=model.predict([[int(yer)]])
    #print(output)
    

    return  render_template('predict.html',data=output)

if __name__='__main__':
    app.run(debug=True)

