import time
import webbrowser

i = 0

print("this program started on " + time.ctime())
while i<3: # add a loop to this code so it prompts the user to take 3 breaks
    time.sleep(5) # waiting for 5 second before running the next code
    webbrowser.open("http://www.facebook.com")
    i+=1