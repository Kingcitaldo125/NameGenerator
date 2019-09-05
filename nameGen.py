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
"Larry","Lenny","LeBron","Linus","Lucas","Luke",
"Mac","Marcus","Mark","Mat","Matt","Matthew","Michael","Mike","Mikey","Mitt","Morgan",
"Nick","Nicholas","Nolan",
"Orel","Oliver",
"Paul","Pete","Peter","Phillip",
"Quinn","Quincy",
"Randy","Ray","Rhys","Rob","Robert","Robby","Robbie","Ronald","Ron","Ren","Rick","Richard","Ricky","Rickey","Rudy","Ryan",
"Scott","Sean","Seth","Simon","Stan","Steve","Stephen","Steven","Stevie",
"Thomas","Timmy","Tim","Timmothy","Tommy","Travis","Trevor","Trey","Tony","Tom","Tyler",
"Vince","Vinny",
"William","Will","Willy","Willie","Winston",
"Xavier",
"Zach","Zachary","Zack","Zackary"]

ffNames = ["Amy","Ashley","Ashlee","Allison","Abigail","Ally","Abby","Alexandra","Anastasia","Ann","Anna","Annie","April",
"Barbara","Beth","Brandy","Brandi","Britt","Brittany",
"Carissa","Carley","Carla","Carli","Catherine","Cathy","Claire","Courtney",
"Darcy","Darla","Deb","Debra","Donna","Drew",
"Ellyse","Elly","Emily","Emma","Erica","Erin",
"Fredricka",
"Gemma","Gina",
"India","Ivanka",
"Jane","Jasmine","Jacqueline","Jackie","Janet","Jan","Jen","Jenna","Jennifer","Jes","Jess","Jessica",
"Katherine","Kathleen","Katrina","Kelly","Kelsey","Kristen",
"Laura","Lauren","Lisa","Lizzie","Lori","Lucy",
"Marianne","MaryAnn","Maryn","Mary","Melissa","Mel","Melanie","Melody","Mia","Morgan",
"Nancy","Nicole","November",
"Patrica","Pat","Patty",
"Quinn",
"Rhys","Roberta","Ruth",
"Sara","Sarah","Sean","Shanna","Shannon","Sharon","Stephanie","Susan","Suzy","Syd","Sydney",
"Tara","Theresa","Tina",
"Valerie","Veronica"]

mis = ["A.","B.","C.","D.","E.","F.","G.","H.","I.","J.","K.","L.","M.","N.","O.","P.","Q.","R.","S.","T.","U.","V.","W.","X.","Y.","Z."]

lNames = ["Aaron","Abbey","Abby","Adams","Andrews","Albers","Anderson","Anthony","Allen","Ashley","Austin","Arelt",
"Baker","Barrett","Bart","Barnes","Belcher","Betts","Blake","Black","Bond","Bonds","Brown","Bird","Bruce","Brule","Bryant","Burgundy","Butler","Byrd",
"Carpenter","Carter","Carver","Clark","Crawford","Collins","Cook","Coorey","Culberson","Culver",
"Dalton","Davis","Day","Devers","Dole","Donaldson","Donovan","Duffy","Dunn","Dykstra",
"Evans","Evers",
"Finch","Fry","Fuller",
"Gant","Gardner","George","Grant","Granderson","Gray","Greene",
"Hand","Hare","Harris","Hamilton","Harvey","Henderson","Hickey","Hill","Hudson",
"James","Jefferson","Jones","John","Johnson","Jordan","Joseph",
"King","Kelly","Kelley","Key","Klosterman","Knox",
"Lang","Leonard","Long",
"Mackey","Maddox","Madducks","Madden","Martin","McDonald","McGriff","McNabb","Metz","Miller","Moore","Morgan",
"Nelson","Nolan","Norman",
"Obrien","Oliver",
"Paul","Peter","Phillips","Price",
"Reynolds","Ritchie","Roberts","Robinson","Robertson","Romney","Ross","Rudy",
"Samberg","Sandburg","Scott","Shepherd","Simon","Simpson","Smith","Snyder","Stubbs","Sutcliffe",
"Taylor","Thomas","Travis","Trumpp",
"Vaughn","Volmer",
"Wallace","Walker","Walsh","Walters","Washington","Warren","Webb","Wills","Wilson","Winston","Wells","Wellington","White","William","Williams",
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
	
	doubleNameOdds = len(lNames)-3
	
	if trueRandom:
		lenList = []
		lenList.append(len(mfNames)-1)
		lenList.append(len(ffNames)-1)
		lenList.append(len(lNames)-1)
		lenList.append(len(mis)-1)
		lenList = sorted(lenList)
		cap = int(lenList[-1])
		
		masterList = truerandom.randRange(10,0,cap)
		time.sleep(1)
		masterList = [int(ii) for ii in masterList]
		if masterList[9] >= cap:
			return ("Larry The Cable Guy")
			
		masterListDecider = truerandom.randRange(50,0,len(masterList)-1)
		time.sleep(1)
		masterListDecider = [int(ii) for ii in masterListDecider]
			
		maleIndex = masterList[masterListDecider[random.randrange(0,len(masterListDecider))]]
		if maleIndex >= len(mfNames):
			maleIndex = random.randrange(0,len(mfNames))
		mfn = mfNames[maleIndex] # male first name
		
		
		femaleIndex = masterList[masterListDecider[random.randrange(0,len(masterListDecider))]]
		if femaleIndex >= len(ffNames):
			femaleIndex = random.randrange(0,len(ffNames))
		ffn = ffNames[femaleIndex] # female first name
		
		
		lastIndex = masterList[masterListDecider[random.randrange(0,len(masterListDecider))]]
		if lastIndex >= len(lNames):
			lastIndex = random.randrange(0,len(lNames))
		ln = lNames[lastIndex] # last name
		
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
			doubleNameLength = len(lNames)-1
			
			doubleLName = truerandom.randRange(1,0,doubleNameLength)
			doubleLName = [int(ii) for ii in doubleLName]
			
			doubleLNameDecider = truerandom.randRange(5,0,doubleNameLength)
			doubleLNameDecider = [int(ii) for ii in doubleLNameDecider]
			
			if doubleLName[0] >= doubleNameOdds:
				secondLName = lNames[doubleLNameDecider[random.randrange(0,len(doubleLNameDecider))]]
				return (ffn + " " + ln + "-" + secondLName)
			return (ffn + " " + ln)
	else:
		mfn = mfNames[random.randrange(0,len(mfNames))] # male first name
		ffn = ffNames[random.randrange(0,len(ffNames))] # female first name
		ln = lNames[random.randrange(0,len(lNames))] # last name

		choice = random.randrange(0,100)
		if choice <= 50:
			ch = random.randrange(0,50)
			chh = random.randrange(0,len(mis))
			if ch == 25:
				return (mfn + " " + mis[chh] + " " + ln)
			return (mfn + " " + ln)
		elif choice > 50 and choice <= 99:
			doubleLName = random.randrange(0,50)
			if doubleLName >= doubleNameOdds:
				secondLName = lNames[random.randrange(0,len(lNames))]
				return (ffn + " " + ln + "-" + secondLName)
			return (ffn + " " + ln)
		return ("Larry The Cable Guy")

windowNameLimit = 10

useTrueRandom = False
if len(sys.argv) == 2:
	nNames = int(sys.argv[1])
	for i in range(nNames):
		random.shuffle(mfNames)
		random.shuffle(ffNames)
		random.shuffle(mis)
		random.shuffle(lNames)
		print(i+1,genName(False))
elif len(sys.argv) == 3:
	nNames = int(sys.argv[1])
	if str(sys.argv[2]) == "true" or str(sys.argv[2]) == "True":
		useTrueRandom = True
	if useTrueRandom and nNames > windowNameLimit:
		print("Default True Random number of names is "+str(windowNameLimit))
		nNames = windowNameLimit # limit
	for i in range(nNames):
		random.shuffle(mfNames)
		random.shuffle(ffNames)
		random.shuffle(mis)
		random.shuffle(lNames)
		print(i+1,genName(useTrueRandom))
else:
	print(genName(useTrueRandom))
