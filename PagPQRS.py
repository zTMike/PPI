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



class VentanaQr(QMainWindow):
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
        self.letrero1.setText("Quejas y Reclamos")


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
        self.idpqrs = QLabel("ID Queja: ")
        self.idpqrs.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold;margin-top:50px;")
        self.idpqrs.setFont(QFont("league spartan", 12))



        # Entrada de dato cedula
        self.idpqrsText = QLineEdit()
        self.idpqrsText.setFixedWidth(260)
        self.idpqrsText.setFont(QFont("league spartan", 10))
        self.idpqrsText.setPlaceholderText("Ingrese ID de PQRS")
        self.idpqrsText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold; margin-top:50px;")
        self.formulario.addRow(self.idpqrs, self.idpqrsText)


        # Caja de modulos #2

        # Texto informativo cedula
        self.cedula = QLabel("Cédula cliente: ")
        self.cedula.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.cedula.setFont(QFont("league spartan", 12))

        # Entrada de dato cedula
        self.cedulaText = QLineEdit()
        self.cedulaText.setFixedWidth(260)
        self.cedulaText.setFont(QFont("league spartan", 10))
        self.cedulaText.setPlaceholderText("Ingrese Cédula")
        self.cedulaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.cedula, self.cedulaText)



        # Caja de modulos #3



        # Caja de modulos #4
        # Texto informativo placa
        self.placa = QLabel("Placa : ")
        self.placa.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.placa.setFont(QFont("league spartan", 12))

        # Entrada de dato Placa
        self.placaText = QLineEdit()
        self.placaText.setFixedWidth(260)
        self.placaText.setFont(QFont("league spartan", 10))
        self.placaText.setPlaceholderText("Ingrese Placa")
        self.placaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.placaText.textChanged.connect(lambda text: self.placaText.setText(text.upper()))
        self.formulario.addRow(self.placa, self.placaText)

        # Caja de modulos #5
        # Texto informativo fecha y hora

        self.fecha = QLabel("Fecha: ")
        self.fecha.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.fecha.setFont(QFont("league spartan", 12))

        # Entrada de dato Fecha y hora
        self.fechaText = QLineEdit()
        self.fechaText.setFixedWidth(260)
        self.fechaText.setFont(QFont("league spartan", 10))
        self.fechaText.setPlaceholderText("Ingrese Fecha de PQRS")
        self.fechaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                          "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.fechaText.setInputMask("99/99/9999")  # para mostrar las barras "/"
        self.fechaText.setText(datetime.date.today().strftime("%m/%d/%Y"))  # para mostrar la fecha actual
        self.fechaText.setReadOnly(True)

        self.formulario.addRow(self.fecha, self.fechaText)


        # Caja de modulos #8
        # Texto informativo fecha Respuesta

        self.estado = QLabel("Estado: ")
        self.estado.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.estado.setFont(QFont("league spartan", 12))

        # Entrada de dato Fecha respuesta

        self.estadoText = QComboBox()
        self.estadoText.addItem("Pendiente")
        self.estadoText.addItem("Solucionado")
        self.estadoText.setFixedWidth(260)
        self.estadoText.setFont(QFont("league spartan", 10))
        self.estadoText.setPlaceholderText("Solucionado o pendiente")
        self.estadoText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.estado, self.estadoText)

        # Caja de modulos #9
        # Texto informativo estado de la pqr


        # Caja de modulos #10
        # Texto informativo descripción de la pqr

        self.descripcion = QLabel("Descripcion: ")
        self.descripcion.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.descripcion.setFont(QFont("league spartan", 12))

        # Entrada de dato descripción de la pqr
        self.descripcionrText = QLineEdit()
        self.descripcionrText.setFixedWidth(260)
        self.descripcionrText.setFont(QFont("league spartan", 10))
        self.descripcionrText.setPlaceholderText("Descripcion de lo sucedido ")
        self.descripcionrText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.descripcion, self.descripcionrText)

        # Caja de modulos #11
        # Texto informativo fecha solución

        self.fechacierre = QLabel("Fecha de Solución: ")
        self.fechacierre.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.fechacierre.setFont(QFont("league spartan", 12))

        # Entrada de dato fecha de la solución
        self.fechacierreText = QLineEdit()
        self.fechacierreText.setFixedWidth(260)
        self.fechacierreText.setFont(QFont("league spartan", 10))
        self.fechacierreText.setPlaceholderText("Fecha de cierre de PQRS")
        self.fechacierreText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                            "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.fechacierreText.setInputMask("99/99/9999")  # para mostrar las barras "/"
        self.fechacierreText.setText(datetime.date.today().strftime("%m/%d/%Y"))  # para mostrar la fecha actual
        self.fechacierreText.setReadOnly(True)

        self.formulario.addRow(self.fechacierre, self.fechacierreText)



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

        self.botonlimpiar = QPushButton("Limpiar")
        self.botonlimpiar.setFixedWidth(170)
        self.formulario.addWidget(self.botonlimpiar)
        self.botonlimpiar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonGuardar.clicked.connect(self.accion_botonGuardar)

        self.botonConsultar.clicked.connect(self.accion_botonConsultar)

        self.botonlimpiar.clicked.connect(self.accion_botonlimpiar)



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
        self.file = open('Datos/Datos_PQRS.txt', 'rb')

        # creamos una lista vacia
        pqrs = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            dp = PQRS(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
            )
            # Metemos el objeto en la lista usuario
            pqrs.append(dp)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        for dp in pqrs:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto

            if not dp.idpqrs =='':
                self.consecutivo=int(dp.idpqrs)
                self.idpqrsText.setText(str(self.consecutivo+1))



    def accion_botonlimpiar(self):
        self.idpqrsText.setText("")
        self.cedulaText.setText("")
        self.placaText.setText("")
        self.estadoText.currentText()
        self.fechacierreText.setText(datetime.date.today().strftime("%m/%d/%Y"))  # para mostrar la fecha actual
        self.descripcionrText.setText("")
        self.fechaText.setText(datetime.date.today().strftime("%m/%d/%Y"))  # para mostrar la fecha actual
        self.consecutivo_iniciarl()
        self.idpqrsText.setReadOnly(False)
        self.cedulaText.setReadOnly(False)
        self.placaText.setReadOnly(False)
        self.fechacierreText.setReadOnly(False)
        self.descripcionrText.setReadOnly(False)
        self.fechaText.setReadOnly(False)

    def accion_botonGuardar(self):

        print("Inicia BT Guardar")
        self.datoscorrectos = True
        # ___________Consecutivo inicial para entrada________
        # abrimos el archivo en modo binario
        self.file = open('Datos/Datos_PQRS.txt', 'rb')

        # creamos una lista vacia
        pqrs = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            dp = PQRS(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
            )
            # Metemos el objeto en la lista usuario
            pqrs.append(dp)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        for dp in pqrs:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto

            if dp.idpqrs == self.idpqrsText.text():
                self.mensaje.setText(f"La queja o reclamo con el consecutivo: {self.idpqrsText.text()}\nYa se encuentra registrada")
                self.ventanaDialogo.exec_()
                self.datoscorrectos = False
                self.accion_botonlimpiar()
                break
                
        print("Inicia Validacion si los campos estan vacios")
        # Validacion si las casillas de texto estan vacias o realizado modificacion en los campos
        if self.datoscorrectos == True and (self.idpqrsText.text() == '' or
                                            self.cedulaText.text() == '' or
                                            self.placaText.text() == '' or
                                            self.fechaText.text() == '' or
                                            self.estadoText.currentText() == '' or
                                            self.fechacierreText.text() == '' or
                                            self.descripcionrText.text() == ''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos para guardar")

            self.ventanaDialogo.exec_()
        print("Inicia Validacion si los campos tienen espacios")
        # Validar que usuario ingreso datos con espacios/ verdadero si tiene espacios/ falso si no tiene espacios
        if self.datoscorrectos == True and (self.estadoText.currentText().isspace()
                                            or self.cedulaText.text().isspace()
                                            or self.placaText.text().isspace()
                                            or self.fechaText.text().isspace()
                                            or self.estadoText.currentText().isspace()
                                            or self.descripcionrText.text().isspace()
                                            or self.fechacierreText.text().isspace()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha Ingresado espacios en blanco")
            self.ventanaDialogo.exec_()
        # Fin Validacion Espacios

        print("Inicia Validacion si los campos tienen letras")
        # Validacion si modelo es numeros/ verdadero si son numeros/falso si son letras
        if self.datoscorrectos == True and (self.idpqrs.text().isalpha() or
                                            self.cedulaText.text().isalpha() or
                                            self.fechaText.text().isalpha() or
                                            self.fechacierreText.text().isalpha()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha ingresado letras en los campos numericos")
            self.ventanaDialogo.exec_()

        # Validacion si en marca o en color son letras / verdadero si son letras/ falso si es numero
        if self.datoscorrectos == True and (self.descripcionrText.text().isdigit()or
                                            self.estadoText.currentText().isdigit()
        ):
            self.datoscorrectos = False
            self.mensaje.setText("Ha ingresador numeros en la descripcion o estado")
            self.ventanaDialogo.exec_()
        # Fin Validacion Numeros

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

            if dc.cedula == self.cedulaText.text() and self.datoscorrectos == True:
                self.validacion = True
                print("CD registrada")
                break
            else:
                self.validacion = False

        if self.datoscorrectos == True and self.validacion == False:
            self.mensaje.setText("El documento del cliente no se encuentra registrado")
            self.ventanaDialogo.exec_()
            self.datoscorrectos = False

        # ____________VAlidacion si el vehiculo ya se encuentra registrado

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



        # si todo esta ok guarda los datos
        if self.datoscorrectos:
            self.mensaje.setText("Datos guardados correctamente")

            self.ventanaDialogo.exec_()
            # abrimos el archivo en modo agregar
            self.file = open('Datos/Datos_PQRS.txt', 'ab')

            # Traer el texto de los Qline y los concatena con ;
            self.file.write(bytes(
                # Cajas de texto de la pestaña
                self.idpqrsText.text() + ";"
                + self.cedulaText.text() + ";"
                + self.placaText.text() + ";"
                + self.fechaText.text() + ";"
                + self.estadoText.currentText() + ";"
                + self.descripcionrText.text() + ";"
                + self.fechacierreText.text() + "\n", encoding='UTF-8'))
            self.file.close()

            self.file.close()
            self.accion_botonlimpiar()
    def accion_botonConsultar(self):
        # datos correctos
        self.datoscorrectos = True
        # establecemos un titulo a la ventana
        self.ventanaDialogo.setWindowTitle("Consultar Ingreso")

        # validamos que se haya ingresado un documento
        if (self.idpqrsText.text() == ''):
            self.datoscorrectos = False

            self.mensaje.setText("Si va a consultar una PQRS"
                                 "\nDebe primero, ingresar la id PQRS")
            self.ingresoText.setFocus()
            self.accion_botonlimpiar()
            self.ventanaDialogo.exec_()
            # si estan correctos los datos

        if (self.datoscorrectos):
            # abrimos el archivo en modo binario
            self.file = open('Datos/Datos_PQRS.txt', 'rb')

            # creamos una lista vacia
            pqrs = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                dp = PQRS(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                )
                # Metemos el objeto en la lista usuario
                pqrs.append(dp)

            self.file.close()

            # En este punto tenemos la lista de usuario con todos los usuarios

            # Variable para controlar si existe el documento
            idpqrs=False
            for dp in pqrs:
                # Comparemos el documento ingresado
                # Si corresponde con el documento es el usuario correcto
                if dp.idpqrs == self.idpqrsText.text():
                    # limpiamos las cajas de texto
                    self.cedulaText.setText("")
                    self.placaText.setText("")
                    self.fechaText.setText(datetime.date.today().strftime("%m/%d/%Y"))
                    self.estadoText.currentText()
                    self.descripcionrText.setText("")
                    self.fechacierreText.setText(datetime.date.today().strftime("%m/%d/%Y"))

                    # Mostramos las preguntas en el formulario
                    self.cedulaText.setText(dp.documento)
                    self.placaText.setText(dp.placa)
                    self.fechaText.setText(dp.fechaq)

                    if dp.estado=="Pendiente":
                        self.estadoText.setCurrentIndex(0)
                    elif dp.estado=="Solucionado":
                        self.estadoText.setCurrentIndex(1)

                    self.descripcionrText.setText(dp.descripcion)
                    self.fechacierreText.setText(dp.fechas)

                    # indicamos que encontramos el documento
                    idpqrs = True
                    self.idpqrsText.setReadOnly(True)
                    self.cedulaText.setReadOnly(True)
                    self.placaText.setReadOnly(True)
                    self.descripcionrText.setReadOnly(True)
                    self.fechaText.setReadOnly(True)
                    self.fechacierreText.setReadOnly(True)
                    self.estadoText.setEnabled(False)


                    # Rompemos el for
                    break
            if (not idpqrs):
                self.mensaje.setText(f"El ID de ingreso{self.ingresoText.text()} \nNo ha sido registrado")
                self.cedulaText.setText("")
                self.placaText.setText("")
                self.horaText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
                self.fechaText.setText(datetime.date.today().strftime("%m/%d/%Y"))
                self.celdaText.setText("")
                # Hacemos que la ventana se vea
                self.ventanaDialogo.exec_()

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







