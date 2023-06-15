from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox
from PyQt5 import QtCore
import datetime

from DatosEntrada import Entrada
from DatosOcupacion import Ocupacion
from DatosSalida import Salida
from DatosCliente import Clientes
from DatosVehiculo import Vehiculos



class VentanaRs(QMainWindow):
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
        self.letrero1.setText("Registro de Salida")

        self.letrero1.setFont(QFont("league spartan", 29))
        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background: rgba(76, 175, 80, 0.0); margin-bottom:50px; margin-top:20px;font-weight: bold")
        self.formulario.addRow(self.letrero1)


        #linea Pendiente intentar realizar
        self.letrero2 = QLabel()
        self.letrero2.setText("                                                                                    ")
        self.letrero1.setFont(QFont("league spartan", 35))
        self.letrero2.setStyleSheet("background: rgba(76, 175, 80, 0.0);color:#EFE718; margin-left:240px;text-decoration: underline ;")

        # Caja de modulos #1

        # Texto informativo Numero de ingreso
        self.salida = QLabel("Número de Salida: ")
        self.salida.setStyleSheet(
            "background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold;text-align: right;")
        self.salida.setFont(QFont("league spartan", 12))

        # Entrada de dato Salida
        self.salidaText = QLineEdit()
        self.salidaText.setFixedWidth(170)
        self.salidaText.setFont(QFont("league spartan", 10))
        self.salidaText.returnPressed.connect(self.accion_botonConsultar)
        self.salidaText.setPlaceholderText("Número de salida")
        self.salidaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.salida, self.salidaText)
        # Caja de modulos #2

        #Texto informativo Numero de ingreso
        self.ingreso = QLabel("Número de ingreso: ")
        self.ingreso.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold;text-align: right;")
        self.ingreso.setFont(QFont("league spartan", 12))


        # Entrada de dato Ingreso
        self.ingresoText = QLineEdit()
        self.ingresoText.setFixedWidth(170)
        self.ingresoText.setFont(QFont("league spartan", 10))
        self.ingresoText.returnPressed.connect(self.accion_botonConsultar)
        self.ingresoText.setPlaceholderText("Número de Ingreso")
        self.ingresoText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.ingreso, self.ingresoText)






        self.botonConsultar = QPushButton("Consultar")
        self.botonConsultar.setFixedWidth(170)
        self.formulario.addWidget(self.botonConsultar)
        self.botonConsultar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")


        self.botonConsultar.clicked.connect(self.accion_botonConsultar)





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

    def consecutivo_iniciar(self):
        #___________Consecutivo inicial para entrada________
        # abrimos el archivo en modo binario
        self.file = open('Datos/Datos_Salida.txt', 'rb')

        # creamos una lista vacia
        salida = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            ds = Salida(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8]
            )
            # Metemos el objeto en la lista usuario
            salida.append(ds)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        for ds in salida:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto

            if not ds.idsalida =='':
                self.consecutivo=int(ds.idsalida)
                self.salidaText.setText(str(self.consecutivo+1))
                self.salidaText.setReadOnly(True)
        if self.salidaText.text()=="":
            self.salidaText.setText("1")




    def accion_botonGuardar(self):
        self.celdaText.setText("0")
        self.mensaje.setText("Datos guardados correctamente")
        self.ventanaDialogo.exec_()
        # abrimos el archivo en modo agregar
        self.file = open('Datos/Datos_Salida.txt', 'ab')

        # Traer el texto de los Qline y los concatena con ;
        self.file.write(bytes(
            # Cajas de texto de la pestaña
            self.ingresoText.text() + ";"
            + self.salidaText.text() + ";"
            + self.cedulaText.text() + ";"
            + self.placaText.text() + ";"
            + self.fechaText.text() + ";"
            + self.horaText.text() + ";"
            + self.fechasText.text() + ";"
            + self.horasText.text() + ";"
            + self.celdaText.text() +"\n", encoding='UTF-8'))
        self.file.close()
        #_____________Ingreso______________
        fechastr = datetime.datetime.strptime(self.fechaText.text(), '%d/%m/%Y')
        horastr = datetime.datetime.strptime(self.horaText.text(), '%H:%M:%S').time()

        # Combine date and time into a single datetime object
        fhingresocombinada = datetime.datetime.combine(fechastr, horastr)

        # Format datetime as a string
        fhingresocombinadastr = fhingresocombinada.strftime('%d/%m/%Y %H:%M:%S')

        print(fhingresocombinadastr)  # Output: 2022-10-01 13:45:00
        #________Fin Ingreso____________

        #_________________Salida________________
        fechasstr = datetime.datetime.strptime(self.fechasText.text(), '%d/%m/%Y')
        horasstr = datetime.datetime.strptime(self.horasText.text(), '%H:%M:%S').time()

        # Combine date and time into a single datetime object
        fhsalidacombinada = datetime.datetime.combine(fechasstr, horasstr)

        # Format datetime as a string
        fhsalidacombinadastr = fhsalidacombinada.strftime('%d/%m/%Y %H:%M:%S')
        print(type(fhsalidacombinadastr))
        print(fhsalidacombinadastr)  # Output: 2022-10-01 13:45:00
        # ________Fin Salida____________

        #___________Operacion_____________

        datetime1 = datetime.datetime.strptime(fhingresocombinadastr, '%d/%m/%Y %H:%M:%S')
        datetime2 = datetime.datetime.strptime(fhsalidacombinadastr, '%d/%m/%Y %H:%M:%S')

        # Calculate time difference in hours
        self.tiempo = int((datetime2 - datetime1).total_seconds())
        self.Totalngreso = '{:.0f}'.format(self.tiempo * 0.416)
        self.tiempo1 = int((datetime2 - datetime1).total_seconds())/3600
        self.tiempo1 = '{:.0f}'.format(self.tiempo1)




        # Print result
        print(self.tiempo)  # Output: 25.583333333333332
        print(self.Totalngreso)

        self.file = open('Datos/Datos_ingresos.txt', 'ab')

        # Traer el texto de los Qline y los concatena con ;
        self.file.write(bytes(
            # Cajas de texto de la pestaña
            self.salidaText.text() + ";"
            + self.cedulaText.text() + ";"
            + self.fechasText.text() + ";"
            + str(self.tiempo1) + ";"
            + str(self.Totalngreso) + "\n", encoding='UTF-8'))
        self.file.close()

        # agregamos 1 a los datos ocupados
        # abrimos el archivo en modo agregar
        self.file = open('Datos/Datos_Ocupacion_Parqueadero.txt', 'ab')

        # Traer el texto de los Qline y los concatena con ;
        self.file.write(bytes(
            # Cajas de texto de la pestaña
            self.celdaText.text() , encoding='UTF-8'))
        self.file.close()
        print(self.celdaText.text())
        # elimina una celda vacia

        self.file = open('Datos/Datos_Ocupacion_Parqueadero.txt', 'rb')

        # creamos una lista vacia
        ocupacion = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            oc = Ocupacion(
                lista[0]
            )
            # Metemos el objeto en la lista usuario
            ocupacion.append(oc)

        self.file.close()

        # ciclo for para remover el registro de un usuario
        for oc in ocupacion:

            if int(oc.celda) == 1:
                ocupacion.remove(oc)
                break

        self.file = open('Datos/Datos_Ocupacion_Parqueadero.txt', 'wb')

        # reescribir el registro del usuario a vacio

        for oc in ocupacion:
            self.file.write(bytes(oc.celda, encoding='UTF-8'))
        self.file.close()
        self.accion_botonLimpiar()



    def accion_botonConsultar(self):

        #____________VALIDACIONES DE DATOS________________________
        # datos correctos
        self.datoscorrectos = True
        # establecemos un titulo a la ventana
        self.ventanaDialogo.setWindowTitle("Consultar Vehiculo")

        # validamos que se haya ingresado un documento
        if (self.ingresoText.text() == ''and self.salidaText.text()==''):
            self.datoscorrectos = False

            self.mensaje.setText("Si va a consultar o registrar una salida "
                                 "\nDebe primero, ingresar un ID Entrada  para registrar o "
                                 "\nIngresar una ID salida para consultar")
            self.ingresoText.setFocus()
            self.ingresoText.setText("")
            self.salidaText.setText("")
            self.ventanaDialogo.exec_()
        else:
            if (self.ingresoText.text() != ''and self.salidaText.text()!=''):
                self.datoscorrectos = False

                self.mensaje.setText("Si va a consultar o registrar una salida "
                                     "\nDebe ingresar uno de los 2 campos")
                self.ingresoText.setFocus()
                self.ingresoText.setText("")
                self.salidaText.setText("")
                self.ventanaDialogo.exec_()
            # si estan correctos los datos
        if (self.datoscorrectos):
            if (self.ingresoText!=''):# abrimos el archivo en modo binario
                self.file = open('Datos/Datos_Salida.txt', 'rb')
                # creamos una lista vacia
                salida = []

                while self.file:
                    # lea el archivo y traiga los datos
                    linea = self.file.readline().decode('UTF-8')

                    # elimine el ; y ponga en una posicion
                    lista = linea.split(";")

                    # se para si ya no hay mas registros
                    if linea == '':
                        break
                    # creamos un objeto tipo cliente llamado u
                    ds = Salida(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                        lista[4],
                        lista[5],
                        lista[6],
                        lista[7],
                        lista[8],
                    )
                    # Metemos el objeto en la lista usuario
                    salida.append(ds)

                self.file.close()

                # En este punto tenemos la lista de usuario con todos los usuarios

                # Variable para controlar si existe el documento
                registrado=False
                for ds in salida:
                    # Comparemos el documento ingresado
                    # Si corresponde con el documento es el usuario correcto

                    if ds.identrada == self.ingresoText.text():
                        self.mensaje.setText(f"El ID de ingreso {self.ingresoText.text()} Ya fue registrado")
                        registrado=True
                        self.ventanaDialogo.exec_()
                        self.ingresoText.setFocus()
                if registrado==False:
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

                            self.botonConsultar.deleteLater()

                            # linea Pendiente intentar realizar
                            self.letrero2 = QLabel()
                            self.letrero2.setText(
                                "                                                                                    ")
                            self.letrero1.setFont(QFont("league spartan", 35))
                            self.letrero2.setStyleSheet(
                                "background: rgba(76, 175, 80, 0.0);color:#EFE718; margin-left:240px;text-decoration: underline ;")

                            # Caja de modulos #2

                            # Texto informativo Nombre
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
                            self.fechaText.setText(datetime.date.today().strftime("%d/%m/%Y"))  # para mostrar la fecha actual
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
                            self.formulario.addRow(self.hora, self.horaText)

                            # Caja de modulos #6
                            # Texto informativo Fecha
                            self.fechas = QLabel("Fecha Salida: ")
                            self.fechas.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
                            self.fechas.setFont(QFont("league spartan", 12))

                            # Entrada de dato Fecha
                            self.fechasText = QLineEdit()
                            self.fechasText.setFixedWidth(170)
                            self.fechasText.setFont(QFont("league spartan", 10))
                            self.fechasText.setPlaceholderText("Ingrese Fecha")
                            self.fechasText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                          "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
                            self.fechasText.setInputMask("99/99/9999")  # para mostrar las barras "/"
                            self.fechasText.setText(datetime.date.today().strftime("%d/%m/%Y"))  # para mostrar la fecha actual
                            self.formulario.addRow(self.fechas, self.fechasText)

                            # Caja de modulos #7
                            # Texto informativo hora
                            self.horas = QLabel("Hora de Salida: ")
                            self.horas.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
                            self.horas.setFont(QFont("league spartan", 12))

                            # Entrada de dato Hora
                            self.horasText = QLineEdit()
                            self.horasText.setFixedWidth(170)
                            self.horasText.setFont(QFont("league spartan", 10))
                            self.horasText.setPlaceholderText("Ingrese Hora")
                            self.horasText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
                            self.horasText.setInputMask("99:99:99")  # para mostrar los dos puntos ":"
                            self.horasText.setText(datetime.datetime.now().strftime("%H:%M:%S"))  # para mostrar la
                            self.formulario.addRow(self.horas, self.horasText)

                            # Caja de modulos #8

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
                            self.celdaText.setText("0")

                            # Linea Separadora
                            self.formulario.addRow(self.letrero2)

                            self.botonGuardar = QPushButton("Guardar")
                            self.botonGuardar.setFixedWidth(170)
                            self.formulario.addWidget(self.botonGuardar)
                            self.botonGuardar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                            "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

                            self.botonLimpiar = QPushButton("Volver")
                            self.botonLimpiar.setFixedWidth(170)
                            self.formulario.addWidget(self.botonLimpiar)
                            self.botonLimpiar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                            "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

                            self.botonGuardar.clicked.connect(self.accion_botonGuardar)

                            self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

                            self.consecutivo_iniciar()
                            # limpiamos las cajas de texto
                            self.cedulaText.setText("")
                            self.placaText.setText("")
                            self.horaText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
                            self.fechaText.setText(datetime.date.today().strftime("%d/%m/%Y"))
                            self.celdaText.setText("0")

                            self.cedulaText.setText(de.documento)
                            self.placaText.setText(de.placa)
                            self.horaText.setText(de.hora)
                            self.fechaText.setText(de.fecha)
                            self.celdaText.setText(de.celda)
                            idingreso = True
                            self.celdaText.setReadOnly(True)
                            self.cedulaText.setReadOnly(True)
                            self.placaText.setReadOnly(True)
                            self.horaText.setReadOnly(True)
                            self.fechaText.setReadOnly(True)
                            self.salidaText.setReadOnly(True)
                            self.ingresoText.setReadOnly(True)
                            self.horasText.setReadOnly(True)
                            self.fechasText.setReadOnly(True)

                            # Rompemos el for
                            break
                    self.validacion = False
                    if (not idingreso)and self.salidaText.text()==''and registrado==False :
                        self.validacion=True
                        self.mensaje.setText(f"El ID de ingreso {self.ingresoText.text()} \nNo ha sido registrado")
                        self.ingresoText.setText("")
                        self.salidaText.setText("")
                        # Hacemos que la ventana se vea1
                        self.ventanaDialogo.exec_()


            if (self.salidaText!=''):


                # ___________Consecutivo inicial para entrada________
                # abrimos el archivo en modo binario
                self.file = open('Datos/Datos_Salida.txt', 'rb')

                # creamos una lista vacia
                salida = []

                while self.file:
                    # lea el archivo y traiga los datos
                    linea = self.file.readline().decode('UTF-8')

                    # elimine el ; y ponga en una posicion
                    lista = linea.split(";")

                    # se para si ya no hay mas registros
                    if linea == '':
                        break
                    # creamos un objeto tipo cliente llamado u
                    ds = Salida(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                        lista[4],
                        lista[5],
                        lista[6],
                        lista[7],
                        lista[8],
                    )
                    # Metemos el objeto en la lista usuario
                    salida.append(ds)

                self.file.close()

                # En este punto tenemos la lista de usuario con todos los usuarios
                idingreso = False
                # Variable para controlar si existe el documento

                for ds in salida:
                    # Comparemos el documento ingresado
                    # Si corresponde con el documento es el usuario correcto

                    if ds.idsalida == self.salidaText.text() and self.ingresoText.text()=='':

                        self.botonConsultar.deleteLater()

                        # linea Pendiente intentar realizar
                        self.letrero2 = QLabel()
                        self.letrero2.setText(
                            "                                                                                    ")
                        self.letrero1.setFont(QFont("league spartan", 35))
                        self.letrero2.setStyleSheet(
                            "background: rgba(76, 175, 80, 0.0);color:#EFE718; margin-left:240px;text-decoration: underline ;")

                        # Caja de modulos #2

                        # Texto informativo Nombre
                        self.cedula = QLabel("Cedula cliente: ")
                        self.cedula.setStyleSheet(
                            "background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold;")
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
                        self.placa.setStyleSheet(
                            "background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
                        self.placa.setFont(QFont("league spartan", 12))

                        # Entrada de dato Placa
                        self.placaText = QLineEdit()
                        self.placaText.setFixedWidth(170)
                        self.placaText.setFont(QFont("league spartan", 10))
                        self.placaText.setPlaceholderText("Ingrese Placa")
                        self.placaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                     "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
                        self.formulario.addRow(self.placa, self.placaText)

                        # Caja de modulos #4
                        # Texto informativo Fecha
                        self.fecha = QLabel("Fecha ingreso: ")
                        self.fecha.setStyleSheet(
                            "background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
                        self.fecha.setFont(QFont("league spartan", 12))

                        # Entrada de dato Fecha
                        self.fechaText = QLineEdit()
                        self.fechaText.setFixedWidth(170)
                        self.fechaText.setFont(QFont("league spartan", 10))
                        self.fechaText.setPlaceholderText("Ingrese Fecha")
                        self.fechaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                     "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
                        self.fechaText.setInputMask("99/99/9999")  # para mostrar las barras "/"
                        self.fechaText.setText(
                            datetime.date.today().strftime("%d/%m/%Y"))  # para mostrar la fecha actual
                        self.formulario.addRow(self.fecha, self.fechaText)

                        # Caja de modulos #5
                        # Texto informativo hora
                        self.hora = QLabel("Hora de ingreso: ")
                        self.hora.setStyleSheet(
                            "background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
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
                        self.formulario.addRow(self.hora, self.horaText)

                        # Caja de modulos #6
                        # Texto informativo Fecha
                        self.fechas = QLabel("Fecha Salida: ")
                        self.fechas.setStyleSheet(
                            "background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
                        self.fechas.setFont(QFont("league spartan", 12))

                        # Entrada de dato Fecha
                        self.fechasText = QLineEdit()
                        self.fechasText.setFixedWidth(170)
                        self.fechasText.setFont(QFont("league spartan", 10))
                        self.fechasText.setPlaceholderText("Ingrese Fecha")
                        self.fechasText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
                        self.fechasText.setInputMask("99/99/9999")  # para mostrar las barras "/"
                        self.fechasText.setText(
                            datetime.date.today().strftime("%d/%m/%Y"))  # para mostrar la fecha actual
                        self.formulario.addRow(self.fechas, self.fechasText)

                        # Caja de modulos #7
                        # Texto informativo hora
                        self.horas = QLabel("Hora de Salida: ")
                        self.horas.setStyleSheet(
                            "background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
                        self.horas.setFont(QFont("league spartan", 12))

                        # Entrada de dato Hora
                        self.horasText = QLineEdit()
                        self.horasText.setFixedWidth(170)
                        self.horasText.setFont(QFont("league spartan", 10))
                        self.horasText.setPlaceholderText("Ingrese Hora")
                        self.horasText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                     "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
                        self.horasText.setInputMask("99:99:99")  # para mostrar los dos puntos ":"
                        self.horasText.setText(datetime.datetime.now().strftime("%H:%M:%S"))  # para mostrar la
                        self.formulario.addRow(self.horas, self.horasText)

                        # Caja de modulos #8

                        # Texto informativo Celda
                        self.celda = QLabel("Celda: ")
                        self.celda.setStyleSheet(
                            "background: rgba(76, 175, 80, 0.0);margin-left:158px;font-weight: bold")
                        self.celda.setFont(QFont("league spartan", 12))

                        # Entrada de dato celda
                        self.celdaText = QLineEdit()
                        self.celdaText.setFixedWidth(170)
                        self.celdaText.setFont(QFont("league spartan", 10))
                        self.celdaText.setPlaceholderText("Ingrese Número de Celda")
                        self.celdaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                     "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
                        self.formulario.addRow(self.celda, self.celdaText)

                        # Linea Separadora
                        self.formulario.addRow(self.letrero2)


                        self.botonGuardar = QPushButton("Guardar")
                        self.botonGuardar.setFixedWidth(170)
                        self.botonGuardar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                        "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

                        self.botonLimpiar = QPushButton("Volver")
                        self.botonLimpiar.setFixedWidth(170)
                        self.formulario.addWidget(self.botonLimpiar)
                        self.botonLimpiar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                                        "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

                        self.botonGuardar.clicked.connect(self.accion_botonGuardar)

                        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)


                        # limpiamos las cajas de texto\
                        self.ingresoText.setText("")
                        self.cedulaText.setText("")
                        self.placaText.setText("")
                        self.horaText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
                        self.fechaText.setText(datetime.date.today().strftime("%d/%m/%Y"))
                        self.horasText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
                        self.fechasText.setText(datetime.date.today().strftime("%d/%m/%Y"))
                        self.celdaText.setText("0")
                        # Mostramos las preguntas en el formulario
                        self.ingresoText.setText(ds.identrada)
                        self.cedulaText.setText(ds.documento)
                        self.placaText.setText(ds.placa)
                        self.horaText.setText(ds.horai)
                        self.fechaText.setText(ds.fechai)
                        self.horasText.setText(ds.horas)
                        self.fechasText.setText(ds.fechas)
                        self.celdaText.setText(ds.celda)
                        # indicamos que encontramos el documento
                        idingreso = True
                        self.salidaText.setReadOnly(True)
                        self.ingresoText.setReadOnly(True)
                        self.cedulaText.setReadOnly(True)
                        self.placaText.setReadOnly(True)
                        self.horaText.setReadOnly(True)
                        self.fechaText.setReadOnly(True)
                        self.horasText.setReadOnly(True)
                        self.fechasText.setReadOnly(True)
                        self.celdaText.setReadOnly(True)
                        # Rompemos el for
                        break
                if (not idingreso)and self.ingresoText.text()==""and self.validacion==False:
                    self.mensaje.setText(f"El ID de salida {self.salidaText.text()} \nNo ha sido registrado")
                    self.ingresoText.setText("")
                    self.salidaText.setText("")
                    # Hacemos que la ventana se vea
                    self.ventanaDialogo.exec_()
    def accion_botonLimpiar(self):
        self.ingresoText.setText("")
        self.salidaText.setText("")
        self.cedulaText.setText("")
        self.placaText.setText("")
        self.horaText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
        self.fechaText.setText(datetime.date.today().strftime("%d/%m/%Y"))
        self.celdaText.setText("0")
        self.horasText.setText(datetime.datetime.now().strftime("%H:%M:%S"))
        self.fechasText.setText(datetime.date.today().strftime("%d/%m/%Y"))
        self.botonLimpiar.deleteLater()
        self.botonGuardar.deleteLater()
        self.ingresoText.deleteLater()
        self.cedulaText.deleteLater()
        self.placaText.deleteLater()
        self.horaText.deleteLater()
        self.fechaText.deleteLater()
        self.celdaText.deleteLater()
        self.ingreso.deleteLater()
        self.cedula.deleteLater()
        self.placa.deleteLater()
        self.hora.deleteLater()
        self.fecha.deleteLater()
        self.celda.deleteLater()
        self.letrero2.deleteLater()
        self.horas.deleteLater()
        self.fechas.deleteLater()
        self.fechasText.deleteLater()
        self.horasText.deleteLater()
        self.salidaText.setReadOnly(False)
        self.ingresoText.setReadOnly(False)
        self.salidaText.setFocus()
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




        self.botonConsultar = QPushButton("Consultar")
        self.botonConsultar.setFixedWidth(170)
        self.formulario.addWidget(self.botonConsultar)
        self.botonConsultar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")


        self.botonConsultar.clicked.connect(self.accion_botonConsultar)
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