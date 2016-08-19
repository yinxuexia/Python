#开始 面向对象 学习
class Vehicle:#定义类
    def __init__(self,speed):
        self.speed=speed

    def drive(self,distance):
        print('need %.2f hours'%(distance/self.speed))


class Bike(Vehicle):#括号内表示定义的类继承了哪个类，即BIke继承了Vehicle
    pass

class Car(Vehicle):
    def __init__(self,speed,fuel):
        Vehicle.__init__(self,speed)
        self.fuel=fuel

    def drive(self,distance):
        Vehicle.drive(self,distance)
        print('need %.3f fuel'%(distance*self.fuel))

b=Bike(15.0)#先传入速度
b.drive(100.0)#再调用方法传入距离
c=Car(45.0,0.012)#传入速度和油耗
c.drive(100.0)

#__init__函数会在类被创建的时候自动调用，用来初始化，它的参数要在创建类的时候提供
#注意init两边的_是两个哦
