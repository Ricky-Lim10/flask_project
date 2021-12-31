from flask import Flask, jsonify,request
app = Flask(__name__)

tasks= [
    {
        'contact': 8582761819,
        'name': 'Ricky',
        'id':1,
        'done':False,
    },
    {
        'contact':8580921915,
        'name': 'Aiden',
        'id':2,
        'done':False,
    },
]
@app.route('/add-contact',methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        }, 400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
if (__name__ == "__main__"):
    app.run(debug=True)
