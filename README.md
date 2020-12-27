# AIMS-Grades-Script

**Exculsively for IIIT Raichur students

** Can be used for other institute AIMS portal too. Change the url for that. (Eg. IITH, IIIT Dharwad [Didn't tried it though])

By running this script you don't have to check for your grades again and again on the institute AIMS portal.

## How to use

Install python requirements.

### Get cookie value

Login into AIMS portal and pull out the cookie **value** using your browser's Dev Tools.
![Chrome Example](assets/cookie.png)

### Setting required fields

Set the following fields in the script. (Comments are written after these variables)

```
email
password
from
to
```

### Running the script

Run the script using Python v3.

`python3 script.py`

Enter cookie **value** and academic period id. (Generally it's the semester number but for 3rd sem it is 4, don't know why)

![](assets/starting.png)

The script will start and will send an email when any of the course grades are changed

Output:
```
[2020-12-27 02:10:52.410499] 1/7 courses till now. Trying again in 10 mins.....
[2020-12-27 02:20:52.837820] 1/7 courses till now. Trying again in 10 mins.....
[2020-12-27 02:30:53.194651] 1/7 courses till now. Trying again in 10 mins.....
Successfully sent email.
[2020-12-27 02:40:53.594826] 3/7 courses till now. Trying again in 10 mins.....
.
.
.
.
.


```

Wait for the email.......

## Extras

You can change the interval accordingly in the script.

Run this in background during result time and enjoy......... (Oh wait how can you enjoy)


<br>
<br>
<br>
Bye bye.....
