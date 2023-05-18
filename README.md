# **Time Discord Bot**

### **Created by:**
JeSuisBaguette

##  **Project Description:**

This is a discord bot which, upon receiving commands, sends a channel text message with time zone information and can also help convert between time-zones at a future date.  

## **File Structure:**

### **Bot.py:**

Contains code that interacts with the Discord API. Houses all functions and decorators necessary to make the bot run in context of Discord.

### **Time_API.py:**

Contains code that queries the API containing all the data parsed and sent through the bot. All data presented is accessed from the [Time API](https://timeapi.io/#). 

### **Requirements.txt:**

Contains the pip-installable libraries and their respective versions used in the project which are required for it to run.

## **Documentation:**

### **Decorators:**

Contrary to my previous Discord Bot, this bot does not subclass but instead uses decorators/annotations to modify the functionality of the Discord API. The reason for the switch was for me to gain practice and exposure to both in case of working on a larger project in the future.

### **Functions:**

Queries to the [Time API](https://timeapi.io/#) is handled through the use of functions in the time_API.py file. A brief rundown of the purposes of the functions are provided below:

**get_time():** 

Upon receiving an IANA formatted time-zone, returns the location, date, and time of that time-zone. 

**convert_time():**

This function takes three parameters. The time zone it is converting from, the time zone it is converting to, and the time by which to increment that conversion, which is zero by default. When called, the function will return the time of the location converted from the initial location with apprpriate incrementation (if any). 

**get_help():**

This is a non-API related help function housed in the bot.py file that returns a text stating the way to call the aforementioned functions through commands on Discord, and the specific parameters (if any) which they accept. 

## **Remarks:**

You are free to use the code as you'd like. If you are as tired as I am of having to convert between time-zones for planning activities, this bot may be of some use in alleviating that. Special thanks to [Time API](https://timeapi.io/#) for their free API access and super simple and easy-to-understand documentation. 
