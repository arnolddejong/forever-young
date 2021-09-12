from RobotArm import RobotArm

robotArm = RobotArm('exercise 4') # levelName of predefined levels

robotArm.speed = 2 # speed can have values: 0,1,2,3,4 or 5



# hieronder jouw code om de arm te laten bewegen

for i in range(2):
	robotArm.grab()
	robotArm.moveRight()
	robotArm.moveRight()
	robotArm.drop()
	robotArm.moveLeft()
	robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for i in range(2):
	robotArm.moveRight()
	robotArm.grab()
	robotArm.moveLeft()
	robotArm.drop()




# hierboven jouw code om de arm te laten bewegen


# expect input from console to continue
input('wait')