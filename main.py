from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add route for flight planning functionality
@app.route('/plan-flight', methods=['POST'])
def plan_flight():
    # Get form data
    departure_airport = request.form['departure_airport']
    arrival_airport = request.form['arrival_airport']
    # Add more functionality as needed
    return "Flight planned successfully! Departure: {}, Arrival: {}".format(departure_airport, arrival_airport)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
