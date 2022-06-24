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

    @app.route('/predict', methods = ['POST'])
    def predict():
        data1 = (int(request.form['a']) * 3.305785) #평수를 m^2로 변환. 사람들한텐 평수가 더 편하니까.
        data2 = int(request.form['b'])
        data3 = int(request.form['c'])
        X_test = [[data1, data2, data3]]
        y_pred = model.predict(X_test)
        return render_template('predict.html', data=round(y_pred[0][0]))

    # @app.route('/predict', methods = ['POST'])
    # def predict():
    #     X_test = [[90, 2002, 6]]
    #     y_pred = model.predict(X_test)
    #     return f"예측 가격 = {round(y_pred[0][0])} 만원"
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)