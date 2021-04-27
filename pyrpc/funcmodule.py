import time
import sqlite3

def set_up(cID):
	activity = {"startTimestamp":time.time()}
	activityKey = ["details", "state", "largeImageKey", "largeImageText", "smallImageKey", "smallImageText"]

	for i in activityKey:
		answer = input(f"Enter {i} = ")
		activity[i]=answer if not answer=='' else None

	button = input("Do you want set a button (yes/no) = ")
	if button.lower()=='yes' or button.lower()=='y':
		activity["buttons"]=[]
		for i in range(2):
			nums = ['st','nd']
			while True:
				label = input(f"Enter the LABEL for {i+1}{nums[i]} button = ")
				if label=='':
					print("LABEL cannot be empty please input again. ")
				else:
					break
			while True:
				buttonLink = input(f"Enter the URL for {i+1}{nums[i]} button = ")
				if label=='':
					print("URL cannot be empty please input again. ")
				else:
					break
			newButton = {"label":label,"url":buttonLink}
			activity["buttons"].append(newButton)
			if i==0:
				button = input("Do you want a second button? (yes/no) = ")
				if button.lower()=='yes' or button.lower()=='y':
					continue
				else:
					break

		if len(activity['buttons'])==0:
			activity['buttons']=None
	else:
		activity['buttons']=None
	save_data(activity, cID)

	return activity

def save_data(activity, cID):
	con = sqlite3.connect('database.db')
	c = con.cursor()
	select = c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name="discord"''')
	if len(select.fetchall())==0:
		c.execute('''CREATE TABLE discord(id INT, clientid INT,details TEXT, state TEXT, largeImageKey TEXT, largeImageText TEXT, smallImageKey TEXT, smallImageText TEXT, btlbl1 TEXT, bturl1 TEXT, btlbl2 TEXT, bturl2 TEXT)''')
		con.commit()
	if activity['buttons']==None:
		activity['btlbl1']=""
		activity['bturl1']=""
		activity['btlbl2']=""
		activity['bturl2']=""
	else:
		if(len(activity)==1):
			activity['btlbl1']=activity['buttons'][0]['label']
			activity['bturl1']=activity['buttons'][0]['url']
			activity['btlbl2']=""
			activity['bturl2']=""
		else:
			activity['btlbl1']=activity['buttons'][0]['label']
			activity['bturl1']=activity['buttons'][0]['url']
			activity['btlbl2']=activity['buttons'][1]['label']
			activity['bturl2']=activity['buttons'][1]['url']

	task = (cID, activity['details'], activity['state'],activity['largeImageKey'],activity['largeImageText'],activity['smallImageKey'],activity['smallImageText'],activity['btlbl1'],activity['bturl1'],activity['btlbl2'],activity['bturl2'])
	select = c.execute('''SELECT id FROM discord WHERE id=1''').fetchone()
	if select==None:
		sql = '''INSERT INTO discord(id,clientid,details,state,largeImageKey,largeImageText,smallImageKey,smallImageText,btlbl1,bturl1,btlbl2,bturl2) VALUES(1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
	else:
		sql = '''UPDATE discord SET clientid=?, details=?, state=?, largeImageKey=?, largeImageText=?, smallImageKey=?, smallImageText=?, btlbl1=?, bturl1=?, btlbl2=?, bturl2=?'''
	c.execute(sql,task)
	con.commit()
	con.close()

def storage():
	con = sqlite3.connect('database.db')
	c = con.cursor()
	select = c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name="discord"''')
	if len(select.fetchall())==0:
		c.execute('''CREATE TABLE discord(id INT, clientid INT,details TEXT, state TEXT, largeImageKey TEXT, largeImageText TEXT, smallImageKey TEXT, smallImageText TEXT, btlbl1 TEXT, bturl1 TEXT, btlbl2 TEXT, bturl2 TEXT)''')
		con.commit()
	select = c.execute('''SELECT * FROM discord WHERE id=1''').fetchone()
	if select==None:
		while True:
			cID = input("Enter client id = ")
			if not cID.isdigit():
				print("Client Id can only be integer = ")
			else:
				break
		c.execute('''INSERT INTO discord(id,clientid,details,state,largeImageKey,largeImageText,smallImageKey,smallImageText,btlbl1,bturl1,btlbl2,bturl2) VALUES(1,?,"","","","","","","","","","")''',(cID,))
		con.commit()
		select = (1,cID,"","","","","","","","","")
	con.close()
	return select

def existing_data():
	select = storage()
	activity = {"startTimestamp":time.time()}
	activityKey = ["clientId","details", "state", "largeImageKey", "largeImageText", "smallImageKey", "smallImageText"]
	for i in range(6):
		activity[activityKey[i]] = select[i+1] if not select[i+1]=="" else None
	if select[7]=="":
		activity['buttons']=None
	else:
		activity['buttons']=[]
		newButton = {"label":select[8],"url":select[9]}
		activity['buttons'].append(newButton)
		if not select[9]=="":
			newButton = {"label":select[10],"url":select[11]}
			activity['buttons'].append(newButton)
	return activity
