print(" Vampire Dracula is finally free.\n Amarjeet has never lost a battle against the undead,but now their fortress is compromised and Dracula is roaming Creeksville.\n It is up to Amarjeet to take the unbeatable monster, but will he be able to contain him? \n")

#Loop conditions
flag = True

while flag != False:
	decide_player = input("Pick a game character.\n Type in 'vampire' to be a vampire or 'human' to be human:  \n").lower()

	if decide_player == "human":
		flag = False
		print("Amarjeet has a chance to fight back Dracula.\n He is going to use his weapons and skills to outwit Dracula.\n He has to find a way to be stronger than his enemy.\n Dracula will try his best to capture Amarjeet alive.\n Amarjeet will do everything he can do and try not to lose at all costs.\n You decide your next steps using 'Y' for Yes and 'N' for No or by choosing a number from a list of options.\n")
		
  		#human skillsets
		
		h_skill_set = ["Gun with silver bullets","Arsonry","Holywater"]
		
		flag = True
		
		while flag != False:
			
			#pick skill
			hman_list = int(input(" Pick a skill set:\n 0.Gun with silver bullets\n 1.Arsonry\n 2.Holywater\n Pick a number to continue\n"))
			
			if hman_list == 0:
				flag = False
				print("You chose Gun with silver bullets.")
			elif hman_list == 1:
				flag = False
				print("You chose Arsonry.")
			elif hman_list == 2:
				flag = False
				print("You chose Holywater.")
			else:
				print("Please select the correct input")
		
		skill_set = h_skill_set[hman_list]
		
		print("\n The village chief has summoned me to fight the great dracula that has been terrorizing the good people of Creeksville.\n I Amarjeet vows to fight to the death and kill the vampire for good.")
		
		#varies for skill set chosen
		print("\n𝖘𝖐𝖎𝖑𝖑 𝖘𝖊𝖙 𝖉𝖊𝖈𝖎𝖘𝖎𝖔𝖓 𝖎𝖓𝖈𝖔𝖒𝖎𝖓𝖌")
		if skill_set == "Gun with silver bullets":
			print("\n🏃I bring out my gun and clean it")
		elif skill_set == "Arsonry":
			print("\n🏃You light up the touch with excitment.")
		elif skill_set == "Holywater":
			print("\n🏃I sprinkle holywater and make the sign of the cross")
   
		print("You are finally ready to start the war with you an Dracula.\n What would be your choice be?")
  
		dec_1 = int(input("\n 1.Wait for Dracula to attack or 2.March straight to the castle. \nType a number to continue. "))
		if dec_1 == 1:
			print("You hear an angry mob marching to your home.\n A lot of undead and hypnotized beigns roam the street.\n You hear loud crying from the neighborhood.\n 'i have to act quick,' you say.")
		elif dec_1 == 2:
			print("You gather some items that you would use to get to the vampire's castle.")

		dec_2 =input("You were finally able to escape the village and you were very thirsty.\n You see a near by river. Do you drink from it? Y or N\n").upper()
		if dec_2 == "Y":
			print("you drink the water only to find out it was spiked.\n You start hallucinating and then you pass out losing daylight")
			print("You wake up feeling a bit dizy\n'Was it the water?'you say\n")
		
		elif dec_2 == "N":
			print("You pass out from dehydration.Losing daylight.")
			print("You wake up feeling drenched.\nYou notice that rain is failing\nYou drink some of the rain water and it makes you a bit weaker\n'Must continue',you say.")
		
		dec_3 = int(input("You come across a two way path\n 1.To get on the left path 2.To get on the right path\n"))
		
		if dec_3 == 1:
			print("You chose the left path. You come across the undead")
		
		elif dec_3 == 2:
			print("You chose the right path. Your path is blocked by hypnotized enemies.")
<<<<<<< HEAD
			if skill_set == "Gun with silver bullets":
				print("You knock out the charmed humans with the butt of your gun.")
			
			elif skill_set == "Arsonry":
				print("You circle them up in a large wall of fire so they don't reach you.")
			
			elif skill_set == "Holywater":
				print("Holy water is ineffective against them. You sustained some injuries and barely escaped")
