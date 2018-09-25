from IPython.display import HTML, display

def show_answer(excercise_tag):
    
    s = answers[excercise_tag]
    s = '<code>'+s+'</code>'
    s = ''.join(['<div >', str(s), '</div>'])
    display(HTML(s))
    
answers = {}

answers['OI'] = r'''
Python3:

BHt = B @ H.T
K = BHt @ np.linalg.inv(H @ BHt + R)
xa[:, t] = xf[:, t] + K @ (y[:, t] - H @ xf[:, t])

Python2:

BHt = B.dot(H.T)
K = BHt.dot(np.linalg.inv(H.dot(BHt) + R))
xa[:, t] = xf[:, t] + K.dot(y[:, t] - H.dot(xf[:, t]))
'''

answers['3DVar J'] = r'''
Python3:

difB = x - xf
difR = y - H.dot(x) 

costB = difB @ Binv @ difB.T
costR = difR @ Rinv @ difR.T

cost = costB + costR

Python2:

difB = x - xf
difR = y - H.dot(x) 

costB = difB.dot(Binv).dot(difB.T)
costR = difR.dot(Rinv).dot(difR.T)

cost = costB + costR
'''

answers['3DVar gradJ'] = r'''
Python3:

difB = x - xf
difR = y - H.dot(x) 

gradB = 2 * Binv @ difB
gradR = 2 * H.T @ Rinv @ difR

grad = gradB - gradR

Python2:

difB = x - xf
difR = y - H.dot(x) 

gradB = 2 * Binv.dot(difB)
gradR = 2 * H.T.dot(Rinv.dot(difR)) 

grad = gradB - gradR
'''


answers['EnKF'] = r'''
Python3:

_, Np = xf.shape

S = np.cov(xf) * infl

SHT = S @ H.T
K = SHT @ np.linalg.pinv(H @ SHT + R)

perturbations = scipy.stats.multivariate_normal(np.zeros(N), R).rvs(Np).T
D = np.vstack(y) + perturbations
innov = D - H @ xf

xa = xf + K @ innov

Python2:

_, Np = xf.shape

S = np.cov(xf) * infl

SHT = S.dot(H.T)
K = SHT.dot(np.linalg.pinv(H.dot(SHT) + R))

perturbations = scipy.stats.multivariate_normal(np.zeros(N), R).rvs(Np).T
D = np.vstack(y) + perturbations
innov = D - H.dot(xf)

xa = xf + K.dot(innov)
'''