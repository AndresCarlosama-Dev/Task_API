from flask import request
from aplication import app
from model.entity import Task
from model.repository import taskRepository
from controller.response.api import ApiResponse

repository = taskRepository()

@app.route('/api/tasks', methods=['GET'])
def read():
    response = repository.read() #Lista de json/dict
    api = ApiResponse(data = response)
    return api.toMsj(), 200 #Se introduce "api" en el metodo toMsj()

@app.route('/api/tasks/<id>', methods=['GET'])
def readOne(id):
    api = None
    status = 200
    try:
        response = repository.readOne(id) #json/dict
        api = ApiResponse(data = response)
        
    except Exception as ex:
        status = 400
        api = ApiResponse(message = "Error " + str(ex))
        
    return api.toMsj(), status
        

@app.route('/api/tasks', methods=['POST'])
def create():
    api = None
    status = 200
    try:
        nombre = request.json["nombre"]
        fecha = request.json["fecha"]
        completada = request.json["completada"]
        descripcion = request.json["descripcion"]
        
        task = Task(nombre, fecha, completada, descripcion = descripcion)
        repository.create(task)
        
        api = ApiResponse(data = True)
        
    except Exception as ex:
        status = 400
        api = ApiResponse(message = "Error " + str(ex))
        
    return api.toMsj(), status
    
    
@app.route('/api/tasks/<id>', methods=['PUT'])
def update(id):
    api = None
    status = 200
    try:
        id = id
        nombre = request.json["nombre"]
        fecha = request.json["fecha"]
        completada = request.json["completada"]
        descripcion = request.json["descripcion"]
    
        task = Task(nombre, fecha, completada, descripcion = descripcion, id = id)
        repository.update(task)

        api = ApiResponse(data = True)
        
    except Exception as ex:
        status = 400
        api = ApiResponse(message = "Error " + str(ex))
        
    return api.toMsj(), status
    
   
@app.route('/api/tasks/<id>', methods=['DELETE'])
def delete(id):
    api = None
    status = 200
    try:
        repository.delete(id)
        
        api = ApiResponse(data = True)
    
    except Exception as ex:
        status = 400
        api = ApiResponse(message = "Error " + str(ex))
        
    return api.toMsj(), status   