print(" Vampire Dracula is finally free.\n Amarjeet has never lost a battle against the undead,but now their fortress is compromised and Dracula is roaming Creeksville.\n It is up to Amarjeet to take the unbeatable monster, but will he be able to contain him? ")

#Loop conditions
flag = True

while flag != False:
	decide_player = input(" Pick a game character.\n Type in 'vampire' to be a vampire or 'human' to be human:  \n").lower()

	if decide_player == "human":
		flag = False
		print(" Humans have chance to fight back against the vampires.\n They are going to use their weapons and skills to outwit the vampires.\n They have to find a way to be stronger than their enemy.\n The vampires will try their best to capture humans alive.\n The humans will do everything they can do and try not to loose at all costs.\n You decide your next steps using 'Y' for Yes and 'N' for No.\n")

	if decide_player == "vampire":
		flag = False
		print(" Once released,Dracula is a force to be reckone with.\n His powerful hypnotic abilities makes it easy for him to brainwash his victims and he enjoys playing tricks on those who try to stop him.\n Using the power of necromancy and shapeshifting,he's unmatched in his ability to protect himself from any harm.\n He is thirsty for blood,having never drunk from a human since he has been inprisoned four centuries ago.")

	else:
		print("Please input a correct option!")
