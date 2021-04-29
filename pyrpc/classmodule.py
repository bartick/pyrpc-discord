from pypresence import Presence
import os

class MyClass():
    def __init__(self, client_id):
    	self.client_id = client_id
    	self.RPC = Presence(self.client_id)

    def connect(self):
    	try:
            self.RPC.connect()
            return True
    	except Exception as e:
            print(str(e))
            return False

    def statusUpdate(self, state):
        try:
            self.RPC.update(details=state['details'],state=state["state"],start=state["startTimestamp"],large_image=state['largeImageKey'], large_text=state["largeImageText"],small_image=state['smallImageKey'], small_text=state["smallImageText"], buttons=state["buttons"])
        except Exception as e:
            print(str(e))

    def close_presence(self):
        try:
            self.RPC.clear(pid=os.getpid())
        except Exception as e:
            print(str(e))
