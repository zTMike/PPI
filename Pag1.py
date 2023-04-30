from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox
from PyQt5 import QtCore




class VentanaRv(QMainWindow):
    def __init__(self, anterior):
        super(VentanaRv, self).__init__(anterior)
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
        self.letrero1.setText("Registro de\n Vehículos")

        self.letrero1.setFont(QFont("league spartan", 29))
        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background: rgba(76, 175, 80, 0.0); margin-bottom:50px; margin-top:30px;font-weight: bold")
        self.formulario.addRow(self.letrero1)


        #linea Pendiente intentar realizar
        self.letrero2 = QLabel()
        self.letrero2.setText("                                                                                    ")
        self.letrero1.setFont(QFont("league spartan", 35))
        self.letrero2.setStyleSheet("background: rgba(76, 175, 80, 0.0);color:#EFE718; margin-left:240px;text-decoration: underline ;")
        self.formulario.addRow(self.letrero2)




        # Caja de modulos #1

        #Texto informativo Placa
        self.placa = QLabel("Placa: ")
        self.placa.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:220px;font-weight: bold")
        self.placa.setFont(QFont("league spartan", 12))


        # Entrada de dato Placa
        self.placaText = QLineEdit()
        self.placaText.setFixedWidth(170)
        self.placaText.setFont(QFont("league spartan", 10))
        self.placaText.setPlaceholderText("Ingrese Placa")
        self.placaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.placa, self.placaText)


        # Caja de modulos #2

        #Texto informativo Modelo
        self.modelo = QLabel("Modelo: ")
        self.modelo.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:220px;font-weight: bold")
        self.modelo.setFont(QFont("league spartan", 12))

        # Entrada de dato Modelo
        self.modeloText = QLineEdit()
        self.modeloText.setFixedWidth(170)
        self.modeloText.setFont(QFont("league spartan", 10))
        self.modeloText.setPlaceholderText("Ingrese Modelo")
        self.modeloText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.modelo, self.modeloText)

        # Caja de modulos #3
        # Texto informativo Color
        self.colorV = QLabel("Color: ")
        self.colorV.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:220px;font-weight: bold")
        self.colorV.setFont(QFont("league spartan", 12))

        # Entrada de dato Placa
        self.colorVText = QLineEdit()
        self.colorVText.setFixedWidth(170)
        self.colorVText.setFont(QFont("league spartan", 10))
        self.colorVText.setPlaceholderText("Ingrese Color")
        self.colorVText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.colorV, self.colorVText)

        # Caja de modulos #4
        # Texto informativo Marca
        self.marca = QLabel("Marca: ")
        self.marca.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:220px;font-weight: bold")
        self.marca.setFont(QFont("league spartan", 12))

        # Entrada de dato Placa
        self.marcaText = QLineEdit()
        self.marcaText.setFixedWidth(170)
        self.marcaText.setFont(QFont("league spartan", 10))
        self.marcaText.setPlaceholderText("Ingrese Marca")
        self.marcaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.marca, self.marcaText)

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

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(170)
        self.formulario.addWidget(self.botonLimpiar)
        self.botonLimpiar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonGuardar.clicked.connect(self.accion_botonGuardar)

        self.botonConsultar.clicked.connect(self.accion_botonConsultar)

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)



        self.fondo.setLayout(self.formulario)

    def accion_botonGuardar(self):

        self.mensaje = QMessageBox(self)
        self.mensaje.setStyleSheet("border:solid; border-width:1px; border-color:black;font-weight: bold")
        self.mensaje.setIcon(QMessageBox.Information)
        self.mensaje.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.mensaje.setWindowTitle("Informacion")
        self.mensaje.setText("Datos Guardados Correctamente")
        self.mensaje.setStandardButtons(QMessageBox.Ok)
        self.mensaje.buttonClicked.connect(self.accion_botonMensaje)
        self.mensaje.exec_()
        #reiniciar Valores
        self.marcaText.setText("")
        self.placaText.setText("")
        self.modeloText.setText("")
        self.colorVText.setText("")
    def accion_botonMensaje(self):
        self.mensaje.close()

    def accion_botonConsultar(self):

        if self.placaText.text()=="ANK60G":
            self.modeloText.setText("2022")
            self.colorVText.setText("Negra Mate")
            self.marcaText.setText("Victory-Auteco")
        else:
            self.mensaje = QMessageBox(self)
            self.mensaje.setStyleSheet("border:solid; border-width:1px; border-color:black;font-weight: bold")
            self.mensaje.setIcon(QMessageBox.Information)
            self.mensaje.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.mensaje.setWindowTitle("Informacion")
            self.mensaje.setText("El usuario no se encuentra registrado")
            self.mensaje.setStandardButtons(QMessageBox.Ok)
            self.mensaje.buttonClicked.connect(self.accion_botonMensaje)
            self.mensaje.exec_()

    def accion_botonLimpiar(self):
            self.marcaText.setText("")
            self.placaText.setText("")
            self.modeloText.setText("")
            self.colorVText.setText("")

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







