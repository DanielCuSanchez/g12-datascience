import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([40, 20, 60, 87, 65, 89, 90, 40, 11])
y_points = np.array([10, 20, 30, 40, 50, 60, 70, 80, 100])

# markers: +, o, D, P, 1, 2, 3, 4, *
# plt.plot(x_points, y_points, marker = 'o', linestyle = 'dotted')
# plt.grid(color="purple")


fontPersonalized = {'family': "Arial", "color": "blue", "size": 30}

plt.title("Student's grades", fontdict = fontPersonalized, loc="center")
#plt.xlabel("Quantity of students")
#plt.ylabel("Average")

#plt.show()


# POINTS

arrA = np.arange(10)
arrB = np.arange(10)

plt.scatter(arrA, arrB)
# plt.show()

# BARS
apple = ["Apple", "Samsung"]
samsung = [100, 90]
plt.title("Sells", fontdict = fontPersonalized, loc="center")
#plt.xlabel("Companies")
#plt.ylabel("Millions USD")

# plt.bar(apple, samsung,  color=["green", "blue"])
#plt.show()


# PIE CHART
companies = [80, 20]
labelsC = ["Apple", "Samsung"]

myConfig = [0.3, 0] #Separation
plt.pie(companies, labels = labelsC, explode=myConfig)
plt.legend()
plt.show()