#from machine import Pin, I2C
#import time
#from bmp280 import BMP280  
#from machine import Pin, SoftI2C
#import ssd1306

#inicializacion de la pantalla
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
#oled_width = 128
#oled_height = 64
#oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#inicializacion del sensor presion y temperatura
#i2c = I2C(0, scl=Pin(1), sda=Pin(0))  
#bmp = BMP280(i2c)
#bmp.normal_measure()

#inicializacion calidad del aire
#anapin=machine.ADC(28)


#while True:
#    oled.fill(0)
#    temperature = bmp.temperature
#    pressure = bmp.pressure
#    sensor=anapin.read_u16()

#lectura en consola de mediciones
#    print("Temperatura: {:.2f} C".format(temperature))
#    print("Presion: {:.2f} hPa".format(pressure))
#    print("prescencia de gases valor:  ", sensor )

#valores en la oled
#    oled.text('Temperatura:', 0, 0)
#    oled.text("{:.2f} C".format(bmp.temperature), 30, 10)
#    oled.text('Presion:', 0, 20)
#    oled.text("{:.2f} hpa".format(bmp.pressure), 20, 30)
#    oled.text('Calidad del aire:', 0, 40)
#    if sensor>30000:
#        oled.text('Mala', 40, 50)
#    else:
#        oled.text('Buena', 40, 50)
#    oled.show()
#    time.sleep(1) 

