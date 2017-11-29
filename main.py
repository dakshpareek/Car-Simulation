import pygame


class Obstacles:
	"""
	Obstacles class is used to create obstacles for car.

	"""
	def __init__(self,x,y_o,y,s):
		"""
		This init method is used to get coordinates of obstacles.

		Args:
			x : x coordinate of object
			y : y coordinate of object
			y_o : origional y coordinate
			s : speed of object (increment point at y axis)

		"""
		self.x=x
		self.y=y
		self.s=s
		self.y_orignal=y_o
	def move(self,screen):
		"""
		This method is used to move obejct further at speed given at initial time

		Args:
			screen: window which is used to display objects.
		"""
		if self.y > 675:
			"""
			Checking end point of y-axis.
			If object is at the end of window then we again assign it its origional y coordinate.  
			"""
			self.y=self.y_orignal

		"""
		This is used to draw obstacle object on screen 
		circle method takes 4 arguement 1. screen object 2. color
		3. coordinates 4. Radius 
		"""
		pygame.draw.circle(screen,(255,0,0),(self.x,self.y+self.s), 10)
		#Incrementing y coordinates of obstacles
		self.y += self.s


class CarSimulation:
	def __init__(self):
		"""
		This constructor is used to initialize required members of CarSimulation class.
		"""

		self.run=True
		
		#initializing screen
		
		self.max_x=300
		self.max_y=650
		self.screen=pygame.display.set_mode((self.max_x,self.max_y))
		
		#setting clock
		
		self.clock=pygame.time.Clock()
		
		#initializing car image
		
		self.image = pygame.image.load('image/car.jpg')
		self.image = pygame.transform.scale(self.image, (30, 55))
		self.car_x=95
		self.car_y=590
		self.xim=3
		
		#creating border
		
		self.border1=[self.screen,(255,0,0),(10,10),(10,self.max_y-10)]
		self.border2=[self.screen,(255,0,0),(self.max_x-10,10),(self.max_x-10,self.max_y-10)]
		
		#nitializing obstacles
		
		self.ob_x=45
		self.ob_y=35

		#Creating four obstacles at different location with different speed
		
		self.ob1=Obstacles(45,35,-500,5)
		self.ob2=Obstacles(115,35,-550,10)
		self.ob3=Obstacles(185,35,-804,12)
		self.ob4=Obstacles(255,35,-632,8)

	def show(self):
		
		"""
		This show method is used to draw border at road and different lanes.
		"""
		
		while self.run:
			self.screen.fill((0,0,0))
			for event in pygame.event.get():
				
				#If used quit the program loop will stop
				
				if event.type==pygame.QUIT:
					self.run=False
			
			
			#Creating borders
			
			pygame.draw.line(*self.border1)
			pygame.draw.line(*self.border2)

			#Generating lanes
			
			for i in range(70,251,70):
				pygame.draw.line(self.screen,(255,255,255),(10+i,10),(10+i,self.max_y-10))


			#Moving obstacles at their speed
			
			self.ob1.move(self.screen)
			self.ob2.move(self.screen)
			self.ob3.move(self.screen)
			self.ob4.move(self.screen)


			#Checking distance of every obstacle and coordinates of car and also checking expected time to crash with car
			
			distance=[[self.ob1.x,self.ob1.y],[self.ob2.x,self.ob2.y],[self.ob3.x,self.ob3.y],[self.ob4.x,self.ob4.y]]
			car_cordinates=[self.car_x+20,self.car_y+35]
			timecheck=[(self.car_y-self.ob1.y)*self.ob1.s,(self.car_y-self.ob2.y)*self.ob2.s,(self.car_y-self.ob3.y)*self.ob3.s,(self.car_y-self.ob4.y)*self.ob4.s]
			

			temp_x1=self.car_x

			#Comparing location of car with objects and moving accordingly.
			
			for every_obs in range(0,len(distance)):
				if distance[every_obs][0]==car_cordinates[0]:
					if every_obs==0:
						next=timecheck[every_obs+1]
						own=timecheck[every_obs]
						if next>own:
							self.car_x=distance[every_obs+1][0]-20
					elif every_obs < 3:
						next=timecheck[every_obs+1]
						prev=timecheck[every_obs-1]
						own=timecheck[every_obs]

						if next>prev and next>own:
							self.car_x=distance[every_obs+1][0]-20
						elif prev>next and prev>own:
							self.car_x=distance[every_obs-1][0]-20		
					elif every_obs==3:
						prev=timecheck[every_obs-1]
						own=timecheck[every_obs]
						if prev>own:
							self.car_x=distance[every_obs-1][0]-20
						

			#Check if obstacle crashed with car
			
			for i in distance:
				if i[0]==self.car_x+20 and (self.car_y+35-i[1])<0:
					print "Crashed at:",timecheck

			#Moving car to safer lane.
			
			temp_x2=self.car_x
			
			for i in range(temp_x1,temp_x2+1):
				self.screen.blit(self.image,(i,self.car_y))

			pygame.display.flip()
			self.clock.tick(35)



if __name__ == '__main__':
	c=CarSimulation()
	c.show()
