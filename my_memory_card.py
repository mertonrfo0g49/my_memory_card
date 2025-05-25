#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel,QMessageBox, QRadioButton, QGroupBox


app = QApplication([])
win = QWidget()
win.setWindowTitle('Memary Card')


vopros = QLabel('создать переключатели с выриантами ответов')
RadioGroupBox = QGroupBox('Варианты')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

AnsGroupBox = QGroupBox('ответ')
ans = QLabel('222222222222222222222222222222')

layout_0 = QVBoxLayout()




layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
lay_ss = QVBoxLayout()
lay_ss.addWidget(ans)

Button = QPushButton('Ответить')

layout_0.addWidget(vopros)
layout_0.addWidget(RadioGroupBox)

AnsGroupBox.setLayout(lay_ss)
layout_0.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_0.addWidget(Button)


RadioGroupBox.setLayout(layout_ans1)




# class Question():

    
def show_rezult():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    Button.setText("Следующий вопрос")
def next_Question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    Button.setText("Ответить")
 



def start_test():   
    if Button.text() == "Ответить" :
        show_rezult()
    else:
        next_Question()














    #если текст на кнопке = ответить тогда фукция схоу резалт
    #если текст на кнопке следующий вопрос тогда функция некст ансвер


Button.clicked.connect(start_test)

win.setLayout(layout_0)
















win.show()
app.exec_()