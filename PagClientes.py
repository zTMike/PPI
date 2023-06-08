from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox
from PyQt5 import QtCore
from DatosCliente import Clientes
import Ayudas



class VentanaCl(QMainWindow):
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
        self.letrero1.setText("Registro de \n Clientes")

        self.letrero1.setFont(QFont("league spartan", 29))
        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background: rgba(76, 175, 80, 0.0); margin-bottom:50px; margin-top:30px;font-weight: bold")
        self.formulario.addRow(self.letrero1)


        #linea Pendiente intentar realizar
        self.letrero2 = QLabel()
        self.letrero2.setText("                                                                                    ")
        self.letrero1.setFont(QFont("league spartan", 35))
        self.letrero2.setStyleSheet("background: rgba(76, 175, 80, 0.0);color:#EFE718; margin-left:220px;text-decoration: underline ;")
        self.formulario.addRow(self.letrero2)




        # Caja de modulos #1

        #Texto informativo cedula
        self.cedula = QLabel("Cédula: ")
        self.cedula.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:170px;font-weight: bold")
        self.cedula.setFont(QFont("league spartan", 12))


        # Entrada de dato cedula
        self.cedulaText = QLineEdit()
        self.cedulaText.setFixedWidth(242)
        self.cedulaText.setFont(QFont("league spartan", 10))
        self.cedulaText.setMaxLength(15)
        self.cedulaText.setPlaceholderText("Ingrese Cédula")
        self.cedulaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.cedula, self.cedulaText)


        # Caja de modulos #2

        #Texto informativo Nombre
        self.nombre = QLabel("Nombre: ")
        self.nombre.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:170px;font-weight: bold")
        self.nombre.setFont(QFont("league spartan", 12))

        # Entrada de dato Nombre
        self.nombreText = QLineEdit()
        self.nombreText.setFixedWidth(242)
        self.nombreText.setFont(QFont("league spartan", 10))
        self.nombreText.setPlaceholderText("Ingrese Nombre")
        self.nombreText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.nombreText.textChanged.connect(lambda text: self.nombreText.setText(text.upper()))
        self.formulario.addRow(self.nombre, self.nombreText)

        # Caja de modulos #3
        # Texto informativo Celular
        self.celular = QLabel("Celular: ")
        self.celular.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:170px;font-weight: bold")
        self.celular.setFont(QFont("league spartan", 12))

        # Entrada de dato Celular
        self.celularText = QLineEdit()
        self.celularText.setFixedWidth(242)
        self.celularText.setMaxLength(10)
        self.celularText.setFont(QFont("league spartan", 10))
        self.celularText.setPlaceholderText("Ingrese Celular")
        self.celularText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.celular, self.celularText)

        # Caja de modulos #4
        # Texto informativo Correo
        self.correo = QLabel("Correo: ")
        self.correo.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:170px;font-weight: bold")
        self.correo.setFont(QFont("league spartan", 12))

        # Entrada de dato Correo
        self.correoText = QLineEdit()
        self.correoText.setFixedWidth(242)
        self.correoText.setFont(QFont("league spartan", 10))
        self.correoText.setPlaceholderText("Ingrese Correo")
        self.correoText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.correoText.textChanged.connect(lambda text: self.correoText.setText(text.upper()))
        self.formulario.addRow(self.correo, self.correoText)

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
        self.ventanaDialogo.setWindowIcon(QIcon("imagenes/IconoGPP.jpeg"))



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

    def accion_botonGuardar(self):
        # datos correctos
        self.datoscorrectos = True

        #________Validarcion cliente ya registrador__________
        self.file = open('Datos/Datos_cliente.txt', 'rb')

        # creamos una lista vacia
        clientes = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            dc = Clientes(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
            )
            # Metemos el objeto en la lista usuario
            clientes.append(dc)

        self.file.close()


        for dc in clientes:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto

            if dc.cedula == self.cedulaText.text():
                self.mensaje.setText(f"EL cliente con Documento {self.cedulaText.text()} \nYa se encuentra registrador")
                self.ventanaDialogo.exec_()
                self.datoscorrectos=False
                self.accion_botonLimpiar()
                break

        # Validacion si las casillas de texto estan vacias o realizado modificacion en los campos
        if self.datoscorrectos==True and(self.cedulaText.text() == '' or
                self.celularText.text() == '' or
                self.correoText.text() == '' or
                self.nombreText.text() == ''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos")
            self.ventanaDialogo.exec_()

        # Validar que usuario ingreso datos con espacios/ verdadero si tiene espacios/ falso si no tiene espacios
        if self.datoscorrectos==True and(self.cedulaText.text().isspace()
                or self.celularText.text().isspace()
                or self.correoText.text().isspace()
                or self.nombreText.text().isspace()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha Ingresado espacios en blanco")
            self.ventanaDialogo.exec_()
        # Fin Validacion Espacios

        # Validacion si en correo y nombre son letras / verdadero si son letras/ falso si es numero
        if self.datoscorrectos==True and(self.correoText.text().isdigit() or
                self.nombreText.text().isdigit()
        ):
            self.datoscorrectos = False
            self.mensaje.setText("Los datos ingresados son incorrectos"
                                 "\nIngrese letras en correo y en nombre")
            self.ventanaDialogo.exec_()
        # Fin Validacion Numeros

        # Validacion si modelo es numeros/ verdadero si son numeros/falso si son letras
        if self.datoscorrectos==True and(self.cedulaText.text().isalpha()or
                self.celularText.text().isalpha()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha ingresado letras en cedula y celular")
            self.ventanaDialogo.exec_()



        # si todo esta ok guarda los datos

        if self.datoscorrectos:

            self.mensaje.setText("Datos guardados correctamente")

            self.ventanaDialogo.exec_()
            # abrimos el archivo en modo agregar
            self.file = open('Datos/Datos_cliente.txt', 'ab')

            # Traer el texto de los Qline y los concatena con ;
            self.file.write(bytes(
                # Cajas de texto de la pestaña
                self.cedulaText.text() + ";"
                + self.nombreText.text() + ";"
                + self.celularText.text() + ";"
                + self.correoText.text() + "\n", encoding='UTF-8'))
            self.file.close()

            # abrimos en modo lectura en formato bite
            self.file = open('Datos\Datos_cliente.txt', 'rb')

            # recorrer el archivo linea x linea
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break

            self.file.close()
            self.accion_botonLimpiar()

    def accion_botonMensaje(self):
        self.mensaje.close()
    def accion_botonConsultar(self):
        # datos correctos
        self.datoscorrectos = True
        # establecemos un titulo a la ventana
        self.ventanaDialogo.setWindowTitle("Consultar Vehiculo")

        # validamos que se haya ingresado un documento
        if (self.cedulaText.text() == ''):
            self.datoscorrectos = False

            self.mensaje.setText("Si va a consultar un vehiculo"
                                 "\nDebe primero, ingresar la placa")
            self.cedulaText.setFocus()
            self.accion_botonLimpiar()
            self.ventanaDialogo.exec_()
            # si estan correctos los datos

        if (self.datoscorrectos):
            # abrimos el archivo  en modo binario
            self.file = open('Datos/Datos_cliente.txt', 'rb')

            # creamos una lista vacia
            clientes = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                dc = Clientes(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                )
                # Metemos el objeto en la lista usuario
                clientes.append(dc)

            self.file.close()

            # En este punto tenemos la lista de usuario con todos los usuarios

            # Variable para controlar si existe el documento
            existecedula = False

            for dc in clientes:
                # Comparemos el documento ingresado
                # Si corresponde con el documento es el usuario correcto
                if dc.cedula == self.cedulaText.text():
                    # limpiamos las cajas de texto
                    self.celularText.setText("")
                    self.nombreText.setText("")
                    self.correoText.setText("")

                    # Mostramos las preguntas en el formulario
                    self.celularText.setText(dc.celular)
                    self.nombreText.setText(dc.nombre)
                    self.correoText.setText(dc.correo)
                    # indicamos que encontramos el documento
                    existecedula = True
                    self.cedulaText.setReadOnly(True)
                    self.celularText.setReadOnly(True)
                    self.nombreText.setReadOnly(True)
                    self.correoText.setReadOnly(True)

                    # Rompemos el for
                    break
            if (
                    not existecedula
            ):
                self.mensaje.setText("No existe una cedula con: \n" + self.cedulaText.text())
                self.celularText.setText("")
                self.nombreText.setText("")
                self.correoText.setText("")

                # Hacemos que la ventana se vea
                self.ventanaDialogo.exec_()



    def accion_botonLimpiar(self):
        self.cedulaText.setText("")
        self.celularText.setText("")
        self.nombreText.setText("")
        self.correoText.setText("")
        self.cedulaText.setReadOnly(False)
        self.celularText.setReadOnly(False)
        self.nombreText.setReadOnly(False)
        self.correoText.setReadOnly(False)
        self.cedulaText.setFocus()


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





