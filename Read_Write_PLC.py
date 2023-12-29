# Mk1:  organized 
#Const Values---------------------------------------------------------------------------------------------
DB_NUMBER= 2
REAL_SIZE= 4
KP_OFFSET= 0
TI_OFFSET= 4
TD_OFFSET= 8

#Libraries---------------------------------------------------------------------------------------------
import snap7
import time


#Setup---------------------------------------------------------------------------------------------
#Conection Setup
plc = snap7.client.Client()
plc.connect('192.168.0.25', 0, 1) #ip, rack, slot

#Takes buffer for each variable
Kp = plc.db_read(DB_NUMBER,KP_OFFSET,REAL_SIZE)
Ti = plc.db_read(DB_NUMBER,TI_OFFSET,REAL_SIZE)
Td = plc.db_read(DB_NUMBER,TD_OFFSET,REAL_SIZE)

Value_Kp=2.5
Value_Ti=10.1
Value_Td=50
count=0

#Endless loop ---------------------------------------------------------------------------------------------
while(True):
    Value_Kp+=1 #Keep changing values sent to the DB
    Value_Ti+=1
    Value_Td+=1

    #Writes in the buffer
    snap7.util.set_real(Kp,0,Value_Kp)
    snap7.util.set_real(Ti,0,Value_Ti)
    snap7.util.set_real(Td,0,Value_Td)

    #writes in the plc DB
    plc.db_write(DB_NUMBER,KP_OFFSET,Kp)
    plc.db_write(DB_NUMBER,TI_OFFSET,Ti)
    plc.db_write(DB_NUMBER,TD_OFFSET,Td)


    #Reading DB
    DB_bytearray = plc.db_read(DB_NUMBER,0,12)
    Kp_current = snap7.util.get_real(DB_bytearray,KP_OFFSET) #DB, start
    Ti_current = snap7.util.get_real(DB_bytearray,TI_OFFSET)
    Td_current = snap7.util.get_real(DB_bytearray,TD_OFFSET)

    print("\nVALUES FROM PID:\nKp: ", Kp_current, "\nTi : ", Ti_current, "\nTd: ", Td_current)
    
    count+=1
    print("\nNumber of successful transmissions: ",count)
    time.sleep(5) 
#---------------------------------------------------------------------------------------------







