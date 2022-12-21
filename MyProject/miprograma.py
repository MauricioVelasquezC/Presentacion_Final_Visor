from flask import Flask, render_template, request, redirect, url_for 
from coordenada import coordenada
from db import db

class Programa:
    def __init__(self):
        
        self.app=Flask(__name__)
        
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///coordenada.sqlite3"
        
        db.init_app(self.app)
        
        self.app.add_url_rule('/', view_func=self.buscarCoordenadas)
        self.app.add_url_rule('/index', view_func=self.agregar, methods=["GET","POST"])
        
        with self.app.app_context():
            db.create_all()
            
        
        self.app.run(debug=True)

    def buscarCoordenadas(self):
       return render_template('index.html')
    
    def agregar(self):
        
        if request.method=="POST":
            nombre=request.form['nombre']
            latitud=request.form['latitud']
            longitud=request.form['longitud']
            
            micoordenada=coordenada(nombre, latitud, longitud)
            
            db.session.add(micoordenada)
            db.session.commit()
            
        return redirect(url_for('buscarCoordenadas'))    
            
        

miProgrma=Programa()