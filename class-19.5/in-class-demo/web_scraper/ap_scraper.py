from bs4 import BeautifulSoup
import requests


def news_scraper(topic):
    # Scrape the top link
    response = requests.get(f"https://apnews.com/search?q={topic}")
    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find("div", class_="SearchResultsModule-results")
    pagelist_items = search_results.find_all("div", class_="PageList-items-item")  # switched from .find() to find_all() to handle videos

    # Find the first non-video link in the pagelist_items
    for item in pagelist_items:
        a_tag = item.find("a")
        url = a_tag["href"]

        if url.startswith("https://apnews.com/article/"):
            break

    print(url)

    # Scrape the news story
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    story_body = soup.find("div", class_="RichTextStoryBody")
    story_p_elements = story_body.find_all("p")

    # Build a string
    story = ""

    for elem in story_p_elements:
        story += elem.get_text()
        story += "\n\n"

    return url, story


if __name__ == "__main__":
    print(news_scraper("washington"))
    print("\n\nDone scraping!")
