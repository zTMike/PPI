from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox
from PyQt5 import QtCore

import Ayudas
from DatosVehiculo import Vehiculos
from Ayudas import Ayuda




class VentanaRv(QMainWindow):
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
        self.placaText = QLineEdit(self)
        self.placaText.setFixedWidth(170)
        self.placaText.setMaxLength(6)
        self.placaText.setFont(QFont("league spartan", 10))
        self.placaText.setPlaceholderText("Ingrese Placa")
        self.placaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.placaText.textChanged.connect(lambda text: self.placaText.setText(text.upper()))
        self.formulario.addRow(self.placa, self.placaText)


        # Caja de modulos #2

        #Texto informativo Modelo
        self.modelo = QLabel("Modelo: ")
        self.modelo.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:220px;font-weight: bold")
        self.modelo.setFont(QFont("league spartan", 12))

        # Entrada de dato Modelo
        self.modeloText = QLineEdit()
        self.modeloText.setFixedWidth(170)
        self.modeloText.setMaxLength(4)
        self.modeloText.setFont(QFont("league spartan", 10))
        self.modeloText.setPlaceholderText("Ingrese Modelo")
        self.modeloText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.modeloText.textChanged.connect(lambda text: self.modeloText.setText(text.upper()))
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
        self.colorVText.textChanged.connect(lambda text: self.colorVText.setText(text.upper()))
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
        self.marcaText.textChanged.connect(lambda text: self.marcaText.setText(text.upper()))
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


        if Ayudas.Ayuda.TipoUsuario=="Admin":

            self.botonActualizar = QPushButton("Actualizar")
            self.botonActualizar.setFixedWidth(170)
            self.formulario.addWidget(self.botonActualizar)
            self.botonActualizar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                            "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
            self.botonActualizar.clicked.connect(self.accion_botonActualizar)

            self.botonEliminar = QPushButton("Eliminar")
            self.botonEliminar.setFixedWidth(170)
            self.formulario.addWidget(self.botonEliminar)
            self.botonEliminar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                            "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

            self.botonEliminar.clicked.connect(self.accion_botonEliminar)







        self.botonGuardar.clicked.connect(self.accion_botonGuardar)

        self.botonConsultar.clicked.connect(self.accion_botonConsultar)

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)



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

    def accion_botonActualizar(self):
        pass

    def accion_botonEliminar(self):
        pass

    def accion_botonGuardar(self):

        # datos correctos
        self.datoscorrectos = True

        #____________VAlidar si la placa ya se encuentra registrada_______

        # abrimos el archivo  en modo binario
        self.file = open('Datos/Datos_vehiculos.txt', 'rb')

        # creamos una lista vacia
        vehiculos = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            dv = Vehiculos(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
            )
            # Metemos el objeto en la lista usuario
            vehiculos.append(dv)

        self.file.close()


        for dv in vehiculos:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto
            print(dv.placa)
            if dv.placa == self.placaText.text():
                self.mensaje.setText(f"El vehiculo {self.placaText.text()} ya se encuentra registrador")
                self.ventanaDialogo.exec_()
                self.datoscorrectos = False
                self.accion_botonLimpiar()
                print("Hola1")
                break

        if self.datoscorrectos==True and(self.placaText.text() == '' or
                self.modeloText.text() == '' or
                self.colorVText.text() == '' or
                self.marcaText.text() == ''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos para guardar")
            self.ventanaDialogo.exec_()


        #Validar que usuario ingreso datos con espacios/ verdadero si tiene espacios/ falso si no tiene espacios
        if self.datoscorrectos==True and (self.placaText.text().isspace()
                or self.marcaText.text().isspace()
                or self.modeloText.text().isspace()
                or self.colorVText.text().isspace()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha Ingresado espacios en blanco")
            self.ventanaDialogo.exec_()
        #Fin Validacion Espacios

        #Validacion si en marca o en color son letras / verdadero si son letras/ falso si es numero
        if self.datoscorrectos==True and(self.marcaText.text().isdigit()or
                self.colorVText.text().isdigit()
        ):
            self.datoscorrectos = False
            self.mensaje.setText("Ha ingresador numeros en el marca o color")
            self.ventanaDialogo.exec_()
        #Fin Validacion Numeros


        #Validacion si modelo es numeros/ verdadero si son numeros/falso si son letras
        if self.datoscorrectos==True and(self.modeloText.text().isalpha()):
            self.datoscorrectos = False

            self.mensaje.setText("Ha ingresado letras en el modelo")
            self.ventanaDialogo.exec_()

        # si todo esta ok guarda los datos
        if self.datoscorrectos:

            self.mensaje.setText("Datos guardados correctamente")

            self.ventanaDialogo.exec_()
            # abrimos el archivo en modo agregar
            self.file = open('Datos/Datos_vehiculos.txt', 'ab')

            # Traer el texto de los Qline y los concatena con ;
            self.file.write(bytes(
                #Cajas de texto de la pestaña
                self.placaText.text() + ";"
                + self.modeloText.text() + ";"
                + self.colorVText.text() + ";"
                + self.marcaText.text()+ "\n", encoding='UTF-8'))
            self.file.close()

            # abrimos en modo lectura en formato bite
            self.file = open('Datos\Datos_vehiculos.txt', 'rb')

            # recorrer el archivo linea x linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break

            self.file.close()
            self.accion_botonLimpiar()














    def accion_botonConsultar(self):
        # datos correctos
        self.datoscorrectos = True
        # establecemos un titulo a la ventana
        self.ventanaDialogo.setWindowTitle("Consultar Vehiculo")

        # validamos que se haya ingresado un documento
        if (self.placaText.text() == ''):
            self.datoscorrectos = False

            self.mensaje.setText("Si va a consultar un vehiculo"
                                 "\nDebe primero, ingresar la placa")
            self.placaText.setFocus()
            self.accion_botonLimpiar()
            self.ventanaDialogo.exec_()
            # si estan correctos los datos

        if (self.datoscorrectos):
            # abrimos el archivo  en modo binario
            self.file = open('Datos/Datos_vehiculos.txt', 'rb')

            # creamos una lista vacia
            vehiculos = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                dv = Vehiculos(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                )
                # Metemos el objeto en la lista usuario
                vehiculos.append(dv)



            self.file.close()

            # En este punto tenemos la lista de usuario con todos los usuarios

            # Variable para controlar si existe el documento
            existeplaca = False

            for dv in vehiculos:
                # Comparemos el documento ingresado
                # Si corresponde con el documento es el usuario correcto
                if dv.placa == self.placaText.text():
                        # limpiamos las cajas de texto
                    self.modeloText.setText("")
                    self.colorVText.setText("")
                    self.marcaText.setText("")

                    # Mostramos las preguntas en el formulario
                    self.modeloText.setText(dv.modelo)
                    self.colorVText.setText(dv.color)
                    self.marcaText.setText(dv.marca)
                    # indicamos que encontramos el documento
                    self.placaText.setReadOnly(True)
                    self.modeloText.setReadOnly(True)
                    self.colorVText.setReadOnly(True)
                    self.marcaText.setReadOnly(True)
                    existeplaca = True

                    # Rompemos el for
                    break
            if (
                    not existeplaca
            ):
                self.mensaje.setText("No existe un vehiculo con esa placa\n" + self.placaText.text())
                self.modeloText.setText("")
                self.colorVText.setText("")
                self.marcaText.setText("")

                # Hacemos que la ventana se vea
                self.ventanaDialogo.exec_()


    def accion_botonLimpiar(self):
            self.marcaText.setText("")
            self.placaText.setText("")
            self.modeloText.setText("")
            self.colorVText.setText("")
            self.placaText.setFocus()
            self.placaText.setReadOnly(False)
            self.modeloText.setReadOnly(False)
            self.colorVText.setReadOnly(False)
            self.marcaText.setReadOnly(False)

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







