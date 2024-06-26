from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
      {'id': 1,
       'title': 'data analyst',
       'location': 'Bengaluru, India',
       'salary': 'Rs. 10,00,000'},
      {'id': 2,
       'title': 'data analyst',
       'location': 'Kasargod',
       'salary': 'Rs. 15,00,000'},
      {'id': 3,
       'title': 'frontend engineer',
       'location': 'Kasargod',
       'salary': 'Rs. 11,00,000'},
      {'id': 4,
       'title': 'backend engineer',
       'location': 'Ernakulam',
       'salary': 'Rs. 1,00,000'}
  ]


@app.route("/")
def hello_world():
      return render_template('home.html', jobs=JOBS)
  
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
      app.run(host='0.0.0.0', debug=True)
