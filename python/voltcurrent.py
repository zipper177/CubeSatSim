"""Sample code and test for adafruit_in219"""
# Reads all voltage and current sensors for two I2C buses

import sys
#import board
import busio
from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_ina219 import INA219

if __name__ == "__main__":
#	    print 'Length: ', len(sys.argv)
  
  buses = [1, 3] # default I2C buses
  config = False
  
  if (len(sys.argv)) > 1:
#   print("There are arguments!")
#   if (('a' == sys.argv[1]) or ('afsk' in sys.argv[1])):
    buses[0] = int(sys.argv[1], base=10)
    if (len(sys.argv)) > 2:
      buses[1] = int(sys.argv[2], base=10)
      if (len(sys.argv)) > 3:
        if sys.argv[3] == "c":
          config = True
          from adafruit_ina219 import ADCResolution, BusVoltageRange

  addresses = [40, 41, 44, 45] #INA219 addresses on the bus
  print("buses: ", buses, " addr: ", addresses)
  for x in buses:
    for y in addresses:
      print(x,y)
#      try:
      if True:
  # Create library object using  Extended Bus I2C port
        print("bus: ", buses[x], " addr: ", addresses[y])
        i2c_bus = I2C(buses[x]) # 1 Device is /dev/i2c-1
        ina219 = INA219(i2c_bus, addresses[y])
   
#   print("ina219 test")
        if config:
          print("Configuring")
# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
          ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_1S   # 32S
          ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_1S     # 32S
# optional : change voltage range to 16V
          ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

        bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
#       shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
        current = ina219.current  # current in mA
# INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
#       print("{:6.3f}".format(bus_voltage + shunt_voltage))
        print(bus_voltage, " ", current, " ")
#      except:
#        print("0.0 Error")
    
