from flask import *

from weathergrabber import WeatherGrabber

import sys

wg = WeatherGrabber()

app = Flask(__name__)

months = { 1:"January",
           2:"February",
           3:"March",
           4:"April",
           5:"May",
           6:"June",
           7:"July",
           8:"August",
           9:"September",
           10:"October",
           11:"November",
           12:"December"}


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks/<int:year_id>/<int:month_id>/<int:day_id>', methods=['POST', 'GET'])
def DoStuff(year_id, month_id, day_id):
    task_list = ("a", "b")#[task for task in tasks if task['id'] == task_id]
    
    # Probably validation
    if len(task_list) == 0:
        abort(404)
    if not request.json:
        abort(400)
    #if 'title' in request.json and type(request.json['title']) != unicode:
        #abort(400)
    """if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)"""

    dataToSend = 0

    sys.stderr.write("{}-{}-{}\n".format(year_id, month_id, day_id))

    title = request.json['title']


    for i in range(-3, 4):
        tempData = GetData(month = month_id, day=day_id+i, year=year_id)
        if tempData == '':
            tempData = '1'
        dataToSend += float(tempData)

    dataToSend /= 7;
        
    sys.stderr.write("->{}\n".format(dataToSend))
    
    sys.stderr.write("-->{}\n".format(int(round(dataToSend))))
    return str(int(round(dataToSend)))

def GetData(month, day, year = "1979"):
    avg_precip = wg.GetData("{}-{}-{}".format(year, month, day))
    if avg_precip > .25:
        #return '{"rainfall":"1"}'
        return '1'
    else:
        #return '{"rainfall":"0"}'
        return '0'
    
    #return "month: {}   day: {}".format(months[month_id], str(day_id))

def function1(title):
    return "Buy Groceries" + title

def function2():
    return "Learn Python"
"""
@app.route('/todo/api/v1.0/tasks/<int:year_id>/<int:month_id>/<int:day_id>', methods=['OPTIONS'])
def AllowPost(year_id, month_id, day_id):
    return make_response(jsonify({'Allow' : 'POST' }, 200, \
    { 'Access-Control-Allow-Origin': '*', \
      'Access-Control-Allow-Methods' : 'PUT,GET,POST' }))
"""
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response    
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/')
def index():
    return "Hello, World"
    
if "__main__" == __name__:
    app.run(host="10.105.202.143", debug=True)
