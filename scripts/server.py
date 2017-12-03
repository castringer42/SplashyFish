# MLH Local Hack Day 2017
# Tennessee Technological University group
# 2 December, 2017
# 
# Chris S, Caroline E
# Other team members: Maria, Paula B, Ethan L, 
#                     Seth D, John B, Lane S
#
# Description: Run a server that analyzes historical rainfall data to predict
#   if a day will be rainy or not.  
# 
# To use: set the IP address at the bottom of the file to your external IP or to
#   127.0.0.1 if you are only running on your computer.
#
#   Start the server by running this script
#
#   Send a 'POST' request to this server at 
#   http://YOUR_IP:5000/todo/api/v1.0/tasks/YYYY/mm/dd
#   where YYYY is the year, mm is the month, and dd is the day
#   ex: http://127.0.0.1:5000/todo/api/v1.0/tasks/1979/2/12
#       returns 1 for rain, 0 for no rain
#
# Future Work: Add actual predictions. These can be easily added to GetData
#   Clean up the leftover and unused functions.

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

# Leftovers from an example.  Remove these at some point.
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

# Process input data and send back a 1 for rain or a 0 for no rain
@app.route('/todo/api/v1.0/tasks/<int:year_id>/<int:month_id>/<int:day_id>', methods=['POST', 'GET'])
def DoStuff(year_id, month_id, day_id):
    
    # Check that the request is parsible
    if not request.json:
        abort(400)
        
    # Fill out these lines if you send data in the request and not just the URL    
    #if 'title' in request.json and type(request.json['title']) != unicode:
        #abort(400)
    """if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)"""

    dataToSend = 0

    sys.stderr.write("{}-{}-{}\n".format(year_id, month_id, day_id))

    # If you send data in the request body, retrieve it here
    title = request.json['title']

    # This section did not work for some reason.  It was trying to get a week's
    # worth of data at a time and average it to remove most gaps in the data.
    # TODO: Make it work
    # TODO: validate and fix days that lie in different months/years
    """
    for i in range(-3, 4):
        tempData = GetData(month = month_id, day=day_id+i, year=year_id)
        if tempData == '':
            tempData = '1'
        dataToSend += float(tempData)

    dataToSend /= 7;
    """
    
    dataToSend = GetData(month = month_id, day=day_id, year=year_id)
        
    sys.stderr.write("->{}\n".format(dataToSend))
    
    sys.stderr.write("-->{}\n".format(int(round(dataToSend))))
    return str(int(round(dataToSend)))

def GetData(month, day, year = "1979"):
    avg_precip = wg.GetData("{}-{}-{}".format(year, month, day))
    
    # TODO: Insert fancy computer algorithm that does learning or analysis here
    if avg_precip > .5:
        #return '{"rainfall":"1"}'
        return '1'
    else:
        #return '{"rainfall":"0"}'
        return '0'
    
    #return "month: {}   day: {}".format(months[month_id], str(day_id))

# these functions are leftovers from a flask example
def function1(title):
    return "Buy Groceries" + title

def function2():
    return "Learn Python"

# Needed to allow the html to communicate with this server.  Otherwise, the html
# sends an 'OPTIONS' request and not a 'POST' request if not allowed like this
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response    
    
# If you hit this specific part, you are connecting successfully to the server
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# unused
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# You can test your connection in your browser by going to the base website
@app.route('/')
def index():
    return "Hello, World"
    
# start the server
if "__main__" == __name__:
    app.run(host="127.0.0.1", debug=True)
