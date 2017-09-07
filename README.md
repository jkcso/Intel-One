# Who-Dis

## Synopsis
An open source command line tool that collects and stores Open Source Intelligence about an individual, a target domain or a company.

## Motivation
Implemented in my free time as part of my genuine interest in Cyber Security, especially penetration testing.

## Current version
### Constantly improving user experience
- A well documented help menu explaining all the available options with examples.

### Targeting individuals
- Social media search matching the provided keyword in recent posts from all social media.
- Specific social media search using Facebook, Linkedin, Twitter, Instagram and Reddit.
- People search engines using just a name or both a name and a location.
- Get insights on lifetime reddit user activity by providing a username.

### Targeting companies
- Same social media search as above when applicable.
- Company search using the edgar search engine returning difficult to find and often confidential information about companies.

### Targeting domains
- Whois lookup.
- Web vulnerability scan.

### Other features
- Shodan.io search.

## Directories explained
### search
- companies.py: Includes functions able to target companies such as the edgar search.
- domains.py: Includes functions to retrieve domain info such as whois lookup and a vulnerability scanner.
- engines.py: Includes search engines such as google and people search engines such as pipl.
- other.py: Includes non directly related to OSINT functionality such as shodan search.
- socialMedia.py: Includes social media search and posts gathering in various ways.
- utilities.py: Includes functions that help in all other classes.

### tests
- Clear, concise and extensive tests for each of the above class and function.

### help
- Explains with a description and an example each available function.

### intro
- Contains the welcome screen of the tool.

### main
- The main thread of the program responsible for running it.

## Future versions
- Aiming on target's mail and if pawned try to retrieve credentials.
- Advanced google dorks.
- IP address of target.
- And many more.

## Disclaimer
This tool should be used in the white hat way, however, I have no responsibility if someone will use for malicious purposes.

## License
I own all the copyrights of this project.  Feel free to contact me and suggestions new features or anything you like.