# Demystifying-QBs--Accuracy
"Final Project",UNAM -TICs-Simulation and Modeling 2024-1 class,taught by Dr. Victor de la Luz 

# Team_Members :family:
* Valeria Garcés Mendoza ([valeria-gm](https://github.com/valeria-gm))
* Gerardo Zabdiel Martinez Zavala([ZabdielZ](https://github.com/ZabdielZ))
* Miguel Ángel Zamorano Presa. ([miguelzpresa](https://github.com/miguelzpresa))

____
# License :space_invader:
Copyright © 2023 <,gmvaleriaaa@gmail.com,mikezpresa@gmail.com,gm546161@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



[![imm](https://github.com/miguelzpresa/Demystifying-QBs--Accuracy/assets/49998408/e2a92709-018b-4a83-ad9e-c183ed94f318)](https://www.youtube.com/watch?v=U7rPIg7ZNQ8)
[![Watch the video](![imm](https://github.com/miguelzpresa/Demystifying-QBs--Accuracy/assets/49998408/e2a92709-018b-4a83-ad9e-c183ed94f318))](https://www.youtube.com/watch?v=U7rPIg7ZNQ8)



![alt text](https://github.com/miguelzpresa/Demystifying-QBs--Accuracy/blob/main/output14/prueba14.gif)

____
# Introduction :microscope:


The goal of this project is to model the trajectory of an American football ball to determine the force and angle necessary to complete a pass given the coordinates of the quarterback, the direction and speed of the receiver making an estimation of the receiver-ball intersection.

The American football is a project that is affected by gravity and air resistance. Gravity causes the ball to fall toward the ground, while air resistance causes the ball to lose speed.

To model the trajectory of the ball, the equation of motion for projectiles will be used. This equation describes the position of the ball as a function of time.

The force and angle of the launch will be determined through an iterative process. Different force and angle values ​​will be tried until a throw that matches the catcher's coordinates is found.

This project has the potential to improve passing accuracy in American football. By determining the optimal force and angle for a pass, players can increase their chances of completing the pass.

Additionally, this project could be used to develop new training systems for American football players. These systems could help players develop the precision and skill needed to complete difficult steps.

Below are some of the challenges expected to be faced in this project:

    Air resistance is a complex factor that is difficult to model accurately.
    The direction and speed of the catcher may vary during the throw.
    The ball can bounce on the field, which complicates the calculation of the trajectory.

Despite these challenges, this project has the potential to be a valuable tool for American football players and coaches.


![imm](https://github.com/miguelzpresa/Demystifying-QBs--Accuracy/assets/49998408/6b18bf59-9006-445e-b4e9-b31e31ca5d66)




# Justification :telescope:
---
Potential impact

This project has the potential to have a positive impact on American football. The mathematical model and computer program could help coaches and players improve passing accuracy. This could lead to an increase in the number of passes completed, which could lead to an increase in the number of touchdowns and points scored.




---
 



# Arquitecture 







---




---
# Objectives_of_each_Phase :pushpin:
---
##### Phase 1: Develop a mathematical model for the trajectory of the ball
+
+
##### Phase 2: Implement the model in a computer program.
+
+
##### Phase 3: Use the program to calculate the force and angle needed to throw the ball so that the receiver can catc
+
+

##### Phase 4: Integration and Testing
Integrate all the previous phases into a functional and efficient system.
Conduct exhaustive testing to ensure that the system works correctly in all situations.

# Metodology :satellite:
---



The mathematical model for the trajectory of an American football will be based on the laws of physics. The model will take into account the following factors:

    The force and direction of the throw.
    Air resistance.
    The gravity.

![WhatsApp Image 2023-12-01 at 21 36 18](https://github.com/miguelzpresa/Demystifying-QBs--Accuracy/assets/49998408/0c9fcb28-eff0-4495-a67c-f4ac356f34d2)



![imm2](https://github.com/miguelzpresa/Demystifying-QBs--Accuracy/assets/49998408/f95e6c8e-f623-4308-841b-00b04687091a)


The computer program will be implemented in Python. The program will read the coordinates of the quarterback and receiver as input. The program will use the mathematical model to calculate the force and angle needed to throw the ball.

Expected results

The project is expected to achieve the following results:

    A precise mathematical model for the trajectory of an American football ball.
    A computer program that can calculate the force and angle needed to throw the ball so that the receiver can catch it.
---

# Libraries :pencil2:
---
* [Python 3](https://www.python.org/)
* Linux Ubuntu    64-bit
* [Github](https://www.github.com)
* Jupyter lab     3.2.9
* git


# Packages :triangular_flag_on_post:  
---
* [Pandas version 1.4.1](https://pandas.pydata.org/)
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy version 1.21.5](https://numpy.org/) 




---
# Executing_Software_Intructions :surfer:
---
1. clone the deployment repo
2. get libraries versions specified in requirements.txt
3. execute run.py
Instructions to create the gift
1. run rocket.py and create a .dat file with the data
2. Create a folder where the images will be saved
3.run the visual.py code changing the name of the data file and the folder where the images will be saved
4.Create the gift with the images
-Position yourself in the folder
-run the following command on the terminal:
convert -delay 0 -quality 20 -size 200 -loop 5 *.png prueba8.gif
---  

# Conclusions :space_invader:

This project represents a significant stride towards enhancing passing accuracy in American football. By employing the projectile motion equation and an iterative process to determine the optimal force and angle for a pass, this initiative addresses the complex dynamics influenced by gravity, air resistance, and the varying conditions of the playing field. The potential impact of this project extends beyond the field, as it opens avenues for the development of innovative training systems. These systems could revolutionize how football players hone their skills, fostering precision and expertise in executing challenging passes.

Our efforts have successfully resulted in the accurate modeling of the trajectory for actual plays. Through rigorous testing and iterative processes, we have achieved a level of precision in determining the force and angle required for a successful pass. This success not only validates the viability of our approach but also underscores the potential practical applications of our model in real-world game scenarios.

Furthermore, we took our commitment to excellence a step further by exploring and modeling trajectories that we believe represent improved plays. This forward-looking aspect of our project opens up exciting possibilities for strategic decision-making on the field and could contribute to the evolution of play-calling strategies in American football.

In essence, our project has not only addressed the initial objectives of accurately modeling actual play trajectories but has also ventured into the realm of strategic optimization. This dual accomplishment positions our work as a valuable resource for both players and coaches, offering insights into both current performance dynamics and potential avenues for enhancing gameplay. As we continue to refine and expand our models, the impact on American football training and strategy development is poised to be even more profound.


---
# References :peach:
---


