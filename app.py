from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Task cannot be empty'})

if __name__ == '__main__':
    app.run(debug=True)
