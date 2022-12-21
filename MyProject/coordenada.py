from db import db


class coordenada(db.Model):
    
    __tablename__="coordenada"
    
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    latitud=db.Column(db.String(20))
    longitud=db.Column(db.String(20))
    
    
    def __init__(self,nombre,latitud,longitud):
        self.nombre=nombre
        self.latitud=latitud
        self.longitud=longitud