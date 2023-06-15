from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox, QComboBox
from PyQt5 import QtCore
import datetime
from DatosEgreso import Egreso


class VentanaBl(QMainWindow):
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
        self.letrero1.setText("Registro de Egreso")


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

        #Texto informativo Id Egreso
        self.idegreso = QLabel("ID Egreso: ")
        self.idegreso.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold;margin-top:50px;")
        self.idegreso.setFont(QFont("league spartan", 12))

        # Entrada de dato Egreso
        self.idegresoText = QLineEdit()
        self.idegresoText.setFixedWidth(260)
        self.idegresoText.setFont(QFont("league spartan", 10))
        self.idegresoText.setPlaceholderText("Ingrese ID de Egreso")
        self.idegresoText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold; margin-top:50px;")
        self.formulario.addRow(self.idegreso, self.idegresoText)


        # Caja de modulos #2
        # Texto informativo fecha y hora

        self.fecha = QLabel("Fecha: ")
        self.fecha.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.fecha.setFont(QFont("league spartan", 12))

        # Entrada de dato Fecha y hora
        self.fechaText = QLineEdit()
        self.fechaText.setFixedWidth(260)
        self.fechaText.setFont(QFont("league spartan", 10))
        self.fechaText.setPlaceholderText("Ingrese Fecha de Egreso")
        self.fechaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                          "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.fechaText.setInputMask("99/99/9999")  # para mostrar las barras "/"
        self.fechaText.setText(datetime.date.today().strftime("%d/%m/%Y"))  # para mostrar la fecha actual
        self.fechaText.setReadOnly(True)

        self.formulario.addRow(self.fecha, self.fechaText)



        # Caja de modulos #3
        # Texto informativo descripción de la Egreso

        self.descripcion = QLabel("Descripcion: ")
        self.descripcion.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.descripcion.setFont(QFont("league spartan", 12))

        # Entrada de dato descripción de la pqr
        self.descripcionText = QLineEdit()
        self.descripcionText.setFixedWidth(260)
        self.descripcionText.setFont(QFont("league spartan", 10))
        self.descripcionText.setPlaceholderText("Descripcion del egreso ")
        self.descripcionText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.descripcion, self.descripcionText)

        # Caja de modulos #10
        # Texto informativo Valor

        self.valor = QLabel("Valor: ")
        self.valor.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.valor.setFont(QFont("league spartan", 12))

        # Entrada de dato Valor
        self.valorText = QLineEdit()
        self.valorText.setFixedWidth(260)
        self.valorText.setFont(QFont("league spartan", 10))
        self.valorText.setPlaceholderText("Valor del egreso ")
        self.valorText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                            "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.valor, self.valorText)



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

        self.botonlimpiar.clicked.connect(self.accion_botonlimpiar)

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


        self.consecutivo_iniciarl()

    def consecutivo_iniciarl(self):
        #___________Consecutivo inicial para entrada________
        # abrimos el archivo en modo binario
        self.file = open('Datos/Datos_Egreso.txt', 'rb')

        # creamos una lista vacia
        egreso = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            de = Egreso(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
            )
            # Metemos el objeto en la lista usuario
            egreso.append(de)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        max_idegreso = 0
        for de in egreso:
            if de.idegreso and int(de.idegreso) > max_idegreso:
                max_idegreso = int(de.idegreso)
        self.consecutivo = max_idegreso
        self.idegresoText.setText(str(self.consecutivo + 1))
        if self.idegresoText.text()=="":
            self.idegresoText.setText("1")

    def accion_botonlimpiar(self):
        self.idegresoText.setText("")
        self.descripcionText.setText("")
        self.valorText.setText("")
        self.fechaText.setText(datetime.date.today().strftime("%d/%m/%Y"))  # para mostrar la fecha actual
        self.consecutivo_iniciarl()
        self.idegresoText.setReadOnly(False)
        self.descripcionText.setReadOnly(False)
        self.fechaText.setReadOnly(False)
    def accion_botonGuardar(self):
        self.datoscorrectos = True
        # ___________Consecutivo inicial para entrada________
        # abrimos el archivo en modo binario
        self.file = open('Datos/Datos_Egreso.txt', 'rb')

        # creamos una lista vacia
        egreso = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            de = Egreso(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
            )
            # Metemos el objeto en la lista usuario
            egreso.append(de)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        for de in egreso:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto

            if de.idegreso == self.idegresoText.text():
                self.mensaje.setText(f"El Egreso con el consecutivo: {self.idegresoText.text()}\nYa se encuentra registrado")
                self.ventanaDialogo.exec_()
                self.datoscorrectos = False
                self.accion_botonlimpiar()
                break



        # Validacion si las casillas de texto estan vacias o realizado modificacion en los campos
        if self.datoscorrectos == True and (self.idegresoText.text() == '' or
                                            self.fechaText.text() == '' or
                                            self.valorText.text() == '' or
                                            self.descripcionText.text() == ''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos para guardar")

            self.ventanaDialogo.exec_()

        # Validar que usuario ingreso datos con espacios/ verdadero si tiene espacios/ falso si no tiene espacios
        if self.datoscorrectos == True and (self.fechaText.text().isspace()
                                            or self.descripcionText.text().isspace()
                                            or self.valorText.text().isspace()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha Ingresado espacios en blanco")
            self.ventanaDialogo.exec_()
        # Fin Validacion Espacios

        # Validacion si modelo es numeros/ verdadero si son numeros/falso si son letras
        if self.datoscorrectos == True and (self.idegreso.text().isalpha() or
                                            self.valorText.text().isalpha() or
                                            self.fechaText.text().isalpha()

        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha ingresado letras en los campos numericos")
            self.ventanaDialogo.exec_()

        # Validacion si en marca o en color son letras / verdadero si son letras/ falso si es numero
        if self.datoscorrectos == True and (self.descripcionText.text().isdigit()
        ):
            self.datoscorrectos = False
            self.mensaje.setText("Ha ingresador numeros en la descripcion")
            self.ventanaDialogo.exec_()
        # Fin Validacion Numeros

        #si todo esta ok guarda los datos
        if self.datoscorrectos:
            self.mensaje.setText("Datos guardados correctamente")

            self.ventanaDialogo.exec_()
            # abrimos el archivo en modo agregar
            self.file = open('Datos/Datos_Egreso.txt', 'ab')

            # Traer el texto de los Qline y los concatena con ;
            self.file.write(bytes(
                # Cajas de texto de la pestaña
                self.idegresoText.text() + ";"
                + self.fechaText.text() + ";"
                + self.descripcionText.text() + ";"
                + self.valorText.text() + "\n", encoding='UTF-8'))
            self.file.close()
            self.accion_botonlimpiar()
    def accion_botonConsultar(self):
        # datos correctos
        self.datoscorrectos = True
        # establecemos un titulo a la ventana
        self.ventanaDialogo.setWindowTitle("Consultar Ingreso")

        # validamos que se haya ingresado un documento
        if (self.idegresoText.text() == ''):
            self.datoscorrectos = False

            self.mensaje.setText("Si va a consultar una Egreso"
                                 "\nDebe primero, ingresar la id Egreso")
            self.ingresoText.setFocus()
            self.accion_botonlimpiar()
            self.ventanaDialogo.exec_()
            # si estan correctos los datos

        if (self.datoscorrectos):
            # abrimos el archivo en modo binario
            self.file = open('Datos/Datos_Egreso.txt', 'rb')

            # creamos una lista vacia
            egreso = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                de = Egreso(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                )
                # Metemos el objeto en la lista usuario
                egreso.append(de)

            self.file.close()

            # En este punto tenemos la lista de usuario con todos los usuarios

            # Variable para controlar si existe el documento
            idegreso=False
            for de in egreso:
                # Comparemos el documento ingresado
                # Si corresponde con el documento es el usuario correcto
                if de.idegreso == self.idegresoText.text():
                    # limpiamos las cajas de texto
                    self.fechaText.setText(datetime.date.today().strftime("%d/%m/%Y"))
                    self.descripcionText.setText("")
                    self.valorText.setText("")
                   

                    # Mostramos las preguntas en el formulario
                    self.idegresoText.setText(de.idegreso)
                    self.descripcionText.setText(de.descripcion)
                    self.fechaText.setText(de.fecha)
                    self.valorText.setText(de.valor)

                    # indicamos que encontramos el documento
                    idegreso = True

                    break

            if (not idegreso):
                self.mensaje.setText(f"El ID de egreso{self.idegresoText.text()} \nNo ha sido registrado")
                self.accion_botonlimpiar()
                # Hacemos que la ventana se vea
                self.ventanaDialogo.exec_()
    def accion_botoneliminar(self):
        self.datosCorrectos = True
        self.eliminar = False

        if (
                self.idegresoText.text() == ''
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Debe seleccionar un egreso válido para eliminar")
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:

            self.ventanaDialogo_eliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            self.ventanaDialogo_eliminar.resize(300, 150)

            self.ventanaDialogo_eliminar.setWindowModality(Qt.ApplicationModal)
            self.ventanaDialogo_eliminar.setWindowTitle("Eliminar")
            self.ventanaDialogo_eliminar.setWindowIcon(QIcon("imagenes/IconoGPP.jpeg"))

            self.verticalEliminar = QVBoxLayout()

            self.mensajeEliminar = QLabel("¿Estas seguro que desea eliminar este egreso?")

            self.verticalEliminar.addWidget(self.mensajeEliminar)

            # agregar las opciones de los bontes ok y cancel

            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            # agergamos opcionBox
            self.verticalEliminar.addWidget(self.opcionesBox)

            self.ventanaDialogo_eliminar.setLayout(self.verticalEliminar)

            self.ventanaDialogo_eliminar.exec_()

            if self.eliminar:

                self.file = open('Datos/Datos_Egreso.txt', 'rb')

                # creamos una lista vacia
                egreso = []

                while self.file:
                    # lea el archivo y traiga los datos
                    linea = self.file.readline().decode('UTF-8')

                    # elimine el ; y ponga en una posicion
                    lista = linea.split(";")

                    # se para si ya no hay mas registros
                    if linea == '':
                        break
                    # creamos un objeto tipo cliente llamado u
                    de = Egreso(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                    )
                    # Metemos el objeto en la lista usuario
                    egreso.append(de)

                self.file.close()

                existeDocumento = False

                # ciclo for para remover el registro de un usuario
                for de in egreso:

                    if de.idegreso == self.idegresoText.text():
                        egreso.remove(de)
                        existeDocumento = True
                        break

                self.file = open('Datos/Datos_Egreso.txt', 'wb')

                # reescribir el registro del usuario a vacio

                for de in egreso:
                    self.file.write(bytes(de.idegreso + ';'
                                          + de.fecha + ';'
                                          + de.descripcion + ';'
                                          + de.valor , encoding='UTF-8'))
                self.file.close()

                if existeDocumento:
                    self.mensaje.setText("Vehiculo eliminado correctamente.")
                    self.ventanaDialogo.exec_()
                    self.accion_botonlimpiar()
    def ok_opcion(self):
        self.ventanaDialogo_eliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogo_eliminar.close()
    def accion_botonactualizar(self):
        self.datoscorrectos = True


        # Validacion si las casillas de texto estan vacias o realizado modificacion en los campos
        if self.datoscorrectos == True and (self.idegresoText.text() == '' or
                                            self.fechaText.text() == '' or
                                            self.valorText.text() == '' or
                                            self.descripcionText.text() == ''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos para actualizar")

            self.ventanaDialogo.exec_()

        # Validar que usuario ingreso datos con espacios/ verdadero si tiene espacios/ falso si no tiene espacios
        if self.datoscorrectos == True and (self.fechaText.text().isspace()
                                            or self.descripcionText.text().isspace()
                                            or self.valorText.text().isspace()
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha Ingresado espacios en blanco")
            self.ventanaDialogo.exec_()
        # Fin Validacion Espacios

        # Validacion si modelo es numeros/ verdadero si son numeros/falso si son letras
        if self.datoscorrectos == True and (self.idegreso.text().isalpha() or
                                            self.valorText.text().isalpha() or
                                            self.fechaText.text().isalpha()

        ):
            self.datoscorrectos = False

            self.mensaje.setText("Ha ingresado letras en los campos numericos")
            self.ventanaDialogo.exec_()

        # Validacion si en marca o en color son letras / verdadero si son letras/ falso si es numero
        if self.datoscorrectos == True and (self.descripcionText.text().isdigit()
        ):
            self.datoscorrectos = False
            self.mensaje.setText("Ha ingresador numeros en la descripcion")
            self.ventanaDialogo.exec_()
        # Fin Validacion Numeros

        if self.datoscorrectos:

            self.file = open('Datos/Datos_Egreso.txt', 'rb')

            # creamos una lista vacia
            egreso = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                de = Egreso(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                )
                # Metemos el objeto en la lista usuario
                egreso.append(de)

            self.file.close()

            existeDocumento = False

            for de in egreso:

                if de.idegreso == self.idegresoText.text():
                    de.descripcion = self.descripcionText.text()
                    de.fecha = self.fechaText.text()
                    de.valor = self.valorText.text()

                    existeDocumento = True
                    break

            if (
                    not existeDocumento
            ):
                self.mensaje.setText(f"No existe egreso con esa ID\n"
                                     f"{self.idegresoText.text()}")
                self.ventanaDialogo.exec_()

            # Abrimos el archivo en modo agregar
            self.file = open('Datos/Datos_Egreso.txt', 'wb')

            for de in egreso:
                # trae el texto de los Qline y los concatena
                self.file.write(bytes(de.idegreso + ";" +
                                      de.fecha + ";" +
                                      de.descripcion + ";" +
                                      de.valor, encoding='UTF-8'))
            self.file.close()

            if (
                    existeDocumento
            ):
                self.mensaje.setText("Egreso actualizado correctamente!")
                self.ventanaDialogo.exec_()
                self.accion_botonlimpiar()

            self.file = open('Datos/Datos_Egreso.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')

                if linea == '':
                    break
            self.file.close()

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
            self.accion_botonlimpiar()
