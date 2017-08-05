import urequests
import ugfx
import network
import badge

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)       # Activate standalone interface
sta_if.scan()                                                    # Scan for available access points
sta_if.connect("SHA2017-insecure")                             # Connect to the public SHA2017 AP without a password
sta_if.isconnected()                                             # Check for successful connection
sta_if.ifconfig()                                                # Print connection information


r = urequests.get('https://br-gpsgadget-new.azurewebsites.net/data/raintext/?lat=52.28&lon=5.52')
lines = r.text.splitlines()
raindata = [int(lines[i].split('|')[0]) for i in range(len(lines))]

if sum(raindata) > 0:
    # Plot graph
    ugfx.clear(ugfx.WHITE)
    for i in range(len(raindata)):
        ugfx.area(12*i,127-(raindata[i]//2), 11, 127, ugfx.BLACK)
    ugfx.flush()
    
    badge.leds_init()
    badge.leds_send_data(bytes([0, 0, raindata[0]//2, 0]*6) ,24) # all blue with intensity of current rain
    badge.vibrator_init()
    badge.vibrator_activate(9)
    sleep(2)
    badge.leds_disable()
