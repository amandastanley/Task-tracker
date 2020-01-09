from flask import Flask
from flask import jsonify
import json
from flask import request

app = Flask(__name__, static_folder='.')

@app.route('/test/json')
def testJson ():
  return jsonify(
    {
      "items": [
        {"duedate":"",
        'task':"",
        'budget':""}
      ]
    }
  )
  

@app.route('/static/<fn>')
def sstatic (fn):
    return app.send_static_file('./static/'+fn)

@app.route('/')
def index ():
  return app.send_static_file('./static/index.html')

@app.route('/addtask', methods=['POST'])
def addtask():
  task = request.form.get('task')
  duedate = request.form.get('duedate')
  budget = request.form.get('budget')
  return jsonify(
    additem({
      'task':task,
      'duedate':duedate,
      'budget':budget,
    }))
  return 'python says \n' + request.form.get('task')+'\n' + request.form.get('duedate')+'\n' + request.form.get('budget')+'\n'

data = {}
data['items'] = []
def testthing():
  data['items'].append({
      '1': 'Scott',
      'duedate': 'stackabuse.com',
      'budget': 'Nebraska'
  })
  data['items'].append({
      '2': 'Larry',
      'duedate': 'google.com',
      'budget': 'Michigan'
  })
  data['items'].append({
      '3': 'Tim',
      'duedate': 'apple.com',
      'budget': 'Alabama'
  })

with open('tasks.txt', 'w') as outfile:
    json.dump(data, outfile)  

def additem(task):
  data['items'].append(task)
  with open('tasks.txt', 'w') as outfile:
    json.dump(data, outfile)
  return data 

def test():
  additem('meh')
  assert(data['items']==['meh'])
  additem('bop')
print(data)
#assert(chart['items']==['meh','bop'])
with open('tasks.txt', 'w') as outfile:
    json.dump(data, outfile)
#test()
app.run()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
