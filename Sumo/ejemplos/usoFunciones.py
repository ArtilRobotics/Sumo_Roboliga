#RobotName: EjemploFunc
#NO SE PUEDEN USAR TILDES EN LOS COMENTARIOS

from RobotRL import RobotRL

robot = RobotRL()

def salvarmeDeCaer():
   color=robot.getColorPiso() # robot.getColorPiso() devuelve un valor entre 0 (oscuro) y 100 (claro)
   if(robot.getColorPiso()>90): 
       robot.setVel(-30, -30) #Retrocedo
       robot.esperar(0.5) #durante medio segundo
       robot.setVI(30) #pongo la rueda izquierda a andar hacia adelante asi giro
       robot.esperar(0.5) #durante medio segundo tambien
    

while robot.step():
   robot.setVel(50, 50) # Defino la velocidad para ir hacia adelante
   salvarmeDeCaer() #No es un mensaje a robot, porque es una funcion que cree en este modulo.
   

    
