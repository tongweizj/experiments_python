# -*- coding: UTF-8 -*-
class Dog:
    """一次模拟小狗的简单尝试"""
    """Dog 首字母大写，没有 ()"""

    def __init__(self, name, age):
        """初始化属性 name 和 age """
        self.name = name
        self.age = age

    def sit(self):
        """小狗 蹲下"""
        print(f'{self.name} is now sitting')
        
    def roll_over(self):
        print(f'{self.name} rolled over!')

"""创建实例"""
my_dog = Dog('Summer', 2)

"""访问属性"""
print(f"My dog's name is  {my_dog.name}")
print(f"\nMy dog is {my_dog.age} years old.")

"""调用方法"""
my_dog.sit()
my_dog.roll_over()

"""创建多个实例"""
your_dog = Dog("Lucy", 9)
your_dog.sit()