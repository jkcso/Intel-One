# Who-Dis

## Synopsis
An open source command line tool that collects and stores Open Source Intelligence about an individual, a target domain or a company.

## Motivation
Implemented in my free time as part of my genuine interest in Cyber Security, especially penetration testing.

## Current version
1. A well documented help menu explaining all the available options with examples.
2. Social media search for individuals and companies using Facebook, Linkedin, Twitter and Instagram.
3. People search engines search using just a name or both a name and a location.
4. Company search using the edgar search engine returning difficult to find and often confidential information about companies.

## Known technical issues
1. Users often overload the IP search allowance they have (when it comes to scripting allowance) because after a while google thinks that you are a web crawler and denies the service returning an error 503.  What I was doing to avoid this was to change my IP address using a VPN.  Another way of doing so is to use proxychains in kali linux and when banned you can do 'service tor restart' to retrieve a new IP address.

## Future versions
1. Aiming on target's mail and if pawned try to retrieve credentials.
2. Advanced google dorks.
3. Who-is data.
4. IP address of target.
5. And many more.

## Disclaimer
This tool should be used in the white hat way, however, I have no responsibility if someone will use for malicious purposes.

## License
I own all the copyrights of this project.  Feel free to contact me and suggestions new features or anything you like.