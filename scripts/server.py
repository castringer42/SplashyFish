from flask import *

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


@app.route('/todo/api/v1.0/tasks/<int:task_id>/<int:day_id>', methods=['POST'])
def DoStuff(task_id, day_id):
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

    dataToSend = ''

    title = request.json['title']

    dataToSend = GetData(task_id, day_id)

    # The task exists
    if task_id == 1:
        pass
        #dataToSend = function1(title)
        
    elif task_id == 2:
        pass
        #dataToSend = function2()
        
    return dataToSend

def GetData(month_id, day_id):
    return "month: {}   day: {}".format(months[month_id], str(day_id))

def function1(title):
    return "Buy Groceries" + title

def function2():
    return "Learn Python"


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
    app.run(debug=True)
