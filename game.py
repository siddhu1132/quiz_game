print("Welcome to my Computer quiz!!!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()


print("Okay! Let's play :)")

score = 0

answer = input("1. What does CPU stand for? ")

if answer.lower() == "central processing unit":

    print('Correct!')

    score += 1

else:
    print("Incorrect!")


answer = input("2. What does GPU stand for? ")

if answer.lower() == "graphics processing unit":

    print('Correct!')

    score += 1

else:
    print("Incorrect!")


answer = input("3. What does RAM stand for? ")

if answer.lower() == "random access memory":

    print('Correct!')

    score += 1

else:
    print("Incorrect!")

print(f"You got {score} questions Correct!")

print(f"You got {(score /3) * 100} %")
