from RobotArm import RobotArm

robotArm = RobotArm('exercise 6') # levelName of predefined levels

robotArm.speed = 2 # speed can have values: 0,1,2,3,4 or 5



# hieronder jouw code om de arm te laten bewegen

for i in range(7):
	robotArm.moveRight()
for i in range(8):
	robotArm.grab()
	robotArm.moveRight()
	robotArm.drop()
	if i < 7:
		robotArm.moveLeft()
		robotArm.moveLeft()



# hierboven jouw code om de arm te laten bewegen


# expect input from console to continue
input('wait')