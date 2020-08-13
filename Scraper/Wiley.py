from bs4 import BeautifulSoup
import webbot
import time
from loutput import louput as lp

class Wileyscraper:
    """
    Wileyscraper
    """

    def __init__(self):
        # Browser
        self.wiley_home = 'https://onlinelibrary.wiley.com'
        self.url = self.wiley_home + '/loi/14680262'

        self.web = webbot.Browser()
        self.web.go_to(self.url)
        # time.sleep(1)

    def scrape(self):
        # crawler
        page = self.web.get_page_source()
        soup = BeautifulSoup(page, "html.parser")
        issues = soup.find_all('div', {'class': 'loi__issue'})

        all_art_this_year = []
        for atag in issues:
            link = self.wiley_home + atag.a["href"]
            self.web.go_to(link)
            # time.sleep(1)
            page_sub = self.web.get_page_source()
            soup_sub = BeautifulSoup(page_sub, "html.parser")
            # articles = soup_sub.find_all('div', {'class': 'content-item-format-links'})
            articles = soup_sub.find_all('a', {'class': 'issue-item__title'})
            articles = articles[2:-4]
            articles_list = []
            for i in articles:
                title = i.text.strip()  # titles
                # print(title)
                link_art = self.wiley_home + i["href"]
                self.web.go_to(link_art)
                page_art = self.web.get_page_source()
                soup_art = BeautifulSoup(page_art, "html.parser")

                authors = soup_art.find_all('a', {'class': 'author-name'})
                if not authors:
                    # pass
                    # print("no authors")
                    authors_text = "no authors"
                else:
                    num_authors = len(authors) * 0.5
                    num_authors = int(num_authors)
                    authors_text = []
                    for a in range(0, (num_authors - 1)):
                        # print(authors[a].text.strip())
                        authors_text.append(authors[a].text.strip())

                abstract = soup_art.find_all('div', {'class': 'article-section__content'})
                if not abstract:
                    # pass
                    # print("no abstract")
                    abstract_text = "no abstract"
                else:
                    abstract_text = abstract[0].text.strip()
                    # print(abstract_text)
                    #
                article_dict = {'title': title, 'authors': authors_text, 'link': link_art, 'abstract': abstract_text}

                articles_list.append(article_dict)

            all_art_this_year.append(articles_list)

        return all_art_this_year




if __name__ == "__main__":
    scraper = Wileyscraper()
    all_art = scraper.scrape()
    lp(all_art) #

    # [[{'title': 'State Capacity, Reciprocity, and the Social Contract', '
    # length  = 4

