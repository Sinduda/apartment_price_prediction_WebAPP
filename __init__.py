from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# ML 모델 가져오기
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/')
def home():
    X_test = [[90, 2002, 6]]
    y_pred = model.predict(X_test)
    return f"예측 가격 = {round(y_pred[0][0])} 만원"

if __name__ == "__main__":
    app.run(debug=True)
