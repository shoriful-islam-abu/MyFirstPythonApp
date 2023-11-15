from flask import Flask, render_template

app = Flask(__name__)

content = [
  {
    'id': '1000',
    'name': 'Mahmud Akhter',
    'position': 'Human Resources'
  },
  {
    'id': '1001',
    'name': 'Tahmina Rahman',
    'position': 'Network Administration'
  },
  {
    'id': '1002',
    'name': 'John Maritt',
    'position': 'Develpoment'
  },
  {
    'id': '1003',
    'name': 'John Maritt',
    'position': 'Software Architecture'
  },
  {
    'id': '1004',
    'name': 'Conner Ardin',
    'position': 'Human Resources'
  }
]

@app.route("/")
def hello():
  return render_template('index.html', contacts=content)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
