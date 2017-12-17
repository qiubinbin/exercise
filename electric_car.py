"""电动汽车"""
from car import Car
class ElectricCar(Car):
	def __init__(self,make,model,year):
		'''初始化父类'''
		super().__init__(make,model,year)
		self.battery=Battery()
	def fill_gas_tank(self):
		"""电动汽车没有油箱"""
		print("This car doesn't need a gas tank!")
class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	def __init__(self, battery_size=70):
		"""初始化电瓶的属性"""
		self.battery_size = battery_size
	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)