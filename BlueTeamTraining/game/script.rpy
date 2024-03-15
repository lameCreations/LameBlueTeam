# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define n = Character("Narrator", image="narrator")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene darkcyberbg

  

    show narrator sensai at left 


    n sensai "Welcome to this beginning tutorial on how to learn CyberSecurity Principles"
    n sensai "I am the Log Analyis Made Easy (L.A.M.E.) ninja sensai"
    n sensai "I have put this training together to cover many of the principles needed to succeed in the cyber security field"
    n sensai "The goal of this training is to make it available to anyone regardless of whether or not you have the infrastructure."
    n sensai "I plan to give you the tools to be able to do this at your own environment, but if you can't install the software, we will simulate it here in this training"
    
    jump mainMenu

    n sensai "Well this concludes the sharing portion of this meeting" 

    # This ends the game.

    return


label mainMenu:
    scene darkcyberbg
    menu:
        "What would you like to do?"

        "Review the simulated environment":
            n sensai "A wise choice to know your own network before proceeding"
            jump inventory_info

        "Learn scripting tools such as PowerShell.":
            jump powershellOverview

        "Learn about network logs":
            jump networklogOverview

        "Learn about host Logs":
            jump hostlogOverview
    
        "Learn about Cyber Tools.":
            n sensai "Cyber Tools abound"
            jump security_tools

        "Try some of the scenarios for detection":
            n sensai "Bold move if you haven't had any training"       