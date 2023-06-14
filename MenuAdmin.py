import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox
from PyQt5 import QtCore

import Ayudas
from PagVehiculo import VentanaRv
from PagClientes import VentanaCl
from PagEntrada import VentanaRi
from PagSalida import VentanaRs
from PagPQRS import VentanaQr
from PagConsultaIngresos import VentanaCI
from CrearUsuario import VentanaCu
from Ayudas import Ayuda





class Menu(QMainWindow):
    def __init__(self, anterior):
        super().__init__()

        self.Anterior = anterior
        self.setWindowTitle("Gesto Parqueadero")

        self.ancho = 700
        self.alto = 700

        self.resize(self.ancho, self.alto)
        # lineas para hacer que la ventana salga en el centro

        # pantalla traiga frame geometia
        self.pantalla = self.frameGeometry()

        self.setStyleSheet("background-color:white; border-color:Black;")

        # Quitar ventana de windows
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # guarde el centro en la variable centro
        self.centro = QDesktopWidget().availableGeometry().center()

        # pantalla muevete al centro
        self.pantalla.moveCenter(self.centro)

        # pantalla muvete y centrate apartir de la parte superior
        self.move(self.pantalla.topLeft())

        # Para que las ventanas no se puedan estirar o mover
        # Width= Ancho
        self.setFixedWidth(self.ancho)
        # Height= Alto
        self.setFixedHeight(self.alto)



        # crear ventana interna
        self.interna = QWidget()
        self.interna.setContentsMargins(0, 0, 0, 0)
        # definir ventana interna como ventana central
        self.setCentralWidget(self.interna)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/fondo.png')
        self.fondo.setPixmap(self.imagenFondo)
        # que la imagen se  escale o se ajuste
        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        # crear toolbar o menu
        self.barraHerramientas = QToolBar("Barra de herramientas")

        # establecer tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(40, 40))
        # agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)
        # CREAR NUEVOS ELEMENTOS PARA LA TOOLBAR

        self.exp1 = QAction(QIcon("imagenes/cerrar.png"), "Cerrar", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp1 = QAction(QIcon("imagenes/minimizar.png"), "Minimizar", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp3 = QAction(QIcon("imagenes/regresar.png"), "Regresar", self)
        self.barraHerramientas.addAction(self.exp3)

        self.barraHerramientas.setStyleSheet("background-color:#d9d9d9;")

        # que la toolbar no se mueva
        self.barraHerramientas.setMovable(False)
        # Direccion de un layout izqueirda o derecha
        self.barraHerramientas.setLayoutDirection(Qt.RightToLeft)
        # Activar Barra De herramientas
        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraDeHerramientas)

        self.formulario = QFormLayout()

        self.interna.setLayout(self.formulario)

        self.letrero1 = QLabel()
        self.letrero1.setText("Menú Administrador")

        self.letrero1.setFont(QFont("league spartan", 29))
        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background: rgba(76, 175, 80, 0.0); margin-bottom:80px; margin-top:90px;font-weight: bold")
        self.formulario.addRow(self.letrero1)

        self.letrero2 = QLabel()

        self.letrero2.setText("Modulos")

        self.letrero2.setFont(QFont("league spartan", 20))
        self.letrero2.setAlignment(Qt.AlignCenter)

        self.letrero2.setStyleSheet(
            "background: rgba(76, 175, 80, 0.0); opacity:0.6; color:black; margin-bottom:30px;font-weight: bold")
        self.formulario.addRow(self.letrero2)


        #texto antes de boton Creado 1 vez
        self.usuario = QLabel("")
        self.usuario.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:240px;font-weight: bold")
        self.usuario.setFont(QFont("league spartan", 12))

        # Caja de modulos #1
        # Boton Pestaña Registro Vehiculo
        self.botonRegistroVehiculo = QPushButton("Registro Vehículo")
        self.botonRegistroVehiculo.setFixedWidth(170)
        self.botonRegistroVehiculo.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.formulario.addRow(self.usuario, self.botonRegistroVehiculo)

        # Caja de modulos #2
        # Boton Pestaña Registro Clientes
        self.botonRegistroClientes = QPushButton("Registro Clientes")
        self.botonRegistroClientes.setFixedWidth(170)
        self.botonRegistroClientes.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.formulario.addRow(self.usuario, self.botonRegistroClientes)

        # Caja de modulos #3
        # Boton Pestaña Registro de Entrada
        self.botonRegistroEntrada = QPushButton("Registro de Entrada\n de vehículos")
        self.botonRegistroEntrada.setFixedWidth(170)
        self.botonRegistroEntrada.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.formulario.addRow(self.usuario, self.botonRegistroEntrada)

        # Caja de modulos #4
        # Boton Pestaña Registro de Salida
        self.botonRegistroSalida = QPushButton("Registro de salida\n de vehículos")
        self.botonRegistroSalida.setFixedWidth(170)
        self.botonRegistroSalida.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.formulario.addRow(self.usuario, self.botonRegistroSalida)

        # Caja de modulos #5
        # Boton Pestaña Registrar PQRS
        self.botonRegistrarPQRS = QPushButton("Registrar PQRS")
        self.botonRegistrarPQRS.setFixedWidth(170)
        self.botonRegistrarPQRS.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.formulario.addRow(self.usuario, self.botonRegistrarPQRS)

        # Caja de modulos #6
        # Boton Pestaña ver ingresos
        self.botonConsultarI = QPushButton("Consultar Ingresos")
        self.botonConsultarI.setFixedWidth(170)
        self.botonConsultarI.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                              "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.formulario.addRow(self.usuario, self.botonConsultarI)


        self.botoncrearusuario = QPushButton("Crear Usuario")
        self.botoncrearusuario.setFixedWidth(170)
        self.formulario.addWidget(self.botoncrearusuario)
        self.botoncrearusuario.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botoncrearusuario.clicked.connect(self.accion_botoncrearusuario)
        self.botonRegistroVehiculo.clicked.connect(self.accion_botonRegistroVehiculo)
        self.botonRegistroClientes.clicked.connect(self.accion_botonRegistroClientes)
        self.botonRegistroEntrada.clicked.connect(self.accion_botonRegistroEntrada)
        self.botonRegistroSalida.clicked.connect(self.accion_botonRegistroSalida)
        self.botonRegistrarPQRS.clicked.connect(self.accion_botonRegistrarPQRS)
        self.botonConsultarI.clicked.connect(self.accion_botonConsultarI)


        self.fondo.setLayout(self.formulario)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.accion_botonRegistroVehiculo()
        if event.key() == Qt.Key_F2:
            self.accion_botonRegistroClientes()
        if event.key() == Qt.Key_F3:
            self.accion_botonRegistroEntrada()
        if event.key() == Qt.Key_F4:
            self.accion_botonRegistroSalida()
        if event.key() == Qt.Key_F5:
            self.accion_botonRegistrarPQRS()
        if event.key() == Qt.Key_F6:
            self.accion_botonConsultarI()
        if event.key() == Qt.Key_Escape:
            self.accion_botonVolver()
    def accion_botonConsultarI(self):
        self.hide()
        self.ventana2 = VentanaCI(self)
        self.ventana2.show()

    def accion_botonVolver(self):
        self.hide()
        self.Anterior.show()

    def accion_botonRegistroVehiculo(self):
        self.hide()
        self.ventana2 = VentanaRv(self)
        self.ventana2.show()
    def accion_botonRegistroSalida(self):
        self.hide()
        self.ventana2 = VentanaRv(self)
        self.ventana2.show()
    def accion_botonRegistroClientes(self):
        self.hide()
        self.ventana2 = VentanaCl(self)
        self.ventana2.show()
    def accion_botonRegistroEntrada(self):
        self.hide()
        self.ventana2 = VentanaRi(self)
        self.ventana2.show()

    def accion_botonRegistroSalida(self):
        self.hide()
        self.ventana2 = VentanaRs(self)
        self.ventana2.show()
    def accion_botonRegistrarPQRS(self):
        self.hide()
        self.ventana2 = VentanaQr(self)
        self.ventana2.show()

    def accion_botoncrearusuario(self):
        self.hide()
        self.ventana2 = VentanaCu(self)
        self.ventana2.show()


    def accion_barraDeHerramientas(self, option):
        # escodase ventana

        # validar exprecion
        if option.text() == "Cerrar":
            # crar ventana interna

            self.Menu.close()
        if option.text() == "Minimizar":
            # crar ventana interna
            self.showMinimized()

        if option.text() == "Regresar":
            self.hide()
            self.Anterior.show()






