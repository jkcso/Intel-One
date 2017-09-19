"""
Includes the help page of the program having information about the different flags and options.
Most importantly includes examples of how the different flags are going to be used.  This page
is going to be implemented iteratively i.e when a new feature is implemented this page is updated
to include info about it.
"""


# Prints help into screen.
def help():
    print("""
Please refer to 'Issues' section in GitHub for any problems you may have.
           
-- [ Options for Help & Symbols Explained ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
help                | Prints help on screen                             | who-dis> help              
'|' symbol          | Means 'or'                                        | who-dis> click 1 | 2 means click 1 or 2  
'-' symbol          | Used for the short flag                           | who-dis> john smith -g                   
'--' symbol         | Used for the long flag                            | who-dis> john smith --google             
           
           
-- [ ALL in ONE Options ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-c, --company       | Executes all available searches for companies     | who-dis> glovdi -c | --company       
-d, --domain        | Executes all available searches for domains       | who-dis> glovdi.com -d | --domain
-i, --individual    | Executes all available searches for individuals   | who-dis> john smith -i | --individual
-i and -l           | As above including location of an individual      | who-dis> john smith -i madrid -l
-e, --email         | Performs all possible searches using an email     | who-dis> jsmith@email.com -e | --email

-- Note: The 2 following flags below are executed whenever the above ALL in ONE flags are executed. --  
-sm, --socialMedia  | Executes all available searches in social media   | who-dis> john smith -sm | --socialMedia
-s, --search        | Executes all available searches in search engines | who-dis> glovdi -s | --search

           
-- [ Options for Social Media ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-rts, --rtsearch    | Returns real time social media search results     | who-dis> john smith -rts | --rtsearch  
-fb, --facebook     | Performs facebook search through google           | who-dis> john smith -fb | --facebook     
-ln, --linkedin     | Performs linkedin search through google           | who-dis> john smith -ln | --linkedin     
-tw, --twitter      | Twitter search plus retrieves tweets and analytics| who-dis> john smith -tw | --twitter      
-in, --instagram    | Performs instagram search, posts and analytics    | who-dis> john smith -in | --instagram
-pn, --pinterest    | Performs pinterest search through google          | who-dis> john smith -pn | --pinterest
-yt, --youtube      | Performs search in youtube for username           | who-dis> john smith -yt | --youtube
-tb, --tumblr       | Performs tumblr search through google             | who-dis> john smith -tb | --tumblr    
-re, --redit        | Performs reddit search and posts search           | who-dis> john smith -re | --reddit
-ure, --userReddit  | Provides insights and statistics on reddit user   | who-dis> john smith -ure | --userReddit
-bl, --blogs        | Searches in blogs about target keyword            | who-dis> john smith -bl | --blogs  
-cd ,--code         | Performs github & 'nerdy data' search on repos    | who-dis> setoolkit -cd | --code
           
           
-- [ Options for Search Engines ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-g, --google        | Performs normal google search                     | who-dis> john smith -g | --google      
-ddg, --ddGo        | Performs search in duck duck go search engine     | who-dis> john smith -ddg | --ddGo
-bd, --baidu        | Performs search in chinese engine baidu           | who-dis> john smith -bd | --baidu
-bg, --bing         | Performs search in bing search engine             | who-dis> john smith -bg | --bing
-qw, --qwant        | Performs search in qwant search engine            | who-dis> john smith -qw | --qwant
-cl, --cluster      | Performs clustering search for query              | who-dis> john smith -cl | --cluster 
-ex, --exciteNews   | Performs search about recent news on search engine| who-dis> john smith -ex | --exciteNews
-oa, --oldArticles  | Performs search about very old posts about query  | who-dis> john smith -oa | --oldArticles
-ev, --emailValid   | Performs email validity search for target mail    | who-dis> jsmith@email.com -ev | --emailValid


-- [ Options for People Search Engines ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================      
-p, --people        | Provides links on multiple people search engines  | who-dis> john smith -p | --people          
-p and -l           | Performs specific pipl using with location        | who-dis> john smith -p madrid -l         
           
           
-- [ Options for Companies ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================       
-cs, --compSearch   | Performs search in multiple companies websites    | who-dis> glovdi -cs | compSearch             
-are, --reports     | Provides 2 links with annual reports of companies | who-dis> glovdi -are | --reports
-cef, --emailFormat | Returns the email format of the company searched  | who-dis> glovdi -cef | --emailFormat
           
                      
-- [ Options for Domains ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-wh, --whois        | Performs whois search in the target domain        | who-dis> glovdi.com -wh | --whois
-dns, --dnsLookup   | Performs a DNS lookup about target domain         | who-dis> glovdi.com -dns | --dnsLookup     
-sc, --scan         | Performs a vulnerability scan using asafaweb site | who-dis> glovdi.com -sc | --scan
-ar, --archive      | Performs search for past versions of website      | who-dis> glovdi.com -ar | --arch
-rb, --robots       | Provides the link including the robots.txt file   | who-dis> glovdi.com -rb | --robots     
           
           
-- [ Other Options ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-sh, --shodan       | Performs shodan search for given keyword          | who-dis> zanussi -sh | --shodan          

""")
