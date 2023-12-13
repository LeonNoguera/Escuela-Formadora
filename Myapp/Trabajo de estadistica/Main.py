
from Proyecto import *
import sys
from PyQt5.QtWidgets import QMainWindow,QDialog,QMessageBox,QApplication,QLineEdit,QSpacerItem,QSizePolicy,QPushButton

vertical=10
mylista=list()
listax=list()
listay=list()
boton=0

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_resultado.hide()
        




        #==============Llamado a funciones=============
        self.ui.btn_siguiente.clicked.connect(lambda: self.construir())
        self.ui.btn_resultado.clicked.connect(lambda: self.resultado())
    





        #=============Funciones=========================
    def construir(self):
        global mylista
        global vertical
        #self.ui.btn_resultado.show()
        try:
            self.n=int(self.ui.line_n.text())
            self.x=int(self.ui.line_x.text())

            class Login(QDialog,Window):
                def __init__(self,vueltas):
                    QDialog.__init__(self)
                    self.setWindowTitle("Proyecto")
                    self.setStyleSheet('background-color: rgb(0, 111, 0);')

                    self.vueltas=vueltas
                    btn_ok=QPushButton("OK",self)
                    btn_ok.setGeometry(10,10,40,20)
                    btn_ok.clicked.connect(lambda: cerrar())
                    btn_ok.setStyleSheet('background-color: rgb(0, 166, 80);')

                    vertical=45
                    for i in range(self.vueltas):
                        k=f"linex{i}"
                        g=f"liney{i}"
                        i=str(i)
                        x=QLineEdit("",self)
                        x.setObjectName(k)
                        x.setGeometry(30,vertical,40,20)
                        y=QLineEdit("",self)
                        y.setObjectName(g)
                        y.setGeometry(140,vertical,40,20)
                        vertical=vertical + 25
                        
                        mylista.append((k,g))

                        def cerrar():
                            global listax
                            global listay
                            global mylista
                            global boton
                            
                            boton=1
                            
                            
                            
                            
                            
                            for variable in mylista:
                                xx,yy=variable


                                x=self.findChild(QLineEdit,xx).text()
                                y=self.findChild(QLineEdit,yy).text()
                                listax.append(x)
                                listay.append(y)

                            print(listax)   
                            print(listay)
                            
                            self.close()        
            self.mio=Login(self.n) 
            self.mio.show()
            self.mio.exec_() 
                   

        except:         
        
            QMessageBox.information(self,"Atencion","Solo se permiten enteros")


        if boton==1:
            self.ui.btn_resultado.show()
            self.ui.btn_siguiente.hide()


    def resultado(self):
        x=0
        x2=0
        y=0
        y2=0
        xy=0
        
        for i in listax:
            i=float(i)
            x=x+i
        x=str(x)
        for i in listax:
            i=float(i)
            x2=x2+i**2
        x2=str(x2)
        for i in listay:
            i=float(i)
            y=y+i
        y=str(y)
        for i in listay:
            i=float(i)
            y2=y2+i**2
        y2=str(y2)
        for w,q in zip(listax,listay):
            w=float(w)
            q=float(q)
            xy=xy+w*q
        xy=str(xy)
        
        self.ui.label_1.setText(x)
        self.ui.label_2.setText(x2)
        self.ui.label_3.setText(y)
        self.ui.label_4.setText(y2)
        self.ui.label_5.setText(xy)
        x2=float(x2)
        x=float(x)
        y2=float(y2)
        y=float(y)
        xy=float(xy)
        sxx=x2-x**2/10
        sxy=xy-x*y/10
        syy=y2-y**2/10
        sxx=str(sxx)
        sxy=str(sxy)
        syy=str(syy)
        self.ui.label_6.setText(sxx)
        self.ui.label_7.setText(sxy)
        self.ui.label_8.setText(syy)
        sxx=float(sxx)
        sxy=float(sxy)
        syy=float(syy)
        p=self.ui.line_n.text()
        r=self.ui.line_x.text()
        p=float(p)
        r=float(r)
        
        b=sxy/sxx
        b=str(b)
        self.ui.label_9.setText(b)
        b=float(b)
        t=y/p
        f=x/p
        v=b*f
        a=t-v
        a=str(a)
        
        
        self.ui.label_10.setText(a)
        a=float(a)
        
        yyy=a+b*r
        yyy=str(yyy)
        self.ui.label_11.setText(yyy)
        

        cu=sxy**2
        div=cu/sxx
        scr=syy-div
        scr=str(scr)
        self.ui.label_12.setText(scr)
            
       
            


if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Window()
    ventana.show()
    exit(app.exec_())