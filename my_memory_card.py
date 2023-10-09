#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import*

app=QApplication([])
win = QWidget()


class Question_list():
    def __init__(self,q,right,w1,w2,w3):
        self.q=q
        self.right=right
        self.w1=w1
        self.w2=w2
        self.w3=w3
question =[]
question.append(Question_list('Какой Государственный символы России вы знаете?','Флаг,герб,гимн','Путин,медведь,водка','Сила реки,сила тайги, сила руки','Твоя мама (а вот про мать лишнее было...)'))
question.append(Question_list('Какого цвета подкрадули у Ульяшки?','Красные','Филипетовые','Зеленые','СБМ'))
question.append(Question_list('Что сегодня за день?','День сырка','День сурка','День сучка','День ВВП'))

Button = QPushButton('Ответить')
Question = QLabel('Какой Государственный символы России вы знаете?')
RadioGroupBox = QGroupBox('Варианты')
btn1=QRadioButton('Флаг,герб,гимн')
btn2=QRadioButton('Путин,медведь,водка')
btn3=QRadioButton('Сила реки,сила тайги, сила руки')
btn4=QRadioButton('Твоя мама (а вот про мать лишнее было...)')

#Добавляем кнопки в группу
RadioGroup=QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)


#Создаем расположение группы кнопок
layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(btn1)
layout2.addWidget(btn2)

layout3.addWidget(btn3)
layout3.addWidget(btn4)
layout1.addLayout(layout2)
layout1.addLayout(layout3)
RadioGroupBox.setLayout(layout1)
#Создаем расположеие всех видов ответов в окне
line1=QHBoxLayout()
line2=QHBoxLayout()
line3=QHBoxLayout()

line1.addWidget(Question)
line2.addWidget(RadioGroupBox)
line3.addWidget(Button)

#Создаем самую гравню линию лэйнаут

line_card=QVBoxLayout()
line_card.addLayout(line1)
line_card.addLayout(line2)
line_card.addLayout(line3)

#Окно с ответами
AnsGroupBox = QGroupBox('Результат')
Total = QLabel('Прав/не особо прав')
Correct = QLabel('Правильный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(Total)
layout_res.addWidget(Correct)
AnsGroupBox.setLayout(layout_res)

line1_res = QHBoxLayout()
line2_res = QHBoxLayout()
line3_res = QHBoxLayout()

line1_res.addWidget(Question)
line2_res.addWidget(AnsGroupBox)
line2_res.addWidget(RadioGroupBox)
line3_res.addWidget(Button)
RadioGroupBox.hide()

line_card = QVBoxLayout()
line_card.addLayout(line1_res)
line_card.addLayout(line2_res)
line_card.addLayout(line3_res)


win.setLayout(line_card)

#Функции для обработки событий
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    Button.setText('След.вопросик,пупсик')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    Button.setText('ОТВЕЧаЙ!')

    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

'''def test():
    if 'ОТВЕЧаЙ!' == Button.text():
        show_result()
    else:
        show_question()'''

#Button.clicked.connect(test)
answers = [btn1, btn2, btn3, btn4]
def ask(q:Question_list):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    Question.setText(q.q)
    Correct.setText(q.right) 
    show_question() 

def show_correct(res):
    Total.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        win.score += 1
        show_correct('Верно!')
        print('Всего вопросов:', win.total, '\n', 'Правильных ответов:', win.score, '\n', 'Рейтинг:', win.score/win.total*100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Всего вопросов:', win.total, '\n', 'Правильных ответов:', win.score, '\n', 'Рейтинг:', win.score/win.total*100)

def next_question():
    win.total += 1
    num = randint(0,len(question)-1)
    q=question[num]
    ask(q)
def OK():
    if Button.text()=='ОТВЕЧаЙ!':
        check_answer()
    else:
        next_question()
        
win.total = 0
win.score = 0
Button.clicked.connect(OK)
next_question()


win.show()
app.exec_()