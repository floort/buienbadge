import urequests
import ugfx
import network

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)       # Activate standalone interface
sta_if.scan()                                                    # Scan for available access points
sta_if.connect("SHA2017-insecure")                             # Connect to the public SHA2017 AP without a password
sta_if.isconnected()                                             # Check for successful connection
sta_if.ifconfig()                                                # Print connection information


r = urequests.get('https://br-gpsgadget-new.azurewebsites.net/data/raintext/?lat=52.28&lon=5.52')
lines = r.text.splitlines()

ugfx.clear(ugfx.BLACK)                                           # Clear screen
ugfx.string(120, 50, lines[0].split('|')[0], "Roboto_BlackItalic24", ugfx.WHITE) # Write a string to the center of the screen
ugfx.flush()                                                     # Send the update to the screen
