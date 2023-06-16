from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox, QComboBox
from PyQt5 import QtCore
import datetime
from DatosUsuario import Usuarios
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
        # Direccion de un layout izquierda o derecha
        self.barraHerramientas.setLayoutDirection(Qt.RightToLeft)
        # Activar Barra De herramientas
        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraDeHerramientas)

        self.vertical1=QVBoxLayout()
        self.formulario = QFormLayout()


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

        #Texto informativo usuario
        self.usuario = QLabel("Usuario: ")
        self.usuario.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold;margin-top:50px;")
        self.usuario.setFont(QFont("league spartan", 12))
        # Entrada de dato cedula
        self.usuarioText = QLineEdit()
        self.usuarioText.setFixedWidth(260)
        self.usuarioText.setFont(QFont("league spartan", 10))
        self.usuarioText.setPlaceholderText("Usuario")
        self.usuarioText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                       "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold; margin-top:50px;")
        self.formulario.addRow(self.usuario, self.usuarioText)

        # Texto informativo contrasena
        self.contra = QLabel("Contraseña: ")
        self.contra.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.contra.setFont(QFont("league spartan", 12))
        # Entrada de dato contrasena
        self.contraText = QLineEdit()
        self.contraText.setFixedWidth(260)
        self.contraText.setFont(QFont("league spartan", 10))
        self.contraText.setPlaceholderText("Contraseña")
        self.contraText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                      "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.contra, self.contraText)

        # Texto informativo fecha Respuesta
        self.tipoU = QLabel("Tipo de usuario: ")
        self.tipoU.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:100px;font-weight: bold")
        self.tipoU.setFont(QFont("league spartan", 12))

        # Entrada de dato tipo de usuario
        self.tipoUText = QComboBox()
        self.tipoUText.addItem("Administrador")
        self.tipoUText.addItem("Basico")
        self.tipoUText.setFixedWidth(260)
        self.tipoUText.setFont(QFont("league spartan", 10))
        self.tipoUText.setPlaceholderText("Solucionado o pendiente")
        self.tipoUText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario.addRow(self.tipoU, self.tipoUText)
        self.formulario.addRow(self.letrero2)

        self.vertical1.addLayout(self.formulario)

        self.formulario1=QFormLayout()
        #Linea Separadora
        self.formulario1.setContentsMargins(170,0,0,0)
        self.botonGuardar = QPushButton("Guardar")
        self.botonGuardar.setFixedWidth(170)
        self.botonGuardar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonConsultar = QPushButton("Consultar")
        self.botonConsultar.setFixedWidth(170)
        self.botonConsultar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.formulario1.addRow(self.botonGuardar, self.botonConsultar)

        self.botonActualizar = QPushButton("Actualizar")
        self.botonActualizar.setFixedWidth(170)
        self.botonActualizar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                           "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedWidth(170)
        self.botonEliminar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                           "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.formulario1.addRow(self.botonActualizar, self.botonEliminar)



        self.botonGuardar.clicked.connect(self.accion_botonGuardar)
        self.botonConsultar.clicked.connect(self.accion_botonConsultar)
        self.botonActualizar.clicked.connect(self.accion_botonActualizar)
        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        self.vertical1.addLayout(self.formulario1)

        self.horizontal=QHBoxLayout()
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(170)
        self.horizontal.addWidget(self.botonLimpiar)
        self.botonLimpiar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                        "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")
        self.botonLimpiar.clicked.connect(self.accion_botonlimpiar)
        self.vertical1.addLayout(self.horizontal)
        self.vertical1.addSpacing(170)
        self.fondo.setLayout(self.vertical1)

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
        self.usuarioText.setText("")
        self.contraText.setText("")
        self.usuarioText.setFocus()
        self.usuarioText.setReadOnly(False)
        self.contraText.setReadOnly(False)

    def accion_botonGuardar(self):
        self.datoscorrectos = True
        self.file = open('Datos/Datos_usuarios.txt', 'rb')

        # creamos una lista vacia
        usuarios = []

        while self.file:
            # lea el archivo y traiga los datos
            linea = self.file.readline().decode('UTF-8')

            # elimine el ; y ponga en una posicion
            lista = linea.split(";")

            # se para si ya no hay mas registros
            if linea == '':
                break
            # creamos un objeto tipo cliente llamado u
            du = Usuarios(
                lista[0],
                lista[1],
                lista[2],
            )
            # Metemos el objeto en la lista usuario
            usuarios.append(du)

        self.file.close()

        # En este punto tenemos la lista de usuario con todos los usuarios

        # Variable para controlar si existe el documento

        for du in usuarios:
            # Comparemos el documento ingresado
            # Si corresponde con el documento es el usuario correcto

            if du.usuario == self.usuarioText.text():
                self.mensaje.setText(f"El usuario: {self.usuarioText.text()}\nYa se encuentra registrado")
                self.ventanaDialogo.exec_()
                self.datoscorrectos = False
                self.accion_botonlimpiar()
                break

        print("Inicia Validacion si los campos estan vacios")
        # Validacion si las casillas de texto estan vacias o realizado modificacion en los campos
        if self.datoscorrectos == True and (self.usuarioText.text() == '' or
                                            self.contraText.text() == ''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos para guardar")

            self.ventanaDialogo.exec_()
        print("Inicia Validacion si los campos tienen espacios")
        # Validar que usuario ingreso datos con espacios/ verdadero si tiene espacios/ falso si no tiene espacios
        if self.datoscorrectos == True and (self.usuarioText.text().isspace()
                                            or self.contraText.text().isspace()
        ):
            self.datoscorrectos = False
            self.mensaje.setText("Ha Ingresado espacios en blanco")
            self.ventanaDialogo.exec_()
        # Fin Validacion Espacios

        if self.datoscorrectos:
            # abrimos el archivo en modo agregar
            self.file = open('Datos/Datos_usuarios.txt', 'ab')

            # Traer el texto de los Qline y los concatena con ;
            self.file.write(bytes(
                # Cajas de texto de la pestaña
                self.usuarioText.text() + ";"
                + self.contraText.text() + ";"
                + self.tipoUText.currentText() + "\n", encoding='UTF-8'))
            self.file.close()
            self.mensaje.setText("Datos guardados correctamente")
            self.ventanaDialogo.exec_()
            self.accion_botonlimpiar()
    def accion_botonConsultar(self):
        # datos correctos
        self.datoscorrectos = True
        # establecemos un titulo a la ventana
        self.ventanaDialogo.setWindowTitle("Consultar Ingreso")

        # validamos que se haya ingresado un documento
        if (self.usuarioText.text() == ''):
            self.datoscorrectos = False

            self.mensaje.setText("Si va a consultar un usuario"
                                 "\nDebe primero, ingresar el usuario")
            self.ingresoText.setFocus()
            self.accion_botonlimpiar()
            self.ventanaDialogo.exec_()
            # si estan correctos los datos

        if (self.datoscorrectos):
            # abrimos el archivo en modo binario
            self.file = open('Datos/Datos_usuarios.txt', 'rb')

            # creamos una lista vacia
            usuarios = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                du = Usuarios(
                    lista[0],
                    lista[1],
                    lista[2],
                )
                # Metemos el objeto en la lista usuario
                usuarios.append(du)

            self.file.close()

            # En este punto tenemos la lista de usuario con todos los usuarios

            # Variable para controlar si existe el documento
            existeUsuario=False
            for du in usuarios:
                # Comparemos el documento ingresado
                # Si corresponde con el documento es el usuario correcto
                if du.usuario == self.usuarioText.text():
                    # limpiamos las cajas de texto
                    self.contraText.setText("")

                    # Mostramos las preguntas en el formulario
                    self.contraText.setText(du.contra)

                    if du.tipoU=="Administrador":
                        self.tipoUText.setCurrentIndex(0)
                    elif du.tipoU=="Basico":
                        self.tipoUText.setCurrentIndex(1)

                    # indicamos que encontramos el documento
                    existeUsuario = True
                    self.usuarioText.setReadOnly(True)
                    break

            if (not existeUsuario):
                self.mensaje.setText(f"El usuario {self.usuarioText.text()} \nNo ha sido registrado")
                self.accion_botonlimpiar()
                # Hacemos que la ventana se vea
                self.ventanaDialogo.exec_()
    def accion_botonActualizar(self):
        self.datoscorrectos = True

        if self.datoscorrectos == True and (
                self.usuarioText.text() == '' or
                self.contraText.text() == '' or
                self.tipoUText.currentText() == ''
        ):
            self.datoscorrectos = False
            # cambiamos mensaje
            self.mensaje.setText("Debe ingresar todos los campos para guardar")
            self.ventanaDialogo.exec_()

        #Validar que usuario ingreso datos con espacios/ verdadero si tiene espacios/ falso si no tiene espacios
        if self.datoscorrectos == True and (self.usuarioText.text().isspace()
                or self.contraText.text().isspace()
        ):
            self.datoscorrectos = False
            self.mensaje.setText("Ha Ingresado espacios en blanco")
            self.ventanaDialogo.exec_()
        #Fin Validacion Espacios

        if self.datoscorrectos:

            self.file = open('Datos/Datos_usuarios.txt', 'rb')
            # creamos una lista vacia
            usuarios = []

            while self.file:
                # lea el archivo y traiga los datos
                linea = self.file.readline().decode('UTF-8')

                # elimine el ; y ponga en una posicion
                lista = linea.split(";")

                # se para si ya no hay mas registros
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                du = Usuarios(
                    lista[0],
                    lista[1],
                    lista[2],
                )
                # Metemos el objeto en la lista usuario
                usuarios.append(du)

            self.file.close()

            existeDocumento = False

            for u in usuarios:

                if u.usuario == self.usuarioText.text():
                    u.contra = self.contraText.text()
                    u.tipoU = self.tipoUText.currentText()

                    existeDocumento = True
                    break

            if (
                    not existeDocumento
            ):
                self.mensaje.setText(f"No existe usuario\n"
                                     f"{self.cedulaText.text()}")
                self.ventanaDialogo.exec_()

            # Abrimos el archivo en modo agregar
            self.file = open('Datos/Datos_usuarios.txt', 'wb')
            for u in usuarios:
                # trae el texto de los Qline y los concatena
                self.file.write(bytes(u.usuario + ";" +
                                      u.contra + ";" +
                                      u.tipoU, encoding='UTF-8'))
            self.file.close()

            if existeDocumento:
                self.mensaje.setText("Usuario actualizado correctamente!")
                self.ventanaDialogo.exec_()
                self.accion_botonLimpiar()

            self.file = open('Datos/Datos_usuarios.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()
    def accion_botonEliminar(self):
        self.datosCorrectos = True
        self.eliminar = False

        if (
                self.usuarioText.text() == ''
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Debe seleccionar un usuario válido")
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:
            self.ventanaDialogo_eliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
            self.ventanaDialogo_eliminar.resize(300, 150)

            self.ventanaDialogo_eliminar.setWindowModality(Qt.ApplicationModal)
            self.ventanaDialogo_eliminar.setWindowTitle("Eliminar")
            self.ventanaDialogo_eliminar.setWindowIcon(QIcon("imagenes/IconoGPP.jpeg"))

            self.verticalEliminar = QVBoxLayout()

            self.mensajeEliminar = QLabel("¿Estas seguro que desea eliminar este usuario?")

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

                self.file = open('Datos/Datos_usuarios.txt', 'rb')

                # creamos una lista vacia
                usuarios = []

                while self.file:
                    # lea el archivo y traiga los datos
                    linea = self.file.readline().decode('UTF-8')

                    # elimine el ; y ponga en una posicion
                    lista = linea.split(";")

                    # se para si ya no hay mas registros
                    if linea == '':
                        break
                    # creamos un objeto tipo cliente llamado u
                    du = Usuarios(
                        lista[0],
                        lista[1],
                        lista[2],
                    )
                    # Metemos el objeto en la lista usuario
                    usuarios.append(du)

                self.file.close()

                existeDocumento = False

                # ciclo for para remover el registro de un usuario
                for u in usuarios:
                    if u.usuario == self.usuarioText.text():
                        usuarios.remove(u)
                        existeDocumento = True
                        break

                self.file = open('Datos/Datos_usuarios.txt', 'wb')

                # reescribir el registro del usuario a vacio
                for u in usuarios:
                    self.file.write(bytes(u.usuario + ';'
                                          + u.contra + ';'
                                          + u.tipoU, encoding='UTF-8'))
                self.file.close()

                if existeDocumento:
                    self.mensaje.setText("Usuario eliminado correctamente.")
                    self.ventanaDialogo.exec_()
                    self.accion_botonLimpiar()
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
    def ok_opcion(self):
        self.ventanaDialogo_eliminar.close()
        self.eliminar = True
    def cancel_opcion(self):
        self.ventanaDialogo_eliminar.close()
