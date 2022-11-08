"""
This is a file containing the following classes: amazonEmployee, kivaRobot, leadBattery, chargeStation, 
processor, wheels, and infraredSensor.
"""
class amazonEmployee:
    def __init__(self) -> None:
      print("AmazonEmployee Constructor")

    def turnOn(self):
        print("Turn on Kiva Robot")

    def turnOff(self):
        print("Turn off Kiva Robot")

class kivaRobot:
  def __init__(self,color) -> None:
     self._color = color
     print("KivaRobot Constructor")  

  def detectBatteryLevel(self):
    print("Detect Battery Level")

class chargeStation:
  def __init__(self) -> None:
     print("chargeStation Constructor")

  def performCharge(self):
    print("Charge Lead Battery")

class leadBattery:
  def __init__(self, brand) -> None:
     self._brand = brand
     print("LeadBattery Constructor")

  def recharge(self):
    print("Recharge the battery")

  def deplete(self):
    print("Depleted battery level detected")

class processor:
  def __init__(self) -> None:
     print("Processor Constructor")

  def sendCommands(self):
    print("Send commands to camera and infrared sensor")

class wheels:
  def __init__(self) -> None:
     print("Wheels Constructor")

  def turn(self):
    print("Turn Kiva Robot")
  
  def stop(self):
    print("Stop Movement of Kiva Robot")

  def start(self):
    print("Start movement of Kiva Robot")

class infraredSensor:
  def __init__(self) -> None:
    print("infraredSensor constructor")

  def detectFloorSensor(self):
    print("Detect floor sensors")

  def detectObstable(self):
    print("prevent collision")