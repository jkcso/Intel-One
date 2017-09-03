# Who-Dis

## Synopsis
An open source command line tool that collects and stores Open Source Intelligence about an individual, a target domain or a company.

## Motivation
Implemented in my free time as part of my genuine interest in Cyber Security, especially penetration testing.

## Current version
- A well documented help menu explaining all the available options with examples.
- Social media search for individuals and companies using Facebook, Linkedin, Twitter and Instagram.
- People search engines search using just a name or both a name and a location.
- Company search using the edgar search engine returning difficult to find and often confidential information about companies.

## Known technical issues
- Users often overload the IP search allowance they have (when it comes to scripting allowance) because after a while google thinks that you are a web crawler and denies the service returning an error 503.  What I was doing to avoid this was to change my IP address using a VPN.  Another way of doing so is to use proxychains in kali linux and when banned you can do 'service tor restart' to retrieve a new IP address.

## Future versions
- Aiming on target's mail and if pawned try to retrieve credentials.
- Advanced google dorks.
- Who-is data.
- IP address of target.
- And many more.

## Disclaimer
This tool should be used in the white hat way, however, I have no responsibility if someone will use for malicious purposes.

## License
I own all the copyrights of this project.  Feel free to contact me and suggestions new features or anything you like.