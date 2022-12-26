from model.entity import Task
from database.conexion import execute, commit

class taskRepository:
    def read(self) -> list:
        sql = """
            SELECT * 
            FROM task_api
        """
        print (sql)
        cursor = execute(sql)
        tareas = cursor.fetchall()
        cursor.close()
        
        mostrarTareas = list()
        for tarea in tareas:
            mostrarTareas.append(Task(
                nombre = tarea[1],
                completada = tarea[4],
                id = tarea[0],
                fecha = tarea[2],
                descripcion = tarea[3]))
        return mostrarTareas
          
       
    def readOne(self, id: int) -> Task:
        sql = f"""
            SELECT * 
            FROM task_api
            WHERE id = {id}
        """
        cursor = execute(sql)
        tarea = cursor.fetchone()
        cursor.close()
        
        return tarea        
        
        
    def create(self, task:Task) -> None:
        sql = f"""
            INSERT INTO task_api (nombre, fecha, descripcion, completada)
            VALUES ('{task.nombre}', {task.fecha}, '{task.descripcion}', {task.completada})
        """
        cursor = cursor.execute(sql)
        commit()
        cursor.close()
    
    
    def update(self, task: Task) -> None:
        sql = f"""
            UPDATE task_api
            SET nombre = '{task.nombre}',
            completada = '{task.completada},
            fecha = {task.fecha}
            descripcion = '{task.descripcion}'
            WHERE id = {task.id}
        """
        cursor = cursor.execute(sql)
        commit()
        cursor.close()
        
        
    def delete(id: int) -> None:
        sql = f"""
            DELETE
            FROM task_api
            WHERE id = {id}
        """
        cursor = cursor.execute(sql)
        commit()
        cursor.close()