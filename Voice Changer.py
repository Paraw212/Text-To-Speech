import pyttsx3


P4R4W = pyttsx3.init() 
rate = P4R4W.getProperty("rate")
volume = P4R4W.getProperty("volume")
voices = P4R4W.getProperty("voices")


P4R4W.setProperty("rate",150)

P4R4W.setProperty("volume", 200)

P4R4W.setProperty("voice", voices[1].id)


P4R4W.say("Subscribe My Channel" )
#My Channel Link: https://www.youtube.com/channel/UC6zk8S5Fsdd31hhTBnKBrBA?sub_confirmation=1


P4R4W.runAndWait()
P4R4W.stop()
