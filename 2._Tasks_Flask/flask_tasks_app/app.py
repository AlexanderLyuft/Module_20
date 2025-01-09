from flask import Flask, jsonify, request

app = Flask(__name__)

# Список для хранения задач
tasks = []

# Получение списка задач
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Добавление новой задачи
@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.get_json()  # Получение данных задачи из запроса
    tasks.append(task)          # Добавление задачи в список
    return jsonify(task), 201   # Возврат добавленной задачи и кода 201 (создано)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Tasks API!"})

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)



# python app.py - запуск приложения