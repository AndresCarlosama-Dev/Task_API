import json
from model.entity import Task
from database.conexion import mysql

class taskRepository:
    def read(self) -> list:
        sql = """
            SELECT *
            FROM tasks
        """
        
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        tareas = cursor.fetchall()
        cursor.close()
        
        mostrarTareas = list() #Lista de objetos Task
        for tarea in tareas:
            mostrarTareas.append(Task(
                id = tarea[0],
                nombre = tarea[1],
                fecha = tarea[2],
                completada = tarea[4],
                descripcion = tarea[3]))
        
        jsonTask = list() #Lista de json/dict
        for objDicc in mostrarTareas:
            jsonTask.append(objDicc.__dict__)
        
        return jsonTask
            
       
    def readOne(self, id: int) -> Task:
        sql = f"""
            SELECT * 
            FROM tasks
            WHERE id = {id}
        """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        tarea = cursor.fetchone()
        cursor.close()
        
        if tarea == None:
            raise Exception(f"No se encontro ninguna tarea con el id {id}")
        
        objTarea = (Task(
            id = tarea[0],
            nombre = tarea[1],
            fecha = tarea[2],
            completada = tarea[4],
            descripcion = tarea[3]))
        
        return objTarea.__dict__
        
        
    def create(self, task:Task) -> None:
        sql = f"""
            INSERT INTO tasks (nombre, fecha, descripcion, completada)
            VALUES ('{task.nombre}', {task.fecha}, '{task.descripcion}', {task.completada})
        """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()
    
    
    def update(self, task: Task) -> None:
        sql = f"""
            UPDATE tasks
            SET nombre = '{task.nombre}',
                fecha = {task.fecha},
                descripcion = '{task.descripcion}',
                completada = {task.completada}
            WHERE id = {task.id};
        """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        tareaUpdate = cursor.rowcount
        mysql.connection.commit()
        cursor.close()
        print(tareaUpdate)
        
        if tareaUpdate == 0:
            raise Exception(f"No se ha podido actualizar la tarea con el id {task.id}")
        
        
    def delete(self, id: int) -> None:    
        sql = f"""
            DELETE
            FROM tasks
            WHERE id = {id};
        """

        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()