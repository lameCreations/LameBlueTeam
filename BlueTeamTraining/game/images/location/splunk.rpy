label splunk:
    scene darkcyberbg
    n sensai "Welcome to the world of Splunk"
    n sensai "You may be wondering what Splunk is, or you may already have a knowledge of the tool and would better like to learn how to use the tool"
    n sensai "I will provide you an overview of the technology,"
    n sensai "minimum information to set it up in a home lab, "    
    n sensai "instructions on how to set up a more complicated network"
    n sensai "instructions on how to do day to day searches"
    #scene darkcyberbg

    call screen splunkOverview

screen splunkOverview:
    modal True
    imagemap:
        ground "splunkMenu.png"
        hotspot (92, 62, 237, 240) action Jump("splunkHelpGuide")
        hotspot (539, 49, 258, 275) action Jump("splunkHomeNetwork")
        hotspot (953, 59, 247, 253) action Jump("splunkCorporateNetwork")
        hotspot (69, 379, 391, 204) action Jump("splunkSPL")
        hotspot (76, 624, 553, 309) action Jump("splunkEnterpriseSecurity")
        hotspot (791, 609, 356, 328) action Jump("splunkmltk")
        hotspot (1310, 621, 534, 307) action Jump("splunkSoar")
 

label splunkSoar:
    scene darkcyberbg
    n sensai "We shall teach you the power of SOAR"
    jump splunk

label splunkMLTK:
    scene darkcyberbg
    n sensai "We shall teach you the power of MLTK"
    jump splunk

label splunkSPL:
    scene darkcyberbg
    n sensai "We shall teach you the power of SPL"
    jump splunk

label splunkEnterpriseSecurity:
    scene darkcyberbg
    menu:
        "Welcome to Splunk Enterprise Security.  What would you like to do?"

        "What is Enterprise Security?":
            $ renpy.run(OpenURL('https://youtu.be/-v7hVZpAqrw?si=4R-AH6ICTTGzUOPR'))         
   
        "Watch Youtube Videos on Enterprise Security":
            $ renpy.run(OpenURL('https://youtube.com/playlist?list=PLFF93FRoUwXHM36f_pIHw7pgOmSuV2r21&si=eCPZMxCjYSnPboxQ'))
            

        "How to setup an Enterprise Security Server":
            $ renpy.run(OpenURL('https://youtu.be/Iol1CHyv23A?si=T39u25RFKncG8l03'))   
          

        "How to install Enterprise Security":
            $ renpy.run(OpenURL('https://youtu.be/QdM6JvnYu7g?si=XbRhiK4n4n-pg4Fz'))  
           
       
        "Back to Splunk Menu":
            jump splunk

    #n sensai "Welcome to Enterprise Security Overview"
    #n sensai "This product does a lot of things"
    jump splunkEnterpriseSecurity

screen splunkEnterpriseSecurityOverview:
    modal True


label splunkHelpGuide:
    scene darkcyberbg
    n sensai "So you want to learn about general Splunk"
    n sensai "This is generic information"
    jump splunk 

label splunkHomeNetwork:
    scene darkcyberbg
    n sensai "Home Network you want to set up?"
    jump splunk

label splunkCorporateNetwork:
    scene darkcyberbg
    n sensai "Corporate Network you want to set up?"
    jump splunk



