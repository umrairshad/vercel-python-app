from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# with open('q-vercel-python.json','r') as file:
#     # print(,"Faizan")
#     data=file.read()

import json

with open('q-vercel-python.json', 'r') as file:
    data = json.load(file)  # Parse JSON content
 
    

def filter_marks(data,names):
    marks=[]
    
    for student in data:
        if student["name"]==names[0] or student["name"]==names[1]:
            marks.append(student["marks"])
       
    return marks
# Mock data for marks
marks_data = {
    "X": 10,
    "Y": 20,
    "Z": 30
}

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get all 'name' query parameters

    return jsonify({"marks": filter_marks(data,names)})

if __name__ == '__main__':
    app.run(debug=True)