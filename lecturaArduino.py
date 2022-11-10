import serial
import numpy as np
from envioCorreo import Correo

N = True
arduino = serial.Serial("COM4", baudrate=9600, timeout=1.0)
with arduino:
    ii = 0
    while N:
        try:
            line = arduino.readline()
            if not line:
                continue
            cad = np.fromstring(line.decode('ascii', errors='replace'), sep=' ')
            if cad[0] > 400:
                Correo.Generar()
                N = False
            print(cad[0])
        except KeyboardInterrupt:
            print("Exiting")
            break