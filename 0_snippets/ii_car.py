# -*- coding: UTF-8 -*-
class Car:
  """一次模拟汽车的简单尝试"""

  def __init__(self, make, model, year):
    """初始化"""
    self.make = make  # class Car的属性
    self.model = model
    self.year = year
    self.odometer_reading = 0 # 设置默认值

# car(class) 的方法
  def get_descriptive_name(self): # self 掉膘可以使car的属性
    """返回整洁的描述性信息"""
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    """打印一条指出汽车里程的信息"""
    print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    
    """输入数据检测"""
    if mileage > self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can not roll back a odometer!")

  def increment_odometer(self, mileage):
    """增量"""
    self.odometer_reading += mileage

class Battery:
  def __init__(self, battery_size = 75):
      self.battery_size = battery_size

  def describe_battery(self):
    print(f"This car has a {self.battery_size}-KWH battery.")

  def get_range(self):
    if self.battery_size == 75:
      range = 260
    elif self.battery_size == 100:
      range = 315
    print(f"This car can go about {range} miles on a full charge.")  

class ElectricCar(Car): #明确继承关系
  """电动车，继承car"""
  def __init__(self, make, model, year):
    """继承"""
    super().__init__(make, model, year)  # 继承父类的init
    """个性化"""
    self.battery = Battery() # 将实例，作为类的属性

