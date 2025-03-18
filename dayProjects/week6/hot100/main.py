from bs4 import BeautifulSoup
import requests

search_date = input("Choose a date (YYYY-MM-DD include dashes) to search up the hottest 100 songs then: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{search_date}", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"})
response.raise_for_status()
website_html = response.text
site = BeautifulSoup(website_html, "html.parser")

titles = [text.getText().replace("\n", "").replace("\t", "") for text in site.select("h3#title-of-a-story.c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021.lrv-u-font-size-16.u-line-height-125.a-truncate-ellipsis.u-max-width-330")]
titles.insert(0, site.select_one("h3.c-title.a-font-primary-bold-l.lrv-u-color-black.lrv-u-margin-r-150").getText().replace("\n", "").replace("\t", ""))
titles = [titles[i] + " - by - " + [text.getText().replace("\n", "").replace("\t", "") for text in site.select("span.c-label.a-no-trucate.a-font-primary-s.u-letter-spacing-0021.lrv-u-display-block.a-truncate-ellipsis-2line")][i] for i in range(len(titles))]
[print(f"{i + 1}: {titles[i]}") for i in range(len(titles))]