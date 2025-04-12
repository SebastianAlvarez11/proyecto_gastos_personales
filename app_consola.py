from src.view.consola.consola import Consola
from src.controlador.app_controlador import AppControlador

if __name__ == "__main__":
    app_controlador: AppControlador = AppControlador()
    Consola(app_controlador).ejecutar()
