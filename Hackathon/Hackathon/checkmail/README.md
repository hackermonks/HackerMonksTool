
**Goa Police Hackathon.**

You give Checkmail an email then it does two simple useful jobs with it:
- Search for public leaks for the email and returns the result with the most useful details about the leak (Using haveibeenpwned API) and tries to get the plain text passwords from leaks it find.
- Now you give it a password or a leaked password then it tries this credentials against some well-known websites (ex: Facebook, Twitter, Google...), tells if the login successful and if there's captcha some where blocking our way!

### Some of the scenarios checkmail can be used in it
- Check if the targeted email is in any leaks and then use the leaked password to check it against the websites.
- Check if the target credentials you found is reused on other websites/services.
- Checking if the old password you got from the target/leaks is still used in any website.



# Usage
```
usage: checkmail.py [-h] [-p] [-np] [-q] email

positional arguments:
  email       Email/username to check

optional arguments:
  -h, --help  show this help message and exit
  -p          Don't check for leaks or plain text passwords.
  -np         Don't check for plain text passwords.
  -q          Quiet mode (no banner).

```

## Installing and requirements
### To make the tool work at its best you must have :
- Python 3.x or 2.x (preferred 3).
- Linux or Windows system.
- Worked on some machines with MacOS and python3.
- The requirements mentioned in the next few lines.

```

