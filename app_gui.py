from src.view.gui.gui import GastosPersonalesApp
from src.controlador.app_controlador import AppControlador

if __name__ == '__main__':
    app_controlador: AppControlador = AppControlador()
    GastosPersonalesApp(app_controlador).run()