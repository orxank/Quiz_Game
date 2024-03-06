print("Hi, Player! Welcome to my quiz game!\n")

player_conf = input("Do you want to play?: ")

if player_conf.lower() != "yes":
    print("See you next time!")
    quit()

player_score = 0

quiz1 = input("1. Question: What is the capital of Japan?\n\n"
              "A) Beijing\n"
              "B) Seoul\n"
              "C) Tokyo\n"
              "D) Bangkok\n\n"
              "Your answer: ")

if quiz1.lower() == "tokyo":
    print("Wow, you are correct!")
    player_score += 1
    print("Your Score: " + str(player_score))
else:
    print("Hmm, inccorect. Let's try another one.")
    player_score -= 1
    print("Your Score: " + str(player_score))

quiz2 = input("2. Question: Which city serves as the capital of Australia?\n\n"
                "A) Sydney\n"
                "B) Melbourne\n"
                "C) Canberra\n"
                "D) Brisbane\n\n"
                "Your answer: ")
                
if quiz2.lower() == "canberra":
    print("Wow!, Once again you are correct!")
    player_score += 1
    print("Your Score: " + str(player_score))
else:
    print("Incorrect, let's check next quiz.")
    player_score -= 1
    print("Your Score: " + str(player_score))

quiz3 = input("3. Question: What is the capital of Brazil?\n\n"
              "A) Rio de Janeiro\n"
              "B) Brasilia\n"
              "C) Sao Paulo\n"
              "D) Salvador\n\n"
              "Your answer: ")

if quiz3.lower() == "brasilia":
    print("Wow, you are correct!")
    player_score += 1
    print("Your Score: " + str(player_score))
else:
    print("Hmm, inccorect. Let's try another one.")
    player_score -= 1
    print("Your Score: " + str(player_score))

quiz4 = input("4. Question: The capital of Canada is?\n\n"
              "A) Toronto\n"
              "B) Ottawa\n"
              "C) Vancouver\n"
              "D) Montreal\n\n"
              "Your answer: ")

if quiz4.lower() == "ottawa":
    print("Wow!, Once again you are correct!")
    player_score += 1
    print("Your Score: " + str(player_score))
else:
    print("Incorrect, let's check next quiz.")
    player_score -= 1
    print("Your Score: " + str(player_score))

quiz5 = input("5. Question: The capital of Azerbaijan is?\n\n"
              "A) Ganja\n"
              "B) Sumqayit\n"
              "C) Baku\n"
              "D) Shamaxi\n\n"
              "Your answer: ")

if quiz5.lower() == "baku":
    print("Wow!, Once again you are correct!")
    player_score += 1
    print("Your Score: " + str(player_score))
else:
    print("Incorrect, let's check next quiz.")
    player_score -= 1
    print("Your Score: " + str(player_score))