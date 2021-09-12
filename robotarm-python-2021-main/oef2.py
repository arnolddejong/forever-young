from RobotArm import RobotArm

robotArm = RobotArm('exercise 2') # levelName of predefined levels

robotArm.speed = 1 # speed can have values: 0,1,2,3,4 or 5



# hieronder jouw code om de arm te laten bewegen

robotArm.grab()
for i in range(9):
	robotArm.moveRight()
robotArm.drop()

for i in range(5):
	robotArm.moveLeft()
robotArm.grab()
for i in range(5):
	robotArm.moveRight()
robotArm.drop()

robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()


# hierboven jouw code om de arm te laten bewegen


# expect input from console to continue
input('wait')