import random
import sys
import truerandom
import time

mfNames = ["Adam","Andrew","Albert","Alfred","Anthony","Aaron","Allan","Angelo","Andy","Austin",
"Barron","Barry","Bart","Benny","Bill","Blake","Brandon","Brian","Bryan","Brad","Brent","Brett","Bob","Bobby",
"Caleb","Carl","Casey","Charles","Chad","Chandler","Chester","Chris","Chuck","Chuckie","Charlie","Craig","Clark","Clyde","Coby","Cory","Corey","Cody","Curt","Curtis",
"Dalton","Daniel","Dan","Dale","Danny","Denny","Dennis","Dennison","Don","Dave","David","Dom","Dominick","Donovan","Darryl","Donald","Drew","Dru","Dustin",
"Earl","Edward","Ed","Edd","Eddie","Eddy","Edsger","Eric",
"Frank","Frankie","Fred","Freddy","Freddie","Fuller",
"Garry","Greg","Geoff","George","Gerald",
"Harry","Harold","Hank","Henry","Horace",
"Ian","Ivan",
"Jacoby","Jake","Jacob","James","Jimmy","Jim","Jerry","Jeff","Jeremy","John","Jon","Joe","Johnny","Jordan","Joseph","Joshua","Josh","Julian","Justin",
"Karl","Kawhi","Kevin","Kody","Kory","Kyle",
"Larry","Lenny","LeBron","Linus",
"Mac","Mat","Matt","Matthew","Michael","Mike","Mikey","Mitt",
"Nick","Nicholas",
"Orel","Oliver",
"Paul","Pete","Peter","Phillip",
"Quinn","Quincy",
"Randy","Ray","Rhys","Rob","Robert","Robby","Robbie","Ronald","Ron","Ren","Rick","Richard","Ricky","Rickey","Rudy","Ryan",
"Scott","Sean","Seth","Simon","Stan","Steve","Stephen","Steven","Stevie",
"Thomas","Timmy","Tim","Timmothy","Tommy","Travis","Trevor","Trey","Tony","Tom","Tyler",
"Vince",
"William","Will","Willy","Willie","Winston",
"Xavier",
"Zach","Zachary","Zack","Zackary"]

ffNames = ["Amy","Ashley","Ashlee","Allison","Abigail","Ally","Abby","Alexandra","Anastasia","Ann","Anna","Annie","April",
"Barbara","Beth","Brandy","Brandi","Britt","Brittany",
"Carissa","Carley","Carla","Carli","Catherine","Cathy","Claire",
"Darcy","Darla","Deb","Debra","Donna","Drew",
"Ellyse","Elly","Emily","Emma","Erica","Erin","Euvondia",
"Fredricka",
"Gemma","Gina",
"India","Ivanka",
"Jane","Jasmine","Jacqueline","Jackie","Janet","Jan","Jen","Jenna","Jennifer","Jes","Jess","Jessica",
"Katherine","Kathleen","Katrina","Kelly","Kelsey","Kristen",
"Laura","Lauren","Lisa","Lizzie","Lori","Lucy",
"Marianne","MaryAnn","Maryn","Mary","Melissa","Mel","Melanie","Melody","Mia",
"Nancy","Nicole","November",
"Patrica","Pat","Patty",
"Quinn",
"Rhys","Roberta","Ruth",
"Sara","Sarah","Sean","Shanna","Shannon","Sharon","Stephanie","Susan","Suzy","Syd","Sydney",
"Tara","Theresa","Tina",
"Veronica"]

mis = ["A.","B.","C.","D.","E.","F.","G.","H.","I.","J.","K.","L.","M.","N.","O.","P.","Q.","R.","S.","T.","U.","V.","W.","X.","Y.","Z."]

lNames = ["Aaron","Abbey","Abby","Adams","Andrews","Albers","Anderson","Anthony","Allen","Ashley","Austin","Arelt",
"Barrett","Bart","Belcher","Betts","Blake","Bond","Bonds","Brown","Bird","Bruce","Brule","Bryant","Burgundy","Butler","Byrd",
"Carpenter","Carter","Carver","Clark","Crawford","Collins","Coorey","Culberson","Culver",
"Dalton","Davis","Day","Devers","Dole","Donaldson","Donovan","Duffy","Dunn","Dykstra",
"Evers",
"Fry","Fuller",
"Gant","Gardner","George","Grant","Granderson",
"Hand","Hare","Harris","Henderson","Hickey","Hill",
"James","Jefferson","Jones","John","Johnson","Jordan","Joseph",
"Klosterman","Knox",
"Lang","Leonard","Long",
"Mackey","Maddox","Madducks","Madden","Martin","McDonald","McGriff","McNabb","Miller","Moore",
"Nelson",
"Oliver",
"Paul","Peter","Phillips","Price",
"Reynolds","Ritchie","Roberts","Robinson","Robertson","Romney","Rudy",
"Samberg","Sandburg","Shepherd","Simon","Simpson","Smith","Snyder","Stubbs","Sutcliffe",
"Taylor","Thomas","Travis","Trumpp",
"Vaughn","Volmer",
"Wallace","Walker","Walsh","Washington","Warren","Webb","Wills","Wilson","Winston","Wells","Wellington","White","William","Williams",
"Xavier",
"Young"]

def genName(trueRandom):
	"""
	Generate a single random full name using first and last names
	if the user wants a true random experience, name generation will take longer
	"""
	global mfNames
	global ffNames
	global mis
	global lNames
	
	if trueRandom:
		lenList = []
		lenList.append(len(mfNames)-1)
		lenList.append(len(ffNames)-1)
		lenList.append(len(lNames)-1)
		lenList.append(len(mis)-1)
		lenList = sorted(lenList)
		#print(lenList)
		#print("Cap:",cap)
		cap = int(lenList[-1])
		
		masterList = truerandom.randRange(10,0,cap)
		time.sleep(1)
		masterList = [int(ii) for ii in masterList]
		#masterList = sorted(masterList)
		#print(masterList)
		if masterList[9] >= cap-2:
			return ("Larry The Cable Guy")
			
		masterListDecider = truerandom.randRange(50,0,len(masterList)-1)
		time.sleep(1)
		masterListDecider = [int(ii) for ii in masterListDecider]
			
		maleIndex = masterList[masterListDecider[random.randrange(0,len(masterListDecider))]]
		if maleIndex >= len(mfNames):
			maleIndex = random.randrange(0,len(mfNames))
		mfn = mfNames[maleIndex]
		
		
		femaleIndex = masterList[masterListDecider[random.randrange(0,len(masterListDecider))]]
		if femaleIndex >= len(ffNames):
			femaleIndex = random.randrange(0,len(ffNames))
		ffn = ffNames[femaleIndex]
		
		
		lastIndex = masterList[masterListDecider[random.randrange(0,len(masterListDecider))]]
		if lastIndex >= len(lNames):
			lastIndex = random.randrange(0,len(lNames))
		ln = lNames[lastIndex]
		
		#print(mfn,maleIndex,ffn,femaleIndex,ln,lastIndex)
		
		mListDecider = masterListDecider[random.randrange(0,len(masterListDecider))]
		chhDecider = masterListDecider[random.randrange(0,len(masterListDecider))]
		initialDecider = masterListDecider[random.randrange(0,len(masterListDecider))]
		
		if masterList[mListDecider] > cap-int(cap/2) and masterList[mListDecider] <= cap:
			chh = masterList[chhDecider]
			if int(masterList[initialDecider]) == int(cap/2):
				if chh >= len(mis):
					chh = random.randrange(0,len(mis))
					return (mfn + " " + mis[chh] + " " + ln)
			return (mfn + " " + ln)
		elif masterList[mListDecider] <= cap-int(cap/2):
			return (ffn + " " + ln)
	else:
		mfn = mfNames[random.randrange(0,len(mfNames))]
		ffn = ffNames[random.randrange(0,len(ffNames))]
		ln = lNames[random.randrange(0,len(lNames))]

		choice = random.randrange(0,100)
		if choice <= 50:
			ch = random.randrange(0,50)
			chh = random.randrange(0,len(mis))
			if ch == 25:
				return (mfn + " " + mis[chh] + " " + ln)
			return (mfn + " " + ln)
		elif choice > 50 and choice <= 98:
			return (ffn + " " + ln)
		return ("Larry The Cable Guy")


useTrueRandom = False
#useTrueRandom = True

if len(sys.argv) == 2:
	nNames = int(sys.argv[1])
	if useTrueRandom and nNames > 10:
		nNames = 10 # limit
	for i in range(nNames):
		print(i+1,genName(useTrueRandom))
else:
	print(genName(useTrueRandom))
