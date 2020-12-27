import requests
import time
import smtplib, datetime
from email.message import EmailMessage

print("This is a script to send an notification through email for result updates.")
print("Wait and watch")
print("--------------------------------------------------------------------------")
print("Make sure you provide the cookie and courseId while running\n\n")


msg = EmailMessage()

mapper = {
	"A+": 10, "A": 10, "A-": 9, "B": 8, "B-": 7, "C": 6, "C-": 5, "D": 4, "S": 0
}

email = ""				#Update this with sender's email address
password = ""			#Update this with corresponding email address's password

#Change URL if another institute (Not IIITR or URL is changed)
url = 'https://aims.iiitr.ac.in/iiitraichur/courseReg/loadMyCoursesHistroy?studentId=0&courseCd=&courseName=&orderBy=1&degreeIds=&acadPeriodIds=&regTypeIds=&gradeIds=&resultIds=&isGradeIds='
token = str(input("Cookie value: "))
cookie = {'JSESSIONID' : token}
academicPeriod = int(input("Academic Period ID: "))

def sendEmail(r, cgpa, totalCredit):
	try:
		with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

			smtp.login(email, password)

			gradeData = ""

			for course in r:
				if course["acadPeriodId"] == academicPeriod:
					gradeData += f'{course["courseName"]} : {course["gradeDesc"]}\n'
				

			msg["subject"] = "Semester Grades Uploaded"
			msg["To"] = ""									# Update this with sender's address
			msg["From"] = ""								# Update this with reciever(s) address(es)
			msg.set_content("Semester Result\n\nYour CGPA till now for the semester is " + str(cgpa/totalCredit) + ". Below is a breakdown of grades. Have a nice day.\n\n" + gradeData)

			smtp.send_message(msg)
			print("Successfully sent email.")
	except Exception:
		print("Error: unable to send email")



def gradeChecker(tillNow):

	r = requests.get(url, cookies=cookie).json()

	courseCount = 0
	currentCount = 0
	cgpa = 0
	totalCredit = 0


	for course in r:
		if course["acadPeriodId"] == academicPeriod:
			courseCount += 1
			if course["gradeDesc"] != "":
				totalCredit += int(float(course["credits"]))
				currentCount += 1
				cgpa += (mapper[course["gradeDesc"]] * int(float(course["credits"])))
	

	if(tillNow != currentCount):
		sendEmail(r, cgpa, totalCredit)
		tillNow = currentCount
	if(courseCount != currentCount):
		print(f'[{datetime.datetime.now()}] {currentCount}/{courseCount} courses till now. Trying again in an hour.....')
		time.sleep(600)
		gradeChecker(tillNow)
	else:
		print("--------------------------------------------------------------------------")
		print("Script complete........\t\t\t\t Bye Bye")
		print("--------------------------------------------------------------------------")


gradeChecker(0)
