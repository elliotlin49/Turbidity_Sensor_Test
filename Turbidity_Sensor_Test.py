import smbus
import time

address = 0x48
A0 = 0x40

bus = smbus.SMBus(1)
while True:
    volt = 0
    #bus.write_byte(address, A0)
    value = bus.read_byte(address)
    print(value)
    '''for i in range(800):
        volt += float(value/1023) * 5
    num = volt / 800
    if(volt < 2.5):
      ntu = 3000;
    else:
      ntu = -1120.4*(volt**2)+5742.3*volt-4353.8; 
    
    
    #print(value)
    #print("----------")
    #print(num)
    print(f'{volt} V   ::  {ntu} NTU')
    '''
    time.sleep(0.5)