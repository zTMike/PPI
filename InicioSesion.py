import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDesktopWidget, QLabel, QFormLayout, QGridLayout, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QAction, QToolBar, QTabWidget, QMessageBox, QDialog, \
    QDialogButtonBox
from PyQt5 import QtCore

import MenuAdmin
import MenuBasic
from MenuBasic import Menu
from MenuAdmin import Menu
from DatosUsuario import Usuarios
from  Ayudas import Ayuda







class iniciodesesion(QMainWindow):
    def __init__(self, parent=None):
        super(iniciodesesion, self).__init__(parent)

        self.setWindowTitle("Gesto Parqueadero")

        self.ancho = 700
        self.alto = 700

        self.resize(self.ancho, self.alto)
        # lineas para hacer que la ventana salga en el centro

        # pantalla traiga frame geometia
        self.pantalla = self.frameGeometry()

        self.setStyleSheet("background-color:white; border-color:Black;")

        #Quitar ventana de windows
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
        #definir ventana interna como ventana central
        self.setCentralWidget(self.interna)

        self.fondo = QLabel(self)
        self.imagenFondo=QPixmap('imagenes/fondo.png')
        self.fondo.setPixmap(self.imagenFondo)
        #que la imagen se  escale o se ajuste
        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(),self.imagenFondo.height())

        self.setCentralWidget(self.fondo)


        #crear toolbar o menu
        self.barraHerramientas = QToolBar("Barra de herramientas")

        #establecer tamaño de los iconos
        self.barraHerramientas.setIconSize(QSize(40, 40))
        #agregar la barra de herramientas
        self.addToolBar(self.barraHerramientas)
        #CREAR NUEVOS ELEMENTOS PARA LA TOOLBAR

        self.exp1=QAction(QIcon("imagenes/cerrar.png"), "Cerrar", self)
        self.barraHerramientas.addAction(self.exp1)

        self.exp1=QAction(QIcon("imagenes/minimizar.png"), "Minimizar", self)

        self.barraHerramientas.setStyleSheet("background-color:#d9d9d9;")


        self.barraHerramientas.addAction(self.exp1)

        #que la toolbar no se mueva
        self.barraHerramientas.setMovable(False)
        #Direccion de un layout izqueirda o derecha
        self.barraHerramientas.setLayoutDirection(Qt.RightToLeft)
        #Activar Barra De herramientas
        self.barraHerramientas.actionTriggered[QAction].connect(self.accion_barraDeHerramientas)

        self.formulario = QFormLayout()

        self.interna.setLayout(self.formulario)



        self.letrero1 = QLabel()
        self.letrero1.setText("Gestor Parqueadero")

        self.letrero1.setFont(QFont("league spartan", 29))
        self.letrero1.setAlignment(Qt.AlignCenter)

        self.letrero1.setStyleSheet("background: rgba(76, 175, 80, 0.0); margin-bottom:80px; margin-top:90px;font-weight: bold")
        self.formulario.addRow(self.letrero1)


        self.letrero2 = QLabel()

        self.letrero2.setText("Inicio de Sesión")

        self.letrero2.setFont(QFont("league spartan", 20))
        self.letrero2.setAlignment(Qt.AlignCenter)

        self.letrero2.setStyleSheet("background: rgba(76, 175, 80, 0.0); opacity:0.6; color:black; margin-bottom:30px;font-weight: bold")
        self.formulario.addRow(self.letrero2)

        #Cajas Usuario

        self.usuario = QLabel("Usuario:")
        self.usuario.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:240px;font-weight: bold")
        self.usuario.setFont(QFont("league spartan", 12))



        # se crea campo para ingresar usuario
        self.usuarioText = QLineEdit()

       # ancho del campo
        self.usuarioText.setFixedWidth(170)
        self.usuarioText.setFont(QFont("league spartan", 10))
        self.usuarioText.setPlaceholderText("Ingrese su usuario")
        self.usuarioText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")


        self.formulario.addRow(self.usuario,self.usuarioText)

        # Cajas Contraseña

        self.contraseña = QLabel("Contraseña:")
        self.contraseña.setStyleSheet("background: rgba(76, 175, 80, 0.0);margin-left:240px;font-weight: bold")
        self.contraseña.setFont(QFont("league spartan", 12))

        # se crea campo para ingresar numero
        self.contraseñaText = QLineEdit()
        self.contraseñaText.setEchoMode(QLineEdit.Password)
        self.contraseñaText.setPlaceholderText("Ingrese su contraseña")
        self.contraseñaText.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        # ancho del campo
        self.contraseñaText.setFixedWidth(170)
        self.contraseñaText.setFont(QFont("league spartan", 10))
        #agregar a formulario
        self.formulario.addRow(self.contraseña,self.contraseñaText)

        self.botonIngresar = QPushButton("Ingresar")
        self.botonIngresar.setFixedWidth(170)
        self.formulario.addWidget(self.botonIngresar)
        self.botonIngresar.setStyleSheet("background-color:White; color:Black; padding:5px;"
                                         "border:solid; border-width:1px; border-color:#EFE718;font-weight: bold")

        self.botonIngresar.clicked.connect(self.accion_botonIngresar)

        #self.botonCambiarclave = QPushButton("Olvide mi contraseña")
        #self.botonCambiarclave.setFixedWidth(170)
        #self.formulario.addWidget(self.botonCambiarclave)
        #self.botonCambiarclave.setStyleSheet("background: rgba(76, 175, 80, 0.0); color:Black; padding:5px;"
                                         #"font-weight: bold; text-decoration: underline ;")



        #self.botonCambiarclave.clicked.connect(self.accion_botonCambiarclave)

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



    def accion_botonIngresar (self):
        # datos correctos
        self.datoscorrectos = True
        # establecemos un titulo a la ventana
        self.ventanaDialogo.setWindowTitle("Datos Contraseña")

        # validamos que se haya ingresado un documento
        if (self.usuarioText.text() == '' and self.contraseñaText.text()== '' ):
            self.datoscorrectos = False

            self.mensaje.setText("Ingrese un usuario y contraseña")
            self.usuarioText.setFocus()
            self.ventanaDialogo.exec_()
            # si estan correctos los datos

        if (self.datoscorrectos):
            # abrimos el archivo  en modo binario
            self.file = open('Datos/Datos_usuarios.txt', 'rb')

            # creamos una lista vacia
            usuario = []

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
                usuario.append(du)
            self.file.close()

            # En este punto tenemos la lista de usuario con todos los usuarios

            # Variable para controlar si existe el documento
            datos = False
            #Validar tipo usuario 3 es tipo falto
            self.tipodeusuario=3
            for du in usuario:
                # Comparemos el documento ingresado
                # Si corresponde con el documento es el usuario correcto
                if (du.usuario == self.usuarioText.text() and du.contra == self.contraseñaText.text()):
                            print("Usuario OK")
                            self.tipodeusuario=int(du.tipoU)
                            print(self.tipodeusuario)
                            datos=True
                            break
                            print(datos)

            self.admin = int(1)
            self.basic = int(0)


            if self.tipodeusuario==self.admin:
                print("Admin")
                self.ventana2 = MenuAdmin.Menu(self)
                self.ventana2.show()
                Ayuda.TipoUsuario="Admin"
                # inicio esconderse
                self.hide()
            elif(self.tipodeusuario==self.basic):
                print("Basico")
                self.ventana2 = MenuBasic.Menu(self)
                self.ventana2.show()
                Ayuda.TipoUsuario = "Basic"
                # inicio esconderse
                self.hide()

            self.usuarioText.setText("")
            self.contraseñaText.setText("")

            print(datos)

            if (datos==False):
                self.mensaje.setText("Usuario O Contraseña incorrecto")
                self.contraseñaText.setText("")
                self.usuarioText.setText("")
                self.usuarioText.setFocus()

                # Hacemos que la ventana se vea
                self.ventanaDialogo.exec_()

    def accion_barraDeHerramientas(self, option):
        #escodase ventana

        #validar exprecion
        if option.text()=="Cerrar":
            # crar ventana interna
            self.iniciodesesion.close()

        if option.text() == "Minimizar":
            # crar ventana interna
            self.showMinimized()





  
        
        























if __name__ == '__main__':

    #creamos una aplicacion pyqt5
    aplicacion1=QApplication(sys.argv)

    #creamos un objeto de tipo ventana1
    inicio=iniciodesesion()

    #indicamos que la ventana se vea
    inicio.show()

    #indicamos que la ventana se deje cerrar
    sys.exit(aplicacion1.exec_())



