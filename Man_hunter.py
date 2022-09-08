print(" Vampire Dracula is finally free.\n Amarjeet has never lost a battle against the undead,but now their fortress is compromised and Dracula is roaming Creeksville.\n It is up to Amarjeet to take the unbeatable monster, but will he be able to contain him? \n")

#Loop conditions
flag = True

while flag != False:
    decide_player = input("Pick a game character.\n Type in 'vampire' to be a vampire or 'human' to be human:  \n").lower()

    if decide_player == "human":
        flag = False
        print("Amarjeet has a chance to fight back Dracula.\n He is going to use his weapons and skills to outwit Dracula.\n He has to find a way to be stronger than his enemy.\n Dracula will try his best to capture Amarjeet alive.\n Amarjeet will do everything he can do and try not to lose at all costs.\n You decide your next steps using 'Y' for Yes and 'N' for No.\n")
        #human skillsets
        
        h_skill_set = ["Gun with silver bullets","Arsonry", "Holywater"]
        
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
        
    elif decide_player == "vampire":
        flag = False
        print(" Once released,Dracula is a force to be reckone with.\n His powerful hypnotic abilities makes it easy for him to brainwash his victims and he enjoys playing tricks on those who try to stop him.\n Using the power of necromancy and shapeshifting,he's unmatched in his ability to protect himself from any harm.\n He is thirsty for blood,having never drunk from a human since he has been inprisoned four centuries ago.\n You decide your next steps by using 'Y' for yes and 'N' for no \n")

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
        
        print(" The Great Dracula has finally awoken.\n 'After 400 years i'm alive once again.\n Time to get my revenge on those who trapped me here.' Dracula says\n He attempts to use his powers but realizes he's still weak.\n 'Must gain energy, i can see the blood moon rising', He says.")
        
        #Would vary for each skillset
        if  skill == "Necromancy":
            print("He raised the dead to harvest humans for his enjoyment")
        
        elif skill == "Hypnosis":
            print("He charms a villager and lures him to his den.")
        
        elif skill == "Telekinesis":
            print("With the ability to nove things with his mind. He takes advantage of a passer-by")
            

    else:
        print("Please input a correct option!")
