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

    # @app.route('/predict', methods = ['POST'])
    # def predict():
    #     data1 = request.form['a']
    #     data2 = request.form['b']
    #     data3 = request.form['c']
    #     arr = np.array([[data1, data2, data3]])
    #     pred = model.predict(arr)
    #     return f"예측 가격 = {round(pred[0][0])} 만원"
    #     #return render_template('predict.html', data=pred)

    @app.route('/predict', methods = ['POST'])
    def predict():
        X_test = [[90, 2002, 6]]
        y_pred = model.predict(X_test)
        return f"예측 가격 = {round(y_pred[0][0])} 만원"
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