=======
   
   
>>>>>>> a101ec45e0cafa2ae9a98744f9aab90f4d5780db
	elif decide_player == "vampire":
		flag = False
		print(" Once released,Dracula is a force to be reckone with.\n His powerful hypnotic abilities makes it easy for him to brainwash his victims and he enjoys playing tricks on those who try to stop him.\n Using the power of necromancy and shapeshifting,he's unmatched in his ability to protect himself from any harm.\n He is thirsty for blood,having never drunk from a human since he has been inprisoned four centuries ago.\n You decide your next steps by using 'Y' for yes and 'N' for no or choosing a number from a list of options. \n")

		#Players list of skillsets
		v_skill_set = ["Necromancy", "Hypnosis", "Telekinesis"]
		
		flag = True
		
		while flag != False:
			#Decide
			vamp_list = int(input(" Pick a skill set:\n 0.Necromancy\n 1.Hypnosis\n 2.Telekinesis\n Pick a number to continue.\n"))
		
			if vamp_list == 0:
				flag = False
				print("You chose Necromancy.")
			
			elif vamp_list == 1:
				flag = False
				print("You chose Hypnosis.")
			elif vamp_list == 2:
				flag = False
				print("You chose Telekinesis.")
			else:
				print("Please input a correct number")
		
		#To be used throughout the story
		skill = v_skill_set[vamp_list]
		
		print("\n The Great Dracula has finally awoken.\n 'After 400 years i'm alive once again.\n Time to get my revenge on those who trapped me here.' Dracula says\n He attempts to use his powers but realizes he's still weak.\n 'Must gain energy, i can see the blood moon rising', He says.\n He actives an ability with the little strength left.")
		print("\n𝖘𝖐𝖎𝖑𝖑 𝖘𝖊𝖙 𝖉𝖊𝖈𝖎𝖘𝖎𝖔𝖓 𝖎𝖓𝖈𝖔𝖒𝖎𝖓𝖌")
		
		#Would vary for each skillset
		if  skill == "Necromancy":
			print("\n🏃With his necromancy skill he raised the dead to harvest humans for his enjoyment")
					
		elif skill == "Hypnosis":
			print("\n🏃Using hynosis he charms a villager and lures him to his den.")
		
		elif skill == "Telekinesis":
			print("\n🏃With his telekinesis. He takes advantage of a passer-by")
				
		print("\nA group of villagers are killed by a vampire.\n When they wake the next morning, a bunch of villagers run to the village chief.\n The villagers say that there must be someone who can fight this vampire.\n I would send Amarjeet he ends up saying.\n The villages leave feeling relieved.\n")
		print("\n 'I can sense the human coming what is his name?' Dracula says.\n 'He is no match for me. Now to make my next move.' he adds.\n")
				
		print("\n𝖘𝖐𝖎𝖑𝖑 𝖘𝖊𝖙 𝖉𝖊𝖈𝖎𝖘𝖎𝖔𝖓 𝖎𝖓𝖈𝖔𝖒𝖎𝖓𝖌")
		if skill == "Necromancy":
			print(" You are finally ready to go to war with the humans.What would you do?")
			decide1 = int(input("1.Raise an army of the dead to fight\n2.Let the fight come to you\n"))
			
			if decide1 == 1:
				print("You raised an army of the dead to kill Amarjeet. \nThey won't stop at nothing till they get him")
				print("\nAmarjeet fought the undead as they kept on respawning.\nHe barely escaped and hid with an old man.\nThe old man shows him a secret path to get the castle")
			elif decide1 == 2:
				print("You prepare an army of the undead in to guard the castle")
    
		elif skill == "Hypnosis":
			print(" You're finally ready to go to war with the the humans. What would your choice be?")
			decide2 = int(input("1.Capture humans and use them to fight your war\n2.Let the fight come to you\n"))
			if decide2 == 1:
				print("You charmed a few humans and sent them to kill Amarjeet.")
				print("\nAmarjeet knocked out the charmed humans.\nGot into the castle in pursuit of the vampire")
			elif decide2 == 2:
				print("You summon villagers to guard the castle")
    
		elif skill == "Telekinesis":
			print(" You're finally ready to go to war with the the humans. What would your choice be?")
			print("Fight the humans\n")
			
			
	else:
		print("Please input a correct option!")