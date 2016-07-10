# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 16:52:51 2016

@author: jimmy_osma
"""

from qtpy.QtGui import (QIntValidator, QIcon)
from qtpy.QtWidgets import (QApplication, QMainWindow, QFormLayout, QGridLayout,QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit)

class MainWidget(QWidget):
    
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        
        #Widgets
        self.label_Title1 = QLabel()
        self.label_Title1.setText("INGRESE LOS DATOS")
        self.label_Title2 = QLabel()
        self.label_Title2.setText("DATOS BOMBILLOS ESTANDAR")
        self.label_Title3 = QLabel()
        self.label_Title3.setText("DATOS BOMBILLOS LED")
        
        self.label_Data1 = QLabel()
        self.label_Data1.setText("Costo de la electricidad (kW/hora)")
        self.label_Data2 = QLabel()
        self.label_Data2.setText("Numero de bombillos a reemplazar")
        self.label_Data3 = QLabel()
        self.label_Data3.setText("Vatios del bombillo existente")
        self.label_Data4 = QLabel()
        self.label_Data4.setText("Numero de Horas por Dia encendido")
        self.label_Data5 = QLabel()
        self.label_Data5.setText("Vida util bombillo actual")
        self.label_Data6 = QLabel()
        self.label_Data6.setText("Costo Bombillo actual")
        self.label_Data7 = QLabel()
        self.label_Data7.setText("Costo estimado mantenimiento por bombillo")
        self.label_Data8 = QLabel()
        self.label_Data8.setText("Vatios del bombillo LED")
        self.label_Data9 = QLabel()
        self.label_Data9.setText("Vida util estimada del bombillo")
        self.label_Data10 = QLabel()
        self.label_Data10.setText("Costo del bombillo led")
        
        
        #Widgets Titulos del Form
        self.label_Titlef1 = QLabel()
        self.label_Titlef1.setText("INFORMACION DE COSTOS CALCULADOS")
        self.label_Titlef2 = QLabel()
        self.label_Titlef2.setText("INFORMACION DE AHORROS CALCULADOS")
        
        self.line_Data1 = QLineEdit()
        #self.line_Data1.setValidator()
        self.line_Data2 = QLineEdit()
        self.line_Data2.setValidator(QIntValidator())
        self.line_Data3 = QLineEdit()
        self.line_Data3.setValidator(QIntValidator())
        self.line_Data4 = QLineEdit()
        self.line_Data4.setValidator(QIntValidator())
        self.line_Data5 = QLineEdit()
        self.line_Data5.setValidator(QIntValidator())
        self.line_Data6 = QLineEdit()
        #self.line_Data6.setValidator()
        self.line_Data7 = QLineEdit()
        #self.line_Data7.setValidator()
        self.line_Data8 = QLineEdit()
        #self.line_Data8.setValidator()
        self.line_Data9 = QLineEdit()
        #self.line_Data9.setValidator()
        self.line_Data10 = QLineEdit()
        #self.line_Data10.setValidator()
        
        #Widget Informacion Calculada Form1 Costos
        self.line_Inf1 = QLineEdit()
        self.line_Inf1.setValidator(QIntValidator())
        self.line_Inf2 = QLineEdit()
        self.line_Inf2.setValidator(QIntValidator())
        self.line_Inf3 = QLineEdit()
        self.line_Inf3.setValidator(QIntValidator())
        self.line_Inf4 = QLineEdit()
        self.line_Inf4.setValidator(QIntValidator())
        self.line_Inf5 = QLineEdit()
        self.line_Inf5.setValidator(QIntValidator())
        self.line_Inf6 = QLineEdit()
        self.line_Inf6.setValidator(QIntValidator())
        self.line_Inf7 = QLineEdit()
        self.line_Inf7.setValidator(QIntValidator())
        self.line_Inf8 = QLineEdit()
        self.line_Inf8.setValidator(QIntValidator())
        self.line_Inf9 = QLineEdit()
        self.line_Inf9.setValidator(QIntValidator())
        
        #Widget Informacion Calculada Form2 Ahorros
        self.line_Sav1 = QLineEdit()
        self.line_Sav1.setValidator(QIntValidator())
        self.line_Sav2 = QLineEdit()
        self.line_Sav2.setValidator(QIntValidator())
        self.line_Sav3 = QLineEdit()
        self.line_Sav3.setValidator(QIntValidator())
        self.line_Sav4 = QLineEdit()
        self.line_Sav4.setValidator(QIntValidator())
        self.line_Sav5 = QLineEdit()
        self.line_Sav5.setValidator(QIntValidator())
        self.line_Sav6 = QLineEdit()
        self.line_Sav6.setValidator(QIntValidator())
        
        
        self.button_Calc = QPushButton('Calcular Ahorro', parent=self)
        self.button_Impr = QPushButton('Imprimir', parent=self)
        
        #Layouts
        layout =  QGridLayout()
        layout.addWidget(self.label_Title1,0,0)
        layout.addWidget(self.label_Data1,1,0)
        layout.addWidget(self.line_Data1,1,1)
        layout.addWidget(self.label_Title2,2,0)
        layout.addWidget(self.label_Data2,3,0)
        layout.addWidget(self.line_Data2,3,1)
        layout.addWidget(self.label_Data5,3,2)
        layout.addWidget(self.line_Data5,3,3)
        layout.addWidget(self.label_Data3,4,0)
        layout.addWidget(self.line_Data3,4,1)
        layout.addWidget(self.label_Data6,4,2)
        layout.addWidget(self.line_Data6,4,3)
        layout.addWidget(self.label_Data4,5,0)
        layout.addWidget(self.line_Data4,5,1)
        layout.addWidget(self.label_Data7,5,2)
        layout.addWidget(self.line_Data7,5,3)
        layout.addWidget(self.label_Title3,6,0)
        layout.addWidget(self.label_Data8,7,0)
        layout.addWidget(self.line_Data8,7,1)
        layout.addWidget(self.label_Data10,7,2)
        layout.addWidget(self.line_Data10,7,3)
        layout.addWidget(self.label_Data9,8,0)
        layout.addWidget(self.line_Data9,8,1)
        layout.addWidget(self.button_Calc,8,3)
        
        layout1 = QFormLayout()
        layout1.addRow("Horas por año",self.line_Inf1)
        layout1.addRow("Costo de Energia por Dia",self.line_Inf2)
        layout1.addRow("Costo de Energia por Año",self.line_Inf3)
        layout1.addRow("Costo total de la Compra",self.line_Inf4)
        layout1.addRow("Costo Total de la compra con mantenimiento",self.line_Inf5)
        layout1.addRow("Costo Reemplazo Actuales Año",self.line_Inf6)
        layout1.addRow("Costo Energia por Dia LED",self.line_Inf7)
        layout1.addRow("Costo de Energia por Año LED",self.line_Inf8)
        layout1.addRow("Costo Total de la Compra LED",self.line_Inf9)
        
        layout2 = QFormLayout()
        layout2.addRow("Ahorro Energia Anual",self.line_Sav1)
        layout2.addRow("Ahorro Energia Mensual",self.line_Sav2)
        layout2.addRow("Periodo Retorno Inversion en Años",self.line_Sav3)
        layout2.addRow("Periodo Retorno Inversion en Meses",self.line_Sav4)
        layout2.addWidget(self.button_Impr)
        
        #Layout Horizontal Titulos del Form
        self.LayoutTitle = QHBoxLayout()
        self.LayoutTitle.addWidget(self.label_Titlef1)
        self.LayoutTitle.addWidget(self.label_Titlef2)

        ### Layout HOrizontal que une los dos Form
        self.LayoutForm = QHBoxLayout() 
        self.LayoutForm.addLayout(layout1)
        self.LayoutForm.addLayout(layout2)
        
        ## LAyout Vertical Final
        self.myLayout = QVBoxLayout()
        self.myLayout.setMargin(20)
        self.myLayout.addLayout(layout)
        self.myLayout.addLayout(self.LayoutTitle)
        self.myLayout.addLayout(self.LayoutForm)
       
        self.setLayout(self.myLayout)
        
        # Signals
        self.button_Calc.clicked.connect(self.result_method)
        
    def result_method(self):
        v_Data1 = self.line_Data1.text()
        v_Data2 = self.line_Data2.text()
        v_Data3 = self.line_Data3.text()
        v_Data4 = self.line_Data4.text()
        v_Data5 = self.line_Data5.text()
        v_Data6 = self.line_Data6.text()
        v_Data7 = self.line_Data7.text() 
        v_Data8 = self.line_Data8.text()
        v_Data9 = self.line_Data9.text()
        v_Data10 = self.line_Data10.text()
        
        #Calculo Informacion de costos Form1
        v_Inf1 = int(v_Data4)  * (365)
        self.line_Inf1.setText(str(v_Inf1))
        v_Inf2 = ((int(v_Data3) * int(v_Data4))/100) * int(v_Data1)
        self.line_Inf2.setText(str(v_Inf2))
        v_Inf3 = v_Inf2 * 365
        self.line_Inf3.setText(str(v_Inf3))
        v_Inf4 = int(v_Data2) * int(v_Data6)
        self.line_Inf4.setText(str(v_Inf4))
        v_Inf5 = v_Inf4 + (int(v_Data2) * int(v_Data7))
        self.line_Inf5.setText(str(v_Inf5))
        #v_Inf6 = 
        v_Inf7 = ((int(v_Data8) * int(v_Data4))/100) * int(v_Data1)
        self.line_Inf7.setText(str(v_Inf7))
        v_Inf8 = v_Inf7 * 365
        self.line_Inf8.setText(str(v_Inf8))
        v_Inf9 = (int(v_Data2) * int(v_Data10))
        self.line_Inf9.setText(str(v_Inf9))
        
        #Calculo Informacion de Ahorros Form2
        v_Sav1 = v_Inf3 - v_Inf8
        self.line_Sav1.setText(str(v_Sav1))
        v_Sav2 = (v_Inf2 * 30) - (v_Inf7 * 30)
        self.line_Sav2.setText(str(v_Sav2))
        v_Sav3 = v_Inf9 / v_Sav1
        self.line_Sav3.setText(str(v_Sav3))
        v_Sav4 = v_Inf9 / v_Sav2
        self.line_Sav4.setText(str(v_Sav4))
        
        
        
        
        
        
        

class MainWindow(QMainWindow):
    """Main window widget."""

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #QMainWindow.__init__(self, *args, **kwargs)
        self.widget_main = MainWidget(parent=self)
        self.setCentralWidget(self.widget_main)
        self.setWindowTitle("Calculadora Retorno Inversion LED")
        self.setWindowIcon(QIcon('img/bulb.jpg'))

def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
