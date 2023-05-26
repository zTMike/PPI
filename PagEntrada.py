from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox
from PyQt5 import QtCore
import datetime
from DatosEntrada import Entrada
from DatosCliente import Clientes
from DatosVehiculo import Vehiculos


class VentanaRi(QMainWindow):
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
        self.letrero1.setText("Registro de Entrada")

        self.letrero1.setFont(QFont("league spartan", 29))
        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background: rgba(76, 175, 80, 0.0); margin-bottom:80px; margin-top:90px;font-weight: bold")
        self.formulario.addRow(self.letrero1)


        #linea Pendiente intentar realizar
        self.letrero2 = QLabel()
        self.letrero2.setText("                                                                                    ")
        self.letrero1.setFont(QFont("league spartan", 35))
        self.letrero2.setStyleSheet("background: rgba(76, 175, 80, 0.0);color:#EFE718; margin-left:240px;text-decoration: underline ;")
        self.formulario.addRow(self.letrero2)




        # Caja de modulos #1

        #Texto informativo Numero de ingreso
        self.ingreso = QLabel("Número de ingreso: ")
        self.ingreso.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold;text-align: right;")
        self.ingreso.setFont(QFont("league spartan", 12))


        # Entrada de dato cedula
        self.ingresoText = QLineEdit()
        self.ingresoText.setFixedWidth(170)
        self.ingresoText.setFont(QFont("league spartan", 10))
        self.ingresoText.setPlaceholderText("Número de Ingreso")
        self.ingresoText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.ingreso, self.ingresoText)


        # Caja de modulos #2

        #Texto informativo Nombre
        self.cedula = QLabel("Cedula cliente: ")
        self.cedula.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold;")
        self.cedula.setFont(QFont("league spartan", 12))

        # Entrada de dato Modelo
        self.cedulaText = QLineEdit()
        self.cedulaText.setFixedWidth(170)
        self.cedulaText.setFont(QFont("league spartan", 10))
        self.cedulaText.setPlaceholderText("Ingrese cedula del cliente")
        self.cedulaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.cedula, self.cedulaText)

        # Caja de modulos #3
        # Texto informativo Placa
        self.placa = QLabel("Placa: ")
        self.placa.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
        self.placa.setFont(QFont("league spartan", 12))

        # Entrada de dato Placa
        self.placaText = QLineEdit()
        self.placaText.setFixedWidth(170)
        self.placaText.setFont(QFont("league spartan", 10))
        self.placaText.setPlaceholderText("Ingrese Placa")
        self.placaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                     "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.placaText.textChanged.connect(lambda text: self.placaText.setText(text.upper()))
        self.formulario.addRow(self.placa, self.placaText)

        # Caja de modulos #4
        # Texto informativo Fecha
        self.fecha = QLabel("Fecha ingreso: ")
        self.fecha.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
        self.fecha.setFont(QFont("league spartan", 12))

        # Entrada de dato Fecha
        self.fechaText = QLineEdit()
        self.fechaText.setFixedWidth(170)
        self.fechaText.setFont(QFont("league spartan", 10))
        self.fechaText.setPlaceholderText("Ingrese Fecha")
        self.fechaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.fechaText.setInputMask("99/99/9999")  # para mostrar las barras "/"
        self.fechaText.setText(datetime.date.today().strftime("%m/%d/%Y"))  # para mostrar la fecha actual

        self.fechaText.setReadOnly(True)
        self.formulario.addRow(self.fecha, self.fechaText)

        # Caja de modulos #5
        # Texto informativo hora
        self.hora = QLabel("Hora de ingreso: ")
        self.hora.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
        self.hora.setFont(QFont("league spartan", 12))

        # Entrada de dato Hora
        self.horaText = QLineEdit()
        self.horaText.setFixedWidth(170)
        self.horaText.setFont(QFont("league spartan", 10))
        self.horaText.setPlaceholderText("Ingrese Hora")
        self.horaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                     "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.horaText.setInputMask("99:99:99")  # para mostrar los dos puntos ":"
        self.horaText.setText(datetime.datetime.now().strftime("%H:%M:%S"))  # para mostrar la

        self.horaText.setReadOnly(True)
        self.formulario.addRow(self.hora, self.horaText)

        # Caja de modulos #6

        # Texto informativo Celda
        self.celda = QLabel("Celda: ")
        self.celda.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
        self.celda.setFont(QFont("league spartan", 12))

        # Entrada de dato celda
        self.celdaText = QLineEdit()
        self.celdaText.setFixedWidth(170)
        self.celdaText.setFont(QFont("league spartan", 10))
        self.celdaText.setPlaceholderText("Ingrese Número de Celda")
        self.celdaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.celda, self.celdaText)



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

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(170)
        self.formulario.addWidget(self.botonLimpiar)
        self.botonLimpiar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonGuardar.clicked.connect(self.accion_botonGuardar)

        self.botonConsultar.clicked.connect(self.accion_botonConsultar)

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)



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
        self.consecutivo_iniciarl()

    def consecutivo_iniciarl(self):
        #___________Consecutivo inicial para entrada________
        # abrimos el archivo en modo binario
        self.file = open('Datos/Datos_Entrada.txt', 'rb')

        # creamos una lista vacia
        entrada = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            de = Entrada(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
            )
            # Metemos el objeto en la lista usuario
            entrada.append(de)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        for de in entrada:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto

            if not de.idingreso =='':
                self.consecutivo=int(de.idingreso)
                self.ingresoText.setText(str(self.consecutivo+1))




    def accion_botonGuardar(self):

        # datos correctos
        self.datoscorrectos = True

        #____________VAlidar si el consecutivo ya se encuentra registrado_______

        # abrimos el archivo en modo binario
        self.file = open('Datos/Datos_Entrada.txt', 'rb')

        # creamos una lista vacia
        entrada = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            de = Entrada(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
            )
            # Metemos el objeto en la lista usuario
            entrada.append(de)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        for de in entrada:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto

            if de.idingreso == self.ingresoText.text():
                self.mensaje.setText(f"El Id de ingreso {self.ingresoText.text()} ya se encuentra registrador")
                self.ventanaDialogo.exec_()
                self.datoscorrectos = False
                self.accion_botonLimpiar()
                break

        # Validacion si las casillas de texto estan vacias o realizado modificacion en los campos
        if self.datoscorrectos==True and(self.ingresoText.text() == '' or
                self.cedulaText.text() == '' or
                self.placaText.text() == '' or
                self.fechaText.text() == '' or
                self.horaText.text() == '' or
                self.celdaText.text() == ''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos para guardar")

            self.ventanaDialogo.exec_()


        #Validar que usuario ingreso datos con espacios/ verdadero si tiene espacios/ falso si no tiene espacios
        if self.datoscorrectos==True and(self.ingresoText.text().isspace()
                or self.cedulaText.text().isspace()
                or self.placaText.text().isspace()
                or self.fechaText.text().isspace()
                or self.horaText.text().isspace()
                or self.celdaText.text().isspace()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha Ingresado espacios en blanco")
            self.ventanaDialogo.exec_()
        #Fin Validacion Espacios


        #Validacion si modelo es numeros/ verdadero si son numeros/falso si son letras
        if self.datoscorrectos==True and(self.ingresoText.text().isalpha() or
                self.cedulaText.text().isalpha() or
                self.placaText.text().isalpha() or
                self.fechaText.text().isalpha() or
                self.horaText.text().isalpha() or
                self.celdaText.text().isalpha()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha ingresado letras en los campos numericos")
            self.ventanaDialogo.exec_()


        # ________Validarcion cliente ya registrador__________
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

            if dc.cedula==self.cedulaText.text() and self.datoscorrectos==True:
                self.validacion=True
                print("CD registrada")
                break
            else:
                self.validacion = False


        if self.datoscorrectos==True and self.validacion==False:
            self.mensaje.setText("El documento del cliente no se encuentra registrado")
            self.ventanaDialogo.exec_()
            self.datoscorrectos=False

        #____________VAlidacion si el vehiculo ya se encuentra registrado

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
            if dv.placa == self.placaText.text() and self.datoscorrectos == True:
                self.validacion = True
                print("Vh registrada")
                break
            else:
                self.validacion = False

        if self.datoscorrectos == True and self.validacion == False:
            self.mensaje.setText("El Vehiculo no se encuentra registrado")
            self.ventanaDialogo.exec_()
            self.datoscorrectos = False



        # ____________VAlidar si el celda ya se encuentra Ocupada_______

        # abrimos el archivo en modo binario
        self.file = open('Datos/Datos_Entrada.txt', 'rb')

        # creamos una lista vacia
        vcelda = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            de1 = Entrada(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
            )
            # Metemos el objeto en la lista usuario
            vcelda.append(de1)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        for de1 in vcelda:
            if self.datoscorrectos==True:
                self.txtcelda=str(int(de1.celda))
                if self.txtcelda==self.celdaText.text():
                    self.mensaje.setText(f"La celda {self.celdaText.text()} Ya se encuentra en uso")
                    self.ventanaDialogo.exec_()
                    self.datoscorrectos = False


        # si todo esta ok guarda los datos
        if self.datoscorrectos:
            print("Celda Libre")
            self.mensaje.setText("Datos guardados correctamente")

            self.ventanaDialogo.exec_()
            # abrimos el archivo en modo agregar
            self.file = open('Datos/Datos_Entrada.txt', 'ab')

            # Traer el texto de los Qline y los concatena con ;
            self.file.write(bytes(
                #Cajas de texto de la pestaña
                self.ingresoText.text() + ";"
                + self.cedulaText.text() + ";"
                + self.placaText.text() + ";"
                + self.fechaText.text() + ";"
                + self.horaText.text() + ";"
                + self.celdaText.text()+ "\n", encoding='UTF-8'))
            self.file.close()



            self.file.close()
            self.accion_botonLimpiar()

    def accion_botonConsultar(self):
        # datos correctos
        self.datoscorrectos = True
        # establecemos un titulo a la ventana
        self.ventanaDialogo.setWindowTitle("Consultar Vehiculo")

        # validamos que se haya ingresado un documento
        if (self.ingresoText.text() == ''):
            self.datoscorrectos = False

            self.mensaje.setText("Si va a consultar un vehiculo"
                                 "\nDebe primero, ingresar la placa")
            self.ingresoText.setFocus()
            self.accion_botonLimpiar()
            self.ventanaDialogo.exec_()
            # si estan correctos los datos

        if (self.datoscorrectos):
            # abrimos el archivo en modo binario
            self.file = open('Datos/Datos_Entrada.txt', 'rb')

            # creamos una lista vacia
            entrada = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                de = Entrada(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                )
                # Metemos el objeto en la lista usuario
                entrada.append(de)

            self.file.close()

            # En este punto tenemos la lista de usuario con todos los usuarios

            # Variable para controlar si existe el documento
            idingreso = False
            for de in entrada:
                # Comparemos el documento ingresado
                # Si corresponde con el documento es el usuario correcto
                if de.idingreso == self.ingresoText.text():
                    # limpiamos las cajas de texto
                    self.cedulaText.setText("")
                    self.placaText.setText("")
                    self.horaText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
                    self.fechaText.setText(datetime.date.today().strftime("%m/%d/%Y"))
                    self.celdaText.setText("")


                    # Mostramos las preguntas en el formulario
                    self.cedulaText.setText(de.documento)
                    self.placaText.setText(de.placa)
                    self.horaText.setText(de.hora)
                    self.fechaText.setText(de.fecha)
                    self.celdaText.setText(de.celda)
                    idingreso = True
                    self.ingresoText.setReadOnly(True)
                    self.cedulaText.setReadOnly(True)
                    self.placaText.setReadOnly(True)
                    self.celdaText.setReadOnly(True)

                    # Rompemos el for
                    break
            if (not idingreso):
                self.mensaje.setText(f"El ID de ingreso{self.ingresoText.text()} \nNo ha sido registrado")
                self.cedulaText.setText("")
                self.placaText.setText("")
                self.horaText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
                self.fechaText.setText(datetime.date.today().strftime("%m/%d/%Y"))
                self.celdaText.setText("")
                # Hacemos que la ventana se vea
                self.ventanaDialogo.exec_()





    def accion_botonLimpiar(self):
        self.ingresoText.setText("")
        self.cedulaText.setText("")
        self.placaText.setText("")
        self.horaText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
        self.fechaText.setText(datetime.date.today().strftime("%m/%d/%Y"))
        self.celdaText.setText("")
        self.consecutivo_iniciarl()
        self.ingresoText.setReadOnly(False)
        self.cedulaText.setReadOnly(False)
        self.placaText.setReadOnly(False)
        self.celdaText.setReadOnly(False)


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
