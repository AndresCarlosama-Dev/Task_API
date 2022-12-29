class Task:
    def __init__(self, nombre, fecha, completada, id = None, descripcion = None) -> None:
        self.nombre = nombre
        self.completada = completada
        self.fecha = fecha
        self.id = id
        self.descripcion = descripcion
        
    # def toDict(self):
    #     return{
    #         "id": self.id,
    #         "nombre": self.nombre,
    #         "fecha": self.fecha,
    #         "completada": self.completada,
    #         "descripcion": self.descripcion
    #     }
        