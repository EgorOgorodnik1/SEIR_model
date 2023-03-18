import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.linspace(0,40, num=1000)

alpha_1 = 0.2
alpha_2 = 0.8
beta = 1
gamma = 0.45
sigma = 0.15


params = [alpha_1,alpha_2,beta,gamma,sigma]

N = 1
E0 = 0
I0 = 0.01
R0 = 0
S0 = N-E0-I0-R0

y0 = [S0, E0, I0, R0]

def seir(variables, t, params):

    S = variables[0]
    E = variables[1]
    I = variables[2]
    R = variables[3]

    N = S + E + I + R

    alpha_1 = params[0]
    alpha_2 = params[1]
    beta = params[2]
    gamma = params[3]
    sigma = params[4]

    dSdt = -S*((alpha_1 + alpha_2)*I + beta*E)
    dEdt = alpha_1*S*I + beta*E*S - gamma*E
    dIdt = alpha_2*S*I - sigma*I
    dRdt = gamma * E + sigma*I

    return([dSdt, dEdt, dIdt, dRdt])

def dyseir(variables, t, params):

    S = variables[0]
    E = variables[1]
    I = variables[2]


    alpha_1 = params[0]
    alpha_2 = params[1]
    beta = params[2]
    gamma = params[3]
    sigma = params[4]

    dSdt = -S*((alpha_1 + alpha_2)*I + beta*E)
    dEdt = alpha_1*S*I + beta*E*S - gamma*E
    dIdt = alpha_2*S*I - sigma*I

    return([dSdt, dEdt, dIdt])


y = odeint(seir, y0, t, args=(params,))

fig1, axes1 = plt.subplots()
fig2, axes2 = plt.subplots()

axes1.plot(t, y[:,0], '-', color='y', label='$\\alpha_1$'f'{sigma}')
axes1.plot(t, y[:,0], '-', color='r', label='S(t)')
axes1.plot(t, y[:,1], '-', color='b', label='E(t)')
axes1.plot(t, y[:,2], '-', color='k', label='I(t)')
axes1.plot(t, y[:,3], '-', color='g', label='R(t)')
axes1.set_xlabel('t')


i0List = np.arange(0.01,0.8,0.1)  # (start,stop,step)
for i0 in i0List:
    e0 = 0         
    s0 = 1 - i0 - e0              
    ySEIR = odeint(dyseir, (s0,e0,i0), t, args=(params,))  # SEIR model
    plt.plot(ySEIR[:,2], ySEIR[:,1])  # (e(t),i(t))
    #print("lamda={}\tdelta={}\mu={}\tsigma={}\ti0={}\te0={}".format(alpha_1,alpha_2,beta,gamma,sigma,i0,e0))

# Output drawing
plt.axis([0, 0.8, 0, 0.15])
#plt.plot([0,1],[1,0],'b-')  #[x1,x2][y1,y2]
plt.text(0.02,0.36,r"$\lambda=0.3, \delta=0.1, \mu=0.1$",color='black')
plt.xlabel('i(t)')
plt.ylabel('e(t)')

line = ['--','-.',]
label = []


sigma =0.05
params = [alpha_1,alpha_2,beta,gamma,sigma]
y = odeint(seir, y0, t, args=(params,))
axes1.plot(t, y[:,0], line[0], color='r', label= r'$\alpha='f'{sigma}')
axes1.plot(t, y[:,1], line[0], color='b', label='E(t)')
axes1.plot(t, y[:,2], line[0], color='k', label='I(t)')
axes1.plot(t, y[:,3], line[0], color='g', label='R(t)')
axes1.set_xlabel('t')

sigma =0.3
params = [alpha_1,alpha_2,beta,gamma,sigma]
y = odeint(seir, y0, t, args=(params,))
axes1.plot(t, y[:,0], line[1], color='r', label= r'$\alpha='f'{sigma}')
axes1.plot(t, y[:,1], line[1], color='b', label='E(t)')
axes1.plot(t, y[:,2], line[1], color='k', label='I(t)')
axes1.plot(t, y[:,3], line[1], color='g', label='R(t)')
axes1.set_xlabel('t')



plt.show()