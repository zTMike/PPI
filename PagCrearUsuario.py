from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox, QComboBox
from PyQt5 import QtCore
import datetime
from DatosPQRS import PQRS
from DatosCliente import Clientes
from DatosVehiculo import Vehiculos
import Ayudas


class VentanaCu(QMainWindow):
    def __init__(self, anterior):
        super().__init__()
        self.vetanaAnterior = anterior
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

        self.exp2 = QAction(QIcon("imagenes/minimizar.png"), "Minimizar", self)
        self.barraHerramientas.addAction(self.exp2)

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
        self.letrero1.setText("Crear Usuarios\nNuevos")


        self.letrero1.setFont(QFont("league spartan", 29))
        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background: rgba(76, 175, 80, 0.0); font-weight: bold; margin-bottom:15px;margin-top:50px;")
        self.formulario.addRow(self.letrero1)


        #linea Pendiente intentar realizar
        self.letrero2 = QLabel()
        self.letrero2.setText("                                                                                    ")
        self.letrero1.setFont(QFont("league spartan", 35))
        self.letrero2.setStyleSheet("background: rgba(76, 175, 80, 0.0);color:#EFE718; margin-left:240px;text-decoration: underline ;")
        self.formulario.addRow(self.letrero2)




        # Caja de modulos #1

        #Texto informativo Id PQRS
        self.idpqrs = QLabel("Usuario: ")
        self.idpqrs.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold;margin-top:50px;")
        self.idpqrs.setFont(QFont("league spartan", 12))



        # Entrada de dato cedula
        self.idpqrsText = QLineEdit()
        self.idpqrsText.setFixedWidth(260)
        self.idpqrsText.setFont(QFont("league spartan", 10))
        self.idpqrsText.setPlaceholderText("Usuario")
        self.idpqrsText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold; margin-top:50px;")
        self.formulario.addRow(self.idpqrs, self.idpqrsText)


        # Caja de modulos #2

        # Texto informativo cedula
        self.cedula = QLabel("Contraseña: ")
        self.cedula.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.cedula.setFont(QFont("league spartan", 12))

        # Entrada de dato cedula
        self.cedulaText = QLineEdit()
        self.cedulaText.setFixedWidth(260)
        self.cedulaText.setFont(QFont("league spartan", 10))
        self.cedulaText.setPlaceholderText("Contraseña")
        self.cedulaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.cedula, self.cedulaText)







        # Caja de modulos #8
        # Texto informativo fecha Respuesta

        self.estado = QLabel("Tipo de usuario: ")
        self.estado.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.estado.setFont(QFont("league spartan", 12))

        # Entrada de dato Fecha respuesta

        self.estadoText = QComboBox()
        self.estadoText.addItem("Administrador")
        self.estadoText.addItem("Basico")
        self.estadoText.setFixedWidth(260)
        self.estadoText.setFont(QFont("league spartan", 10))
        self.estadoText.setPlaceholderText("Solucionado o pendiente")
        self.estadoText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.estado, self.estadoText)

        # Caja de modulos #9
        # Texto informativo estado de la pqr



        #Linea Separadora
        self.formulario.addRow(self.letrero2)

        self.botonGuardar = QPushButton("Guardar")
        self.botonGuardar.setFixedWidth(170)
        self.formulario.addWidget(self.botonGuardar)
        self.botonGuardar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonConsultar = QPushButton("Consultar")
        self.botonConsultar.setFixedWidth(170)
        self.formulario.addWidget(self.botonConsultar)
        self.botonConsultar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonactualizar = QPushButton("Actualizar")
        self.botonactualizar.setFixedWidth(170)
        self.formulario.addWidget(self.botonactualizar)
        self.botonactualizar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                           "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botoneliminar = QPushButton("Eliminar")
        self.botoneliminar.setFixedWidth(170)
        self.formulario.addWidget(self.botoneliminar)
        self.botoneliminar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                           "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonlimpiar = QPushButton("Limpiar")
        self.botonlimpiar.setFixedWidth(170)
        self.formulario.addWidget(self.botonlimpiar)
        self.botonlimpiar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")



        self.botonGuardar.clicked.connect(self.accion_botonGuardar)

        self.botonGuardar.clicked.connect(self.accion_botonGuardar)

        self.botonConsultar.clicked.connect(self.accion_botonConsultar)

        self.botonactualizar.clicked.connect(self.accion_botonactualizar)

        self.botoneliminar.clicked.connect(self.accion_botoneliminar)



        self.fondo.setLayout(self.formulario)

        # ________________Ventana emergente___________
        # creamos ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # asignamos tama;o a la ventana de dailogo

        self.vdancho = 300
        self.vdalto = 150

        self.ventanaDialogo.resize(self.vdancho, self.vdalto)
        # Para que las ventanas no se puedan estirar o mover
        # Width= Ancho
        self.ventanaDialogo.setFixedWidth(self.vdancho)
        # Height= Alto
        self.ventanaDialogo.setFixedHeight(self.vdalto)

        # Creamos el boton aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)
        # Establecemos titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Guardar datos")

        # Configuramos que la ventana sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)
        self.ventanaDialogo.setWindowIcon(QIcon("imagenes/IconoGPP.jpeg"))

        # Creamos layout vertical
        self.vertical = QVBoxLayout()

        # Creamos en label para los mensajes
        self.mensaje = QLabel("")

        # agregamos mensajes al vertical
        self.vertical.addWidget(self.mensaje)

        # agregamos Boton al vertical
        self.vertical.addWidget(self.opciones)

        # asigna layout a la ventana
        self.ventanaDialogo.setLayout(self.vertical)





    def accion_botonlimpiar(self):
        """self.idpqrsText.setText("")
        self.cedulaText.setText("")
        self.placaText.setText("")
        self.estadoText.setCurrentIndex(0)
        self.fechacierreText.setText(datetime.date.today().strftime("%d/%m/%Y"))  # para mostrar la fecha actual
        self.descripcionrText.setText("")
        self.fechaText.setText(datetime.date.today().strftime("%d/%m/%Y"))  # para mostrar la fecha actual
        self.consecutivo_iniciarl()
        self.idpqrsText.setReadOnly(False)
        self.cedulaText.setReadOnly(False)
        self.placaText.setReadOnly(False)
        self.fechacierreText.setReadOnly(False)
        self.descripcionrText.setReadOnly(False)
        self.fechaText.setReadOnly(False)"""


    def accion_botonGuardar(self):
        pass
    def accion_botonConsultar(self):
        pass
    def accion_botonactualizar(self):
        pass
    def accion_botoneliminar(self):
        pass
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
            self.vetanaAnterior.show()







