

#This script that advretises a bluetooth low enrgy beacon for 15 seconds 
#penentaration example right here 
#class library using bluetooth in time 
#this is you writing acutally python scripts
import time #<----- First part class moudle it manuiplues time 

from bluetooth.ble import BeaconService #<--third party module ; the score board you see at the bottom of the espn screen dis the same concept

#create an instance of the object from the 3rd party class 

service = BeaconService() #<- 

#now you want to start to advertise 

service.start_advertising.("11111111-2222-3333-4444-555555555555",1, 1,1, 200)#<---UUID created a skelton example different ports TCP,UDP


time.sleep(15) #<-----low energy beacon for 15 seconds 

service.stop_advertising()  #<----stop the bluetooth connection 

print("Done.") #<---- you already know this is going to pop up on the screen saying done