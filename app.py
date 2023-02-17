from flask import Flask, render_template, request

import pickle
model = pickle.load(open('./model/modelo.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    alert = 0
    return render_template('home.html', alert=alert)


@app.route('/result', methods=['GET', 'POST'])
def result():
    alert = 1
    
    if request.method == 'POST':
        Area = float(request.form.get('Area'))
        MajorAxisLength = float(request.form.get('MajorAxisLength'))        
        MinorAxisLength = float(request.form.get('MinorAxisLength'))
        Eccentricity = float(request.form.get('Eccentricity'))
        ConvexArea = float(request.form.get('ConvexArea'))
        EquivDiameter = float(request.form.get('EquivDiameter'))
        Extent = float(request.form.get('Extent'))
        Perimeter = float(request.form.get('Perimeter'))
        Roundness = float(request.form.get('Roundness'))
        AspectRation = float(request.form.get('AspectRation'))
        
        predict = model.predict([[
            Area,
            MajorAxisLength,
            MinorAxisLength,
            Eccentricity,
            ConvexArea,
            EquivDiameter,
            Extent,
            Perimeter,
            Roundness,
            AspectRation
        ]])
        
        result = predict[0]
        
    return render_template('home.html', alert=alert, result=result)

if __name__ == "__main__":
    app.run()
