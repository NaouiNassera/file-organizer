from organize_file import organize_directory

print(" Hello There , your folder is in mess ? wanna organize it a bit ? \n")
print(" If this the case write yes otherwise no !\n")
choice = input()

if choice == "yes" : 
    print("Give me the name of your directory : \n")
    direct = input()
    organize_directory(direct)
    print("it's done , check the result \n")
elif choice == "no" : 
    print("see You next time \n")
else :
    print("I don't understand your choice")

