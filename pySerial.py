import serial

#* baud-rate = 921600
port = "COM4"
baud = 921600
ser = serial.Serial(port, baud, timeout=1)

if ser.isOpen():
    print(ser.name + ' is open...')
    
ser.reset_input_buffer()

line = ser.readline()
print(line)


#ser.close()

#while True:
#    cmd = input("Enter command or exit: ") 
#    if cmd == 'exit':
#        ser.close()
#        exit()