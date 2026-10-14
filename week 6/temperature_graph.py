import matplotlib.pyplot as plt

days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
temperature=[23,27,17,20,12,15,29]

x=days
y=temperature
plt.figure(figsize=(8, 6))
plt.plot(x,y,color='red',marker='o')
plt.title("Line plot: Temperature Of This Week")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()
plt.pie(y,labels=x)
plt.show()