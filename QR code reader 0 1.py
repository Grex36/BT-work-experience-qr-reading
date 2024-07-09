import serial


Piserial = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
print("Connected to: " + Piserial.portstr)


while True:
        if Piserial.in_waiting > 0:
            line = Piserial.readline().decode('utf-8').rstrip()
            qrcodevalue = line
            print(qrcodevalue)

ser.close()
