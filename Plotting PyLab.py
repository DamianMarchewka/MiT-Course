import matplotlib.pyplot as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 300):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure("lin" "quad")
plt.clf()
plt.subplot(211)
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, "k-", label = "Linear")
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(mySamples, myQuadratic,"o--", label = "Quadratic")
plt.legend(loc = "upper left")
plt.title("Linear vs Quadratic")
plt.xlabel("sample points")
plt.ylabel("linear function")


plt.figure("cube exp")
plt.clf()
plt.plot(mySamples, myCubic,"b-", label = "Cubic")
plt.plot(mySamples, myExponential, "r--", label = "Exponential")
plt.yscale("log")
plt.legend(loc = 'upper left')
plt.title("Cubic vs Exponential")
plt.xlabel("sample points")
plt.ylabel("linear function")

plt.show()
