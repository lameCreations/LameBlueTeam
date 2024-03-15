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
        hotspot (1300, 202, 3, 0) action OpenURL("https://www.youtube.com/playlist?list=PLFF93FRoUwXHja1s9gEBK01st8bmgGz0t")
        hotspot (619, 55, 267, 258) action Jump("splunk")
        hotspot (117, 85, 427, 164) action Jump("pfsense")
        hotspot (69, 379, 391, 204) action Jump("sysmon")
        hotspot (503, 354, 315, 252) action Jump("zeek")
        hotspot (947, 344, 297, 317) action Jump("vmware")
        hotspot (1284, 314, 618, 369) action Jump("hyperv")
        hotspot (1101, 707, 664, 261) action Jump("criblstream")
        hotspot (481, 737, 595, 242) action Jump("securityonion")
        hotspot (94, 674, 360, 365) action Jump("gravwell")