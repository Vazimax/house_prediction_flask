from flask import Flask, render_template, request
import pickle

app = Flask(__name__) 

@app.route('/')
def index():

    return render_template("home.html")

model = pickle.load(open('model.pkl','rb'))
@app.route('/predict',methods=['GET','POST'])
def predict():
    Area_Income = float(request.form.get('income'))
    Area_House_Age = float(request.form.get('age'))
    Area_Rooms = float(request.form.get('rooms'))
    Area_Bed_Rooms = float(request.form.get('bed_rooms'))
    Area_Population = float(request.form.get('population'))
    prediction = model.predict([[Area_Income,Area_House_Age, Area_Rooms,Area_Bed_Rooms,Area_Population]])
    output = round(prediction[0],2)
    return render_template("home.html",text=f"The Predicted Price is {output}")


if __name__ == '__main__':
    app.run(debug=True)