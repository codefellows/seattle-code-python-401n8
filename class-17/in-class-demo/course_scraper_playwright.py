from playwright.sync_api import sync_playwright, expect
from bs4 import BeautifulSoup
import time


def main():
    with sync_playwright() as playwright:
        # Open chrome and navigate to my target page
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto("https://testing-www.codefellows.org/course-calendar/")
        # time.sleep(5)

        # Then you do stuff
        # expect(page.get_by_text("200: Foundations")).to_be_visible().click()  # TODO: do it right
        # page.get_by_label("200: Foundations").click()  # Also doesn't work
        page.get_by_text("200: Foundations").nth(2).click()

        # page.click("//label[text() = '200: Foundations']")
        page.click("//label[text() = 'Ops 201']")

        # Now that we have the HTML, bring in bs4
        soup = BeautifulSoup(page.content(), "html.parser")

        calendar_results = soup.find_all("article", class_="calendar-event")

        schedule = "Course Info for Code 201 Classes:\n\n"

        # Iterate through list, pull course info out and concatenate to "schedule"
        for course in calendar_results:
            schedule += course.h1.text + "\n"
            schedule += course.h2.text + "\n\n"

        with open("courses_playwright.txt", "w") as file:
            file.write(schedule)


if __name__ == "__main__":
    main()
