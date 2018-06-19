# [Activation Functions](https://en.wikipedia.org/wiki/Activation_function) from scratch using python 

   
### Prerequisites

The things that you must have a decent knowledge on: 
```
    * Python
    * Activation Functions
```

### Installation

* This project is fully based on python. So, the necessary modules needed for computaion are:
```
    * Numpy 
    * Matplotlib
    
```
* The commands needed for installing the above modules on windows platfom are:
```python

    pip install numpy
    pip install matplotlib
```
* we can verify the installation of modules by  importing the modules. For example:
```python

    import numpy
    import matplotlib.pyplot as plt
    
```
### Explanation 

* There are two programs written for implementing activation funcions.They are:
     * [ActivationFunctions.py](https://stats.stackexchange.com/questions/101344/is-kernel-pca-with-linear-kernel-equivalent-to-standard-pca)
     * [graphs_for_AF.py](https://en.wikipedia.org/wiki/Radial_basis_function_kernel)
    
* **Download the code** : 

      ```
        git clone
      
      ```
      or
      
    
     [click Here to Download]()
  
* After downloading the code, the module can be imported using below command:
  ```
      from ActivationFunctions import ActivationFunctions as af
      
  ```
   The methods of the ActivationFunctions can be used as:
   ```
      af.identity(11)
      af.ReLu(1)
      af.tanh(1126)
   ```
    
1. The program [**ActivationFunctions.py**]() consists of eight different types of activation functions : 


     * [Identity](https://en.wikipedia.org/wiki/Activation_function)
     * [BinaryStep](https://en.wikipedia.org/wiki/Activation_function)
     * [Sigmoid](https://en.wikipedia.org/wiki/Activation_function)
     * [tanh](https://en.wikipedia.org/wiki/Activation_function)
     * [ArcTan](https://en.wikipedia.org/wiki/Radial_basis_function_kernel)
     * [Rectified Linear Unit(ReLU)]https://en.wikipedia.org/wiki/Activation_function)
     * [Leaky Rectified Linear Unit(leakyReLU)](https://en.wikipedia.org/wiki/Activation_function)
     * [Softmax](https://en.wikipedia.org/wiki/Activation_function)
     

   * The above functions are implemented under the class **_ActivationFunctions_**.
   
2. The second program is [**_graphs_for_AF_**]() : 
     * This programis used to plot the above eight activation functions using [matplotlib](https://matplotlib.org/tutorials/index.html)
     * By executing this program, it results eight plots forthe repective activation functions.
     * The generated plota are shown below:
          *
          *
          *
          *
      
   

### Conclusion 

   * By performing **KPCA** with three different kernels (linear,rbf,polynomial) on the iris data set.
   * since, the initial two Principal Components(PC'S) has more variance ratio. we selected two only.
   * Initially the dataset contains the dimensions **150 X 5** is drastically reduced to **150 X 3** dimensions including label.
   * The classification has varied a lot according to the kernel choosen.
   

## License

This project is licensed under the **MIT** License - see the [LICENSE.md](https://github.com/syamkakarla98/Kernel-PCA-Using-Different-Kernels-With-Classification/blob/master/LICENSE.md)

