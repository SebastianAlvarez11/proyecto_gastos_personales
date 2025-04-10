from src.model.aplicacion import Aplicacion
from view.consolaPrueba import ConsolaPrueba
from view.consola import Consola
from controlador.app_controlador import AppControlador

#if __name__ == "__main__":
#    app_controlador: AppControlador = AppControlador()
#    Consola(app_controlador).ejecutar()


if __name__ == '__main__':
    aplicacion = Aplicacion() 
    consola = Consola(aplicacion) 
    consola.ejecutar()