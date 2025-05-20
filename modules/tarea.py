class Tarea:
    def __init__(self, titulo, fecha):
        self.titulo = titulo
        self.fecha = fecha

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "fecha": self.fecha
        }

    @staticmethod
    def from_dict(data):
        return Tarea(data["titulo"], data["fecha"])
