from src.model.aplicacion import Aplicacion
from view.consola import Consola

if __name__ == "__main__":
    aplicacion = Aplicacion() 
    consola = Consola(aplicacion) 
    consola.ejecutar()