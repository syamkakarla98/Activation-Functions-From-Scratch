import numpy as np
import matplotlib.pyplot as plt
from ActivationFunctions import ActivationFunctions as af


def plotActivationFunctions():
    actfn=['identity','binaryStep','sigmoid','tanh',
        'arcTan','ReLU','leakyReLU','softmax']
    dic={0:'plt.plot(x, af.identity(x))',1:'plt.plot(x, af.binaryStep(x))'
         ,2:'plt.plot(x, af.sigmoid(x))',3:'plt.plot(x, af.tanh(x))'
         ,4:'plt.plot(x, af.arcTan(x))',5:'plt.plot(x, af.ReLU(x))'
         ,6:'plt.plot(x, af.leakyReLU(x))',7:'plt.plot(x, af.softmax(x))'
         }
    for i in range(8):
        x = np.linspace(-10, 10)
        exec(dic[i])
        plt.axis('tight')
        plt.title('Activation Function :'+actfn[i]+' ')
        plt.show()



plotActivationFunctions()
