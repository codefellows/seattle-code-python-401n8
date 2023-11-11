import requests
from bs4 import BeautifulSoup


url = "https://testing-www.codefellows.org/course-calendar/"
response = requests.get(url)

# print(response.content)
soup = BeautifulSoup(response.content, "html.parser")

calendar_results = soup.find_all("article", class_="calendar-event")

schedule = "Course Info for Code 201 Classes:\n\n"

# Iterate through list, pull course info out and concatenate to "schedule"
for course in calendar_results:
    if "Code 201" in course.h1.text:
        schedule += course.h1.text + "\n"
        schedule += course.h2.text + "\n\n"

# print(schedule)
with open("courses.txt", "w") as file:
    file.write(schedule)
