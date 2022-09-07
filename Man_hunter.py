print("\nVampire Dracula is finally free.\n Amarjeet has never lost a battle against the undead,but now their fortress is compromised and Dracula is roaming Creeksville.\n It is up to Amarjeet to take the unbeatable monster, but will he be able to contain him? \n")

#Loop conditions
flag = True

while flag != False:
    decide_player = input("Pick a game character.\n Type in 'vampire' to be a vampire or 'human' to be human:  \n").lower()

    if decide_player == "human":
        flag = False
        print("Amarjeet has a chance to fight back Dracula.\n He is going to use his weapons and skills to outwit Dracula.\n He has to find a way to be stronger than his enemy.\n Dracula will try his best to capture Amarjeet alive.\n Amarjeet will do everything he can do and try not to lose at all costs.\n You decide your next steps using 'Y' for Yes and 'N' for No.\n")

    elif decide_player == "vampire":
        flag = False
        print("\nOnce released,Dracula is a force to be reckone with.\n His powerful hypnotic abilities makes it easy for him to brainwash his victims and he enjoys playing tricks on those who try to stop him.\n Using the power of necromancy and shapeshifting,he's unmatched in his ability to protect himself from any harm.\n He is thirsty for blood,having never drunk from a human since he has been inprisoned four centuries ago.\n You decide your next steps by using 'Y' for yes and 'N' for no \n")

        #Players list of skillsets
        v_skill_set = ["Necromancy", "Hypnosis", "Shapeshifting"]
        
        #Decide
        vamp_list = int(input("Pick a skill set: 0. Necromancy 1. Hypnosis 2. Shapeshifting\n"))
        
        #To be used throughout the story
        skill = v_skill_set[vamp_list]
  
    else:
        print("Please input a correct option!")
        