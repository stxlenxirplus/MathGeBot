import telebot
from telebot import types

TOKEN = 'ur token'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'menu'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	btn1 = types.KeyboardButton("Таблицы📊")
	btn2 = types.KeyboardButton("Формулы и теоремы📕")
	btn3 = types.KeyboardButton("Информация")
	markup.add(btn1, btn2, btn3)
	bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}!".format(message.from_user), reply_markup=markup)
	
@bot.message_handler(content_types=['text'])
def func(message):
	if(message.text == "Информация"):
		bot.send_message(message.chat.id, text="""
			Бот, содержащий таблицы 
			по математическим/тригонометрическим операциям.
			По всем вопросам к
			@ksjsususjsua 
			""")
	elif(message.text == "Таблицы📊"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		btn1 = types.KeyboardButton("Таблица степеней ")
		btn2 = types.KeyboardButton("Таблица квадратов")
		btn3 = types.KeyboardButton("Таблица кубов")
		btn4 = types.KeyboardButton("Таблица натуральных логарифмов")
		btn5 = types.KeyboardButton("Таблица десятичных логарифмов")
		btn6 = types.KeyboardButton("Таблица формул сокращенного умножения")
		back = types.KeyboardButton("Вернуться в главное меню")
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
		bot.send_message(message.chat.id, text="Выберите Таблицу", reply_markup=markup)
	
	elif(message.text == "Таблица степеней"):
		bot.send_photo(message.chat.id, photo=open('Table_stepen.jpg', 'rb'))
		bot.send_message(message.chat.id, """
			Таблица степеней.

m - число, а - степень.
			""")
	
	elif message.text == "Таблица квадратов":
		bot.send_photo(message.chat.id, photo=open('Table_kvadrat.jpg', 'rb'))
		bot.send_message(message.chat.id, """Таблица квадратов""")
	
	elif message.text == "Таблица кубов":
		bot.send_photo(message.chat.id, photo=open('Table_cube.jpg', 'rb'))
		bot.send_message(message.chat.id, """Таблица кубов""")

	elif message.text == "Таблица натуральных логарифмов":
		bot.send_photo(message.chat.id, photo=open('Table_nat_log.jpg', 'rb'))
		bot.send_message(message.chat.id, """Таблица натуральных логарифмов""")
	
	elif message.text == "Таблица десятичных логарифмов":
		bot.send_photo(message.chat.id, photo=open('Table_des_log.jpg', 'rb'))
		bot.send_message(message.chat.id, """Таблица десятичных логарифмов""")


	elif message.text == "Таблица формул сокращенного умножения":
		bot.send_photo(message.chat.id, photo=open('fsu.jpg', 'rb'))
		bot.send_message(message.chat.id, """Таблица формул сокращенного умножения""")

	elif(message.text == "Формулы и теоремы📕"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		abtn1 = types.KeyboardButton("Квадрат")
		abtn2 = types.KeyboardButton("Куб")
		abtn3 = types.KeyboardButton("Ромб")
		abtn4 = types.KeyboardButton("Пирамида")
		abtn5 = types.KeyboardButton("Треугольник")
		abtn6 = types.KeyboardButton("Параллелограмм")
		abtn7 = types.KeyboardButton("Трапеция")
		abtn8 = types.KeyboardButton("Конус")
		abtn9 = types.KeyboardButton("Круг")
		abtn10 = types.KeyboardButton("Сфера")
		abtn11 = types.KeyboardButton("Прямоугольник")
		abtn12 = types.KeyboardButton("Параллелепипед")
		abtn13 = types.KeyboardButton("Основные тригонометрические тождества")
		exit = types.KeyboardButton("Вернуться в главное меню")
		markup.add(abtn1, abtn2, abtn3, abtn4, abtn5, abtn6, abtn7, abtn8, abtn9, abtn10, abtn11, abtn12,abtn13, exit)
		bot.send_message(message.chat.id, text="Выберите фигуру:", reply_markup=markup)
	
	elif message.text == "Квадрат":
		bot.send_message(message.chat.id, """
			Квадрат - правильный четырёхугольник у 
которого все углы и всё стороны равны. 
Квадрат является частным случаем 
ромба и прямоугольника.

S = a^2
Р = 4а.
a - сторона квадрата

			""")
	elif message.text == "Куб":
		bot.send_message(message.chat.id, """
			Куб - правильный многогранник, каждая 
грань которого представляет собой квадрат. 
Частный случай параллелипипеда и призмы.

S = 6а^2
Р = 12*а
а - ребро.

			""")
	elif message.text == "Ромб":
		bot.send_message(message.chat.id, """
			Ромб - параллелограмм, у которого все стороны равны.

S = 1/2*d1*d2
S = ah
P = 4a
d1 и d2 - диагонали ромба
h - высота ромба
a - сторона ромба.

			""")	
	elif message.text == "Пирамида":
		bot.send_message(message.chat.id, """
		Пирамида - многогранник у которого одна грань- 
произвольный многоугольник, называемое основанием, 
а остальные грани треугольники имеющие общую вершину..

S = площади всех треугольников и основания
S(треугольника) = (а*h)/2
S = основания вычисляется в зависимости от его формы, универсальной формулы нет.
			""")
	elif message.text == "Треугольник":
		bot.send_message(message.chat.id, """
		Треугольник - геометрическая фигура, образованная 
тремя отрезками, которые соединяют три точки, не 
лежащие на одной прямой. Указанные три точки называются 
вершинами треугольника, а отрезки сторонами треугольника.

S = 1/2a*h
S = √(p*(p-a)*(p-b)*(p-c))
S = 1/2a*b*sinc
S = (a*b*c)/R
S = p*r
a - сторона треугольника
h - высота (в данном случае непосредственно падающая на сторону a)
p - полупериметр
sinc - синус угла между сторонами a и b
R - радиус описанной окружности
r - радиус вписанной окружности
	""")
	elif message.text == "Параллелограмм":
		bot.send_message(message.chat.id, """
			Параллелограмм - четырехугольник, у которого стороны 
попарно параллельны. Признаки параллелограмма: 
Если противоположные стороны четырехугольника попарно 
параллельны, то этот четырехугольник называется параллелограммом .

S = a*h
P = 2*(a+b)
h - высота непосредственно падающая на сторону a.
			""")

	elif message.text == "Трапеция":
		bot.send_message(message.chat.id, """
			Трапеция - выпуклый четырехугольник, у которого 
две стороны параллельны, а две другие нет. Две параллельные 
стороны трапеции называются её основаниями, 
а две другие- боковыми сторонами.

S = (a+b)/2*h
S = (a+b)/2*√(c^2-(((a-b)^2+c^2-d^2)/2*(a-b))^2)
Р = a+b+c+d
a - верхнее основание
b - нижнее основание
c и d - боковые стороны
h - высота непосредственно подающая с верхнего основания на нижнее.

			""")
	elif message.text == "Конус":
		bot.send_message(message.chat.id, """
			Конус - тело в евклидовом пространстве полученное 
объединением всех лучей исходящих, из одной точки 
и проходящих через плоскую поверхность.

S = πr^2+πRl
l- образующая конуса.

			""")
	elif message.text == "Круг":
		bot.send_message(message.chat.id, """
			Круг - часть плоскости, лежащая внутри окружности. 
Другими словами, это геометрическое место точек плоскости, 
расстояние от которых до заданной точке, называемой центром 
круга, не превышает заданного неотрицательного числа называется 
радиусом данного круга.

S = πr^2
P = 2πr
r - радиус круга
π - 3,1415926535897....

			""")
	elif message.text == "Сфера":
		bot.send_message(message.chat.id, """
			Сфера - геометрическое место точек в пространстве, 
равно удаленные от некоторой заданной точки. 
Расстояние от центра сферы до её любой 
точки называется её радиусом. 
Сфера радиуса 1 называется единичной сферой.

S = 4πR^2

			""")
	elif message.text == "Прямоугольник":
		bot.send_message(message.chat.id, """
			Прямоугольник - четырехугольник, 
у которого все углы прямые(90градусов).

S= a*b
P = 2(a+b)
a и b - стороны прямоугольника.

			""")
	elif message.text == "Параллелепипед":
		bot.send_message(message.chat.id, """
			Параллелипипед - призма, основанием которой служит параллелограмм, 
или многогранник, у которого шесть граней и каждая 
является параллелограммом.

S = 2(ab+bc+ac)
Р = 4(а+b+c)
a,b и с - рёбра параллелепипеда.
""")

	elif message.text == "Основные тригонометрические тождества":
		bot.send_message(message.chat.id, """
			Основные тригонометрические тождества
			https://telegra.ph/Osnovnye-trigonometricheskie-tozhdestva-05-06

			""")
                

	elif (message.text == "Вернуться в главное меню"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
		button1 = types.KeyboardButton("Таблицы📊")
		button2 = types.KeyboardButton("Формулы и теоремы📕")
		button3 = types.KeyboardButton("Информация")
		markup.add(button1, button2, button3)
		bot.send_message(message.chat.id, text="С возвращением!", reply_markup=markup)
	else:
		bot.send_message(message.chat.id, text="Неизвестная команда! Для вызова меню введите команду /menu")

if __name__ == '__main__':
        bot.polling(none_stop=True, interval=0)
