#
# import matplotlib.pyplot as plt
#
# import numpy as np
#
#
# y0=[6, 12, 18, 12, 13, 8, 13, 11, 10, 16, 13, 11, 10, 10, 2, 14]
# x0=[8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 12, 13, 13]
# data = [x0, y0]
# fig = plt.figure(1,figsize=(9,6))
# ax = fig.add_subplot(111)
#
#
# # Create the boxplot
# bp = ax.boxplot(data)
# for whisker in bp['whiskers']:
#     whisker.set(color='#7570b3', linewidth=2)
#
# for median in bp['medians']:
#     median.set(color='#b2df8a', linewidth=2)
#
# for fliers in bp['fliers']:
#     fliers.set(color='red', markersize=4)
#
#
# plt.grid()
# plt.show()


#class Shape():
#    def __init__(self, bidth, height):
#        self.bidth = bidth
#        self.height = height
#
#class Triangle(Shape):
#	def area(self):
#		return (self.bidth * self.height) * 0.5
#
#class Rectangle(Shape):
#	def area(self):
#		return (self.bidth * self.height)
#
#
#triangle = Triangle(2, 3)
#rectangle = Rectangle(4, 5)
#
#print(triangle.area())
#print(rectangle.area())


count = 3
count1 = 5

for i in range(1, 101):
	if i == count:
		print("MThree")
		count += 3
	elif i == count1:
		print("MFive")
		count1 += 5
	else:
		print(i)



















