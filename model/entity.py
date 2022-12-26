class Task:
    def __init__(self, nombre, completada, fecha, id = None, descripcion = None) -> None:
        self.nombre = nombre
        self.completada = completada
        self.fecha = fecha
        self.id = id
        self.descripcion = descripcion