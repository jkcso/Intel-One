"""
Includes the help page of the program having information about the different flags and options.
Most importantly includes examples of how the different flags are going to be used.  This page
is going to be implemented iteratively i.e when a new feature is implemented this page is updated
to include info about it.
"""


# prints help into screen.
def help():
    print("""
Please refer to 'Issues' section in GitHub for any problems you may have.
           
-- [ Options for Help & Symbols Meaning ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =========================================
help                | Prints help on screen                             | who-dis> help              
'|' symbol          | Means 'or'                                        | who-dis> click 1 | 2 means click 1 or 2  
'-' symbol          | Used for the short flag                           | who-dis> john smith -g                   
'--' symbol         | Used for the long flag                            | who-dis> john smith --google             
           
           
-- [ Options for Individuals @ Social Media ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =========================================
-ss, --social       | Returns posts from all social media about target  | who-dis> john smith -ss | --social       
-fb, --facebook     | Performs facebook search through google           | who-dis> john smith -fb | --facebook     
-ln, --linkedin     | Performs linkedin search through google           | who-dis> john smith -ln | --linkedin     
-tw, --twitter      | Performs twitter search through google            | who-dis> john smith -tw | --twitter      
-in, --instagram    | Performs instagram search through google          | who-dis> john smith -in | --instagram    
-re, --redit        | Performs reddit search through google             | who-dis> john smith -re | --reddit       
           
           
-- [ Options for Individuals @ (People/Username) Search Engines ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =========================================
-g, --google        | Performs normal google search                     | who-dis> john smith -g | --google        
-p, --pipl          | Provided a link to pipl search engine             | who-dis> john smith -p | --pipl          
-p and -l           | Performs specific pipl using with location        | who-dis> john smith -p madrid -l         
-ure, --userReddit  | Provides insights and statistics on reddit user   | who-dis> john smith -ure | --userReddit  
           
           
-- [ Options for Companies @ Search Engines] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =========================================
-g, --google        | Performs normal google search                     | who-dis> glovdi -g | --google            
-ed, --edgar        | Performs search using edgar company search engine | who-dis> glovdi -ed | --edgar
-cw, --corpWiki     | Provides a link in the wikipedia of corporations  | who-dis> glovdi -cw | --corpWiki             
-ar, --reports      | Provides 2 links with annual reports of companies | who-dis> glovdi -ar | --reports
           
       
-- [ Options for Companies @ Social Media] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =========================================
-ss, --social       | Returns posts from all social media about target  | who-dis> glovdi -ss | --social       
-fb, --facebook     | Performs facebook search through google           | who-dis> glovdi -fb | --facebook         
-ln, --linkedin     | Performs linkedin search through google           | who-dis> glovdi -ln | --linkedin         
-tw, --twitter      | Performs twitter search through google            | who-dis> glovdi -tw | --twitter          
-in, --instagram    | Performs instagram search through google          | who-dis> glovdi -in | --instagram        
           
           
-- [ Options for Domains ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =========================================
-wh, --whois        | Performs whois search in the target domain        | who-dis> glovdi.com -wh | --whois     
-sc, --scan         | Performs a vulnerability scan using asafaweb site | who-dis> glovdi.com -sc | --scan     
           
           
-- [ Other Options ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =========================================
-sh, --shodan       | Performs shodan search for given keyword          | who-dis> zanussi -sh | --shodan          
""")
