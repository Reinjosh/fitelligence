from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personal_info', methods=['POST'])
def personal_info():
    name = request.form['name']
    return render_template('personal_info.html', name=name)

@app.route('/fitness_level', methods=['POST'])
def fitness_level():
    age = request.form['age']
    weight = request.form['weight']
    height = request.form['height']
    gender = request.form['gender']
    return render_template('fitness_level.html', age=age, weight=weight, height=height, gender=gender)

@app.route('/results', methods=['POST'])
def results():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100
    bmi = round(weight / (height ** 2), 2)
    
    if bmi < 18.5:
        health_status = "Underweight"
        calorie_recommendation = "2500 calories/day"
    elif bmi < 24.9:
        health_status = "Normal weight"
        calorie_recommendation = "2000 calories/day"
    else:
        health_status = "Overweight"
        calorie_recommendation = "1800 calories/day"
        
    return render_template('results.html', bmi=bmi, health_status=health_status, calorie_recommendation=calorie_recommendation)

@app.route('/goals', methods=['POST'])
def goals():
    return render_template('goals.html')

@app.route('/plan', methods=['POST'])
def plan():
    goals = request.form['goals']
    # Dummy AI output
    workout_plan = "Workout Plan: 30 mins cardio, 30 mins strength training"
    meal_plan = "Meal Plan: Balanced diet with 2000 calories"
    return render_template('plan.html', workout_plan=workout_plan, meal_plan=meal_plan)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
