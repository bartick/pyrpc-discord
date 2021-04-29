import sys
from .classmodule import MyClass
from .funcmodule import set_up, existing_data, update_specific_data

def main():
    if not (sys.version_info.major == 3 and sys.version_info.minor >= 5):
        print("This script requires Python 3.5 or higher!")
        print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
        sys.exit(1)
    args = sys.argv
    args.append('')
    if(args[1].lower()=='start'):
        while True:
            cID = input("Enter client id = ")
            if not cID.isdigit():
                print("Client Id can only be integer = ")
            else:
                break
        activity = set_up(cID)
        activity["clientId"]=cID
        richPresence(activity)
    elif(args[1].lower()=='autostart'):
        activity = existing_data()
        richPresence(activity)
    else:
    	print("""
    	              Discord Rich Presence
    	===================================================
    	start     : Starts an ineractive setup to start RPC
    	===================================================
    	autostart : AutoStarts RPC from database
    	""")

def richPresence(activity):
    opt = ["state", "details", "largeImageKey", "largeImageText", "smallImageKey", "smallImageText", "clientId"]
    ob = MyClass(activity['clientId'])
    b = ob.connect()
    if b:
        ob.statusUpdate(activity)
        while True:
            x = input()
            if x.lower()=="update":
                activity = set_up(activity['clientId'])
                ob.statusUpdate(activity)
            elif x in opt:
                update_specific_data(x)
                activity = existing_data()
                ob.statusUpdate(activity)
            elif x.lower()=='end':
                ob.close_presence()
                break
            else:
                print("""
               Discord Rich Presence After Start Up
        ====================================================================
        updates        : Starts an ineractive setup to update RPC
        ====================================================================
        clientId       : Changes your current client id to a new one
        ====================================================================
        state          : Changes your current state to a new one
        ====================================================================
        details        : Changes your current details to a new one
        ====================================================================
        largeImageKey  : Changes your current large image key to a new one
        ====================================================================
        largeImageText : Changes your current large image text to a new one
        ====================================================================
        smallImageKey  : Changes your current small image key to a new one
        ====================================================================
        smallImageText : Changes your current small image text to a new one
        ====================================================================
        end            : closes RPC server
    """)

if __name__ == '__main__':
    main()