from flask import Flask, render_template, request
import pickle
import numpy as np

# ML 모델 가져오기
model = pickle.load(open('flask_app/model.pkl', 'rb'))

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html')

    @app.route('/predict', methods = ['POST'])
    def predict():
        data1 = (int(request.form['a']) * 3.305785) #평수를 m^2로 변환. 사람들한텐 평수가 더 편하니까.
        data2 = (2022 - int(request.form['b'])) # 완공년도 = 현재년도 - 연식(input)
        data3 = int(request.form['c'])
        X_test = [[data1, data2, data3]]
        y_pred = model.predict(X_test)
        
        sundae_p = round((round(y_pred[0][0])*10000) / 6000)
        coffee_p = round((round(y_pred[0][0])*10000) / 3000)
        hamb_p = round((round(y_pred[0][0])*10000) / 5900)

        return render_template('predict.html', data=round(y_pred[0][0]), sundae=sundae_p, coffee=coffee_p, hamb=hamb_p)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)