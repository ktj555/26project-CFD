# Project AI

### Object
* __Compute velocity profile__ by using Encoding Decoding Convolution Neural Network added TBNN
  * Very fast calculation speed compared other CFD simulation
  * Great accuracy  
is satisfied(hope)
* __Automation process__ by using python win32com library during all analysis process

<details>
  <summary>What is CFD?</summary>
  <div markdown="1">
    
    CFD is Computational Fulid Dynamics  
      
    In fuild dynamics,  
    general equations, called Navier-Stokes equations, can't be solved analytically.  
      
    So, we can have numerical solution only.  
    CFD solve ns-eqn to numerical analysis.
    One way operating CFD is FEM(Finite Element Method).  
    
    if you want more information about that,  
    <a href="https://en.wikipedia.org/wiki/Computational_fluid_dynamics">Visit</a>
    
  </div>
</details>

### Implementations
* Automation to slice 3d modeling file and save shape infomation to csv file
* Create AI model by using tensorflow

### Additional
* Language : Python(AI Model), C++(win32api for automation), matlab(for create training data sets)
* Enviroment : VScode & jupyter notebook & matlab & Visual studio or others
* Develop period : 8 weeks

### Should learn
* library : win32com(for handling inventor and comsol), openCV(if it is needed)

### PLAN
|index|note|
|--|--|
|1~4|Study win32com library and handling inventor and comsol by python|
|5~6|Create training data set using comsol(CFD-simulator)|
|7|Create AI model and training|
|8|Test algorithm|
