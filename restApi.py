from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

diaries = [
    {
        'id': 1,
        'name': 'Kampala Diary',
        'location': 'Kampala'
    },
    {   
        'id': 2,
        'name': 'Mityana Diary',
        'location': 'Mityana'
    },
    {
        'id': 3,
        'name': 'Gulu Diary',
        'location': 'Gulu'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entries', methods=['POST'])
def create_diary():
    request_data = request.get_json()
    new_entry = {
        'name': request_data['name'],
        'items': []
    }
    diaries.append(new_entry)
    return jsonify(new_entry)

@app.route('/entries/<int:entryId>')
def get_specific_diary(entryId):
    for diary in diaries:
        if diary['id'] == entryId:
            return  jsonify(diary)
    return jsonify({'message': 'entry not found'})

@app.route('/entries') 
def get_all_diaries():
    return jsonify({'diaries': diaries})

app.run(port=5000)