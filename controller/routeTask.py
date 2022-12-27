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
    nombre = request.json["nombre"]
    fecha = request.json["fecha"]
    completada = request.json["completada"]
    descripcion = request.json["descripcion"]
    
    task = Task(nombre, fecha, completada, descripcion = descripcion)
    repository.create(task)
    return "", 201
    
@app.route('/api/tasks/<id>', methods=['PUT'])
def update(id):
    id = id
    nombre = request.json["nombre"]
    fecha = request.json["fecha"]
    completada = request.json["completada"]
    descripcion = request.json["descripcion"]
    
    task = Task(id, nombre, fecha, completada, descripcion = descripcion)
    repository.update(task)
    
@app.route('/api/tasks/<id>', methods=['DELETE'])
def delete(id):
    repository.delete(id)