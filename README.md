# Introduction 

This is a project I built with the sole intent to learn more about scraping websites, manipulating data, and delivering it through a medium. It is not intended for commercial use.

The program tracks an entire eBay search page of a particular item and sends automated updates to an email with the respective link and price to each entry.

The program asks you for:
  - The item you want to track
  - How many hours do you want between updates
  - The range of price
  - The email address you would like to receive the updates to

![This is what you input to the program](https://prnt.sc/26dvn1w)

![This is how the email you receive looks like](https://prnt.sc/26dvsly)

## Installation

The program only works locally. It will create a CSV file in the current directory the program is run from with all the data. 

If you would like to test the program, you need to:

```
pip install eBay_email_tracker
```
```
from ebay_email_tracker import tracker
```
```
tracker()
```

The program will only work for a Gmail account. You have to authorize access to less secure apps in your Gmail settings.

I recommend setting a new password for this. You can do that in "app passwords". You will need to have 2-Factor authorization in your Gmail, and it allows any login attempt with the correct credentials to connect without requiring 2-Factor authorization.

Set environmental variables in your Windows Operating System: (Control Panel -> View advanced system settings -> Environment Variables -> User variables for...)

|                |Variable                        |Value                       |
|----------------|-------------------------------|-----------------------------|
||EBAY_TRACKER_EMAIL          |An email you want to send the information from        |
| |EBAY_TRACKER_PASSWORD            |Password to that email (app passwords preferably)         |

The program depends on these packages:
  - Numpy
  - BeautifulSoup
  - lxml
  - requests
  - Pandas
 
 ## Improvements:

- I realized that the program will often send entries that are no longer available. While the program sleeps, I could check each entry that was not seen in the most recent search, and see if it has its price listed. If not, delete it from the data.
- Currently, the only way to close the program would be to interrupt it and close it. I could implement a way for the user to close the program if he or she desires to.
- While the program is running, there is nothing telling the user that it is working apart from the first email sent. The program will stay the same for the whole duration. I could print statements to the user, so he knows the program is working as intended.
- The program only works locally. I could implement a database that tracks the item of different users, and sends that information without storing each entry locally, but that would be a completely different project.
