label inventory_info:

    n sensai "Welcome to the world of Splunk"
    n sensai "You may be wondering what Splunk is, or you may already have a knowledge of the tool and would better like to learn how to use the tool"
    n sensai "I will provide you an overview of the technology,"
    n sensai "minimum information to set it up in a home lab, "    
    n sensai "instructions on how to set up a more complicated network"
    n sensai "instructions on how to do day to day searches"
    
    scene networkinventory
    call screen network_inventory

screen network_inventory:
    modal True

