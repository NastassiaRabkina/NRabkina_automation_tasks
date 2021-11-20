from random import randrange
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import operator

class Car(object):
	"""This class is for describing object cars and it's properties"""
	def __init__(self, id):
		self.name = 'Car' + str(id)
		self.distance = 0
		self.speed = 0

	def generate_speed (self):
		self.speed = randrange(1, 10)
		self.distance += self.speed		
		return self.speed

	def __str__(self):
		return'{} distance={} speed={}'.format(self.name, self.distance, self.speed)


if __name__ == "__main__":
    
	cars = [Car(i) for i in range(1,11)]
	start = time.perf_counter()

	with ThreadPoolExecutor() as executor:
		tic = 1
		while tic <= 20:
			print (tic, "_____")
			# Start the race and create future object to generate_speed function call for each car
			futures = [executor.submit(car.generate_speed) for car in cars]
			_= [f.result() for f in as_completed(futures)]
			#sort the car list and select top 3
			cars.sort(key=operator.attrgetter('distance'), reverse=True)
			for i in range (1, 4):
				print (str(cars[i]))
			time.sleep(1)
			tic += 1
	print(time.perf_counter() - start)



