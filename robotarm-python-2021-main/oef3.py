from RobotArm import RobotArm

robotArm = RobotArm('exercise 3') # levelName of predefined levels

robotArm.speed = 2 # speed can have values: 0,1,2,3,4 or 5



# hieronder jouw code om de arm te laten bewegen

for i in range(4):
	robotArm.grab()
	robotArm.moveRight()
	robotArm.drop()
	robotArm.moveLeft()



# hierboven jouw code om de arm te laten bewegen


# expect input from console to continue
input('wait')