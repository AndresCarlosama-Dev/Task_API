from flask import request
from aplication import app
from model.entity import Task
from model.repository import taskRepository

repository = taskRepository()

@app.route('/api/tasks', methods=['GET'])
def read():
    return repository.read()

@app.route('/api/tasks/<id>', methods=['GET'])
def readOne(id):
    return repository.readOne(id)

@app.route('/api/tasks', methods=['POST'])
def create():
    # nombre = request.json["nombre"]
    # descripcion = request.json["descripcion"]
    # completada = request.json["completada"]
    
    task = Task()
    repository.create()
    
@app.route('/api/tasks/<id>', methods=['PUT'])
def update(id):
    # nombre = request.json["nombre"]
    # descripcion = request.json["descripcion"]
    # completada = request.json["completada"]
    
    task = Task()
    repository.update(task)
    
@app.route('/api/tasks/<id>', methods=['DELETE'])
def delete(id):
    repository.delete(id)