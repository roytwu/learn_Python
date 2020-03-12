import serial

#* baud-rate = 921600
port = "COM3"
baud = 115200
ser = serial.Serial(port, baud, timeout=1)

if ser.isOpen():
    print(ser.name + ' is open...')
    
ser.reset_input_buffer()

#line = ser.read()
#print(line)

ser.write("0xFF".encode())
ser.write("0x57".encode())
ser.write("0x03".encode())
ser.write("0x03".encode())
ser.write("0x5D".encode())



#while True:
#    cmd = input("enter command or exit: ") 
#    if cmd == 'exit':
#        ser.close()
#        exit()
        
ser.close()