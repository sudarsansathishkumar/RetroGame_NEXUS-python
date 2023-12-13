
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Flames")
		self.setGeometry(100, 100, 320, 400)
		self.UiComponents()
		self.show()

	def UiComponents(self):
		name1_label = QLabel("Enter Name 1 : ", self)
		name1_label.setStyleSheet("border : 1px solid black ;background : lightgrey;")
		name1_label.setGeometry(10, 20, 140, 40)
		name2_label = QLabel("Enter Name 2 : ", self)
		name2_label.setStyleSheet("border : 1px solid black ;background : lightgrey;")
		name2_label.setGeometry(10, 70, 140, 40)
		self.name1 = QLineEdit(self)
		self.name1.setGeometry(160, 20, 150, 40)
		self.name2 = QLineEdit(self)
		self.name2.setGeometry(160, 70, 150, 40)
		self.output = QLabel("Relationship Status", self)
		self.output.setGeometry(20, 160, 280, 60)
		self.output.setStyleSheet("border : 2px solid black;background : white;")
		self.output.setAlignment(Qt.AlignCenter)
		self.output.setFont(QFont('Times', 11))
		self.push = QPushButton("Get Result", self)
		self.push.setGeometry(80, 260, 140, 50)
		self.push.clicked.connect(self.do_action)

	def do_action(self):
		name1 = self.name1.text()
		name2 = self.name2.text()	
		name1.replace(" ", "")
		name2.replace(" ", "")

		def remove_match_char(list1, list2):

			for i in range(len(list1)):
				for j in range(len(list2)):

					
					if list1[i] == list2[j]:
						c = list1[i]

						
						list1.remove(c)
						list2.remove(c)

						
						list3 = list1 + ["*"] + list2

						
						return [list3, True]

						
			
			list3 = list1 + ["*"] + list2
			return [list3, False]

		
		def find_relation(p1_list, p2_list):
			
			
			proceed = True

			
			while proceed:
				
				ret_list = remove_match_char(p1_list, p2_list)

				
				con_list = ret_list[0]

				
				proceed = ret_list[1]

				
				star_index = con_list.index("*")

				
				p1_list = con_list[: star_index]

				
				p2_list = con_list[star_index + 1:]

				
			count = len(p1_list) + len(p2_list)

			
			result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

			
			while len(result) > 1:

				
				split_index = (count % len(result) - 1)

				
				if split_index >= 0:

					
					right = result[split_index + 1:]
					left = result[: split_index]

					
					result = right + left

				else:
					result = result[: len(result) - 1]

			
			return result[0]

		
		result = find_relation(list(name1), list(name2))

		
		self.output.setText("Relationship : " + result)



App = QApplication(sys.argv)


window = Window()


sys.exit(App.exec())
