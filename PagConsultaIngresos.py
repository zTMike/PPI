from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox, QScrollArea, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore

import Ayudas
from DatosConsultaIngresos import Consulta




class VentanaCI(QMainWindow):
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
        self.letrero1.setText("Consulta de ingresos")

        self.letrero1.setFont(QFont("league spartan", 29))
        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background: rgba(76, 175, 80, 0.0); margin-bottom:50px; margin-top:30px;font-weight: bold")
        self.formulario.addRow(self.letrero1)

        self.crear_cajas()

        self.fondo.setLayout(self.formulario)

        #________________Ventana emergente___________
        #creamos ventana de dialogo
        self.ventanaDialogo=QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        #asignamos tama;o a la ventana de dailogo

        self.vdancho = 300
        self.vdalto = 150


        self.ventanaDialogo.resize(self.vdancho, self.vdalto)
        # Para que las ventanas no se puedan estirar o mover
        # Width= Ancho
        self.ventanaDialogo.setFixedWidth(self.vdancho)
        # Height= Alto
        self.ventanaDialogo.setFixedHeight(self.vdalto)



        #Creamos el boton aceptar
        self.botonAceptar=QDialogButtonBox.Ok
        self.opciones=QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)
        #Establecemos titulo de la ventana
        self.ventanaDialogo.setWindowTitle("Guardar datos")

        #Configuramos que la ventana sea modal
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)



        #Creamos layout vertical
        self.vertical=QVBoxLayout()

        #Creamos en label para los mensajes
        self.mensaje=QLabel("")


        #agregamos mensajes al vertical
        self.vertical.addWidget(self.mensaje)

        # agregamos Boton al vertical
        self.vertical.addWidget(self.opciones)

        #asigna layout a la ventana
        self.ventanaDialogo.setLayout(self.vertical)

    def crear_cajas(self):
        # Caja de modulos #1

        # Texto informativo cedula
        self.FechaI = QLabel("Fecha Inicial: ")
        self.FechaI.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:170px;font-weight: bold")
        self.FechaI.setFont(QFont("league spartan", 12))

        # Entrada de dato cedula
        self.FechaIText = QLineEdit()
        self.FechaIText.setFixedWidth(242)
        self.FechaIText.setFont(QFont("league spartan", 10))
        self.FechaIText.setMaxLength(15)
        self.FechaIText.setPlaceholderText("Ingrese una fecha")
        self.FechaIText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.FechaIText.setInputMask("99/99/9999")  # para mostrar las barras "/"
        self.formulario.addRow(self.FechaI, self.FechaIText)

        # Caja de modulos #2

        # Texto informativo Nombre
        self.Fechaf = QLabel("Fecha Final: ")
        self.Fechaf.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:170px;font-weight: bold")
        self.Fechaf.setFont(QFont("league spartan", 12))

        # Entrada de dato Nombre
        self.FechafText = QLineEdit()
        self.FechafText.setFixedWidth(242)
        self.FechafText.setFont(QFont("league spartan", 10))
        self.FechafText.setPlaceholderText("Ingrese una fecha")
        self.FechafText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.FechafText.setInputMask("99/99/9999")  # para mostrar las barras "/"
        self.formulario.addRow(self.Fechaf, self.FechafText)

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

        self.botonConsultar.clicked.connect(self.accion_botonConsultar)

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar1)


    def accion_botonConsultar(self):

        self.botonConsultar.deleteLater()
        self.FechafText.deleteLater()
        self.FechaIText.deleteLater()
        self.Fechaf.deleteLater()
        self.FechaI.deleteLater()
        self.botonLimpiar.deleteLater()

        self.file = open('Datos/Datos_ingresos.txt', 'rb')
        self.ingresos = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')
            lista = linea.split(";")

            if linea == '':
                break

            u = Consulta(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
            )

            self.ingresos.append(u)
        self.file.close()

        self.numeroingresos = len(self.ingresos)
        self.contador = 0


        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        # para crear la tabla para que se vean de forma tabular
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)

        # definimos los numeros de colimnas que tendra la tabla

        self.tabla.setColumnWidth(0, 120)
        self.tabla.setColumnWidth(1, 120)
        self.tabla.setColumnWidth(2, 100)
        self.tabla.setColumnWidth(3, 100)
        self.tabla.setColumnWidth(4, 100)
        self.tabla.setHorizontalHeaderLabels(["ID Ingreso",
                                              "Dcoumento Cliente",
                                              "Fecha de ingreso",
                                              "Horas",
                                              "Total A pagar"
                                              ])

        self.tabla.setRowCount(self.numeroingresos)

        for u in self.ingresos:

            if u.fecha>=self.FechaIText.text() and u.fecha>=self.FechafText.text():
                self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.idingreso))
                self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.documento))
                self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.fecha))
                self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.horas))
                self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.ingreso))

                for i in range(self.tabla.columnCount()):
                    self.tabla.item(self.contador, i).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                self.contador += 1

        self.scrollArea.setWidget(self.tabla)
        self.formulario.addRow(self.scrollArea)


        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(170)
        self.formulario.addWidget(self.botonLimpiar)
        self.botonLimpiar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                        "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)


    def accion_botonLimpiar(self):
        self.scrollArea.deleteLater()
        self.botonLimpiar.deleteLater()
        self.crear_cajas()
    def accion_botonLimpiar1(self):
        self.FechafText.setText("")
        self.FechaIText.setText("")
        self.FechaIText.setFocus()

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
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()
            self.vetanaAnterior.show()
        if event.key() == Qt.Key_F1:
            self.accion_botonGuardar()
        if event.key() == Qt.Key_F2:
            self.accion_botonConsultar()
        if event.key() == Qt.Key_F3:
            self.accion_botonLimpiar()
        if Ayudas.Ayuda.TipoUsuario=="Admin":
            if event.key() == Qt.Key_F4:
                self.accion_botonActualizar()
            if event.key() == Qt.Key_F5:
                self.accion_botonEliminar()




