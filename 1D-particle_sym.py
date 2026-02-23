import matplotlib.pyplot as plt
def acceleration (x, k, m):
    a = -k*x/m
    return a
    
def step(x, v, a, dt, k, m):
    
    v = v + a*dt
    x = x + v*dt
    a = acceleration(x,k,m)
    
    return x, v, a
    
    
def simulate(x0=1, v0=0, dt=1, steps=10, k=1, m=1):
    x = [x0]
    v = [v0]
    a0 = acceleration(x0,k,m)
    a = [a0]
    
    
    for i in range(steps):
        #print(x, v, a)
               
        xv = step(x0, v0, a0, dt, k, m)
       
        x0, v0 , a0 = xv
        x.append(x0)
        v.append(v0)
        a.append(a0)
        
        

   
    return x, v, a
       
def printf(x, v, a):
    for i in range(len(x)):
        print("xva: ",i)
        print(x.pop(), v.pop(), a.pop())
        

      


x, v, a = simulate()
#printf(x, v, a)
  

# x, v, a aus deiner Simulation
# x = [...], v = [...], a = [...]
dt=0.01
t = [i*dt for i in range(len(x))]  # Zeitschritte

plt.figure(figsize=(10,6))

# Ort x
plt.subplot(3,1,1)
plt.plot(t, x, 'o-', label='x')
plt.ylabel('x')
plt.grid(True)
plt.legend()

# Geschwindigkeit v
plt.subplot(3,1,2)
plt.plot(t, v, 'o-', label='v', color='orange')
plt.ylabel('v')
plt.grid(True)
plt.legend()

# Beschleunigung a
plt.subplot(3,1,3)
plt.plot(t, a, 'o-', label='a', color='green')
plt.xlabel('t')
plt.ylabel('a')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
        
        
    