import numpy as np

def dxdt(N, F):
    def deq(x):
        d = np.zeros(N)
        d[0] = (x[1] - x[N-2]) * x[N-1] - x[0]
        d[1] = (x[2] - x[N-1]) * x[0]- x[1]
        d[N-1] = (x[0] - x[N-3]) * x[N-2] - x[N-1]
        
        for i in range(2, N-1):
            d[i] = (x[i+1] - x[i-2]) * x[i-1] - x[i]

        d = d + F
        return d
    
    return deq

def step_solver(f):
    # 4th order runge kutta for autonomous dynamics
    # step is a function with arguments (x, dt)
    # If the system state is x at time t step(x, dt) gives the
    # state at time t + dt. 
    # Since the system is autonomous, t doesn't matter, only x and dt do.
    def step(x, dt):
        k1 = dt * f(x)
        k2 = dt * f(x+k1/2)
        k3 = dt * f(x+k2/2)
        k4 = dt * f(x+k3)
        return x + (k1 + 2*(k2 + k3) + k4)/6
    return step


def integration_between_obs(step, dkobs, dt):
    def M(i, x):
        for j in np.arange(dkobs):
            x = step(x, dt)
        return x
    return M