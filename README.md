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
     * [ActivationFunctions.py](https://github.com/syamkakarla98/Activation-Functions-From-Scratch/blob/master/ActivationFunctions.py)

     * [graphs_for_AF.py](https://github.com/syamkakarla98/Activation-Functions-From-Scratch/blob/master/graphs_for_AF.py)
    
* **Download the code** : 

      ```
        git clone https://github.com/syamkakarla98/Activation-Functions-From-Scratch.git
      
      ```
      or
      
    
     [click Here to Download Zip File](https://github.com/syamkakarla98/Activation-Functions-From-Scratch/releases)
  
* After downloading the code, the module can be imported using below command:
  ```python
      from ActivationFunctions import ActivationFunctions as af
      
  ```
   The methods of the ActivationFunctions can be used as:
   ```python
      af.identity(11)
      af.ReLu(1)
      af.tanh(1126)
   ```
    
1. The program [**ActivationFunctions.py**](https://github.com/syamkakarla98/Activation-Functions-From-Scratch/blob/master/ActivationFunctions.py) consists of eight different types of activation functions : 


     * [Identity](https://en.wikipedia.org/wiki/Activation_function)
     * [BinaryStep](https://en.wikipedia.org/wiki/Activation_function)
     * [Sigmoid](https://en.wikipedia.org/wiki/Activation_function)
     * [tanh](https://en.wikipedia.org/wiki/Activation_function)
     * [ArcTan](https://en.wikipedia.org/wiki/Radial_basis_function_kernel)
     * [Rectified Linear Unit(ReLU)](https://en.wikipedia.org/wiki/Activation_function)
     * [Leaky Rectified Linear Unit(leakyReLU)](https://en.wikipedia.org/wiki/Activation_function)
     * [Softmax](https://en.wikipedia.org/wiki/Activation_function)
     

   * The above functions are implemented under the class **_ActivationFunctions_**.
   
2. The second program is [**_graphs_for_AF_**](https://github.com/syamkakarla98/Activation-Functions-From-Scratch/blob/master/graphs_for_AF.py) : 

     * This programis used to plot the above eight activation functions using [matplotlib](https://matplotlib.org/tutorials/index.html)
     * By executing this program, it results eight plots forthe repective activation functions.
     * The generated plota are shown below:
     
          *![identity](https://user-images.githubusercontent.com/36328597/41585817-be5d8c90-73c8-11e8-8510-b6a5ceec19bb.png)

          *![binarystep](https://user-images.githubusercontent.com/36328597/41585816-be19b3ee-73c8-11e8-9b3e-1aa10921ac69.png)

          *![sigmoid](https://user-images.githubusercontent.com/36328597/41585822-bf2f5b44-73c8-11e8-9314-6faaa66c0f62.png)

          *![tanh](https://user-images.githubusercontent.com/36328597/41585826-bfc21592-73c8-11e8-9418-58c1b3538431.png)

          *![arctan](https://user-images.githubusercontent.com/36328597/41585814-bdd94188-73c8-11e8-8211-b72883100517.png)

          *![relu](https://user-images.githubusercontent.com/36328597/41585819-bed596e0-73c8-11e8-991c-18ace4aefb33.png)

          *![leakyrelu](https://user-images.githubusercontent.com/36328597/41585818-be98f2a8-73c8-11e8-8fca-65b1603e64b7.png)

          *![softmax](https://user-images.githubusercontent.com/36328597/41585824-bf79995c-73c8-11e8-9cc2-74e457fce802.png)


## License

This project is licensed under the **MIT** License - see the [LICENSE.md](https://github.com/syamkakarla98/Activation-Functions-From-Scratch/blob/master/LICENSE.md)

