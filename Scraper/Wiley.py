from bs4 import BeautifulSoup
import pandas as pd
import webbot
import time
#from loutput import louput as lp

class Wileyscraper:
    """
    Wileyscraper
    """

    def __init__(self):
        # Browser
        self.wiley_home = 'https://onlinelibrary.wiley.com'
        self.econometrica = '/loi/14680262'
        self.JAE = '/loi/10991255'

        #self.url = self.wiley_home + '/loi/14680262'
        #self.web = webbot.Browser()
        #self.web.go_to(self.url)
        # time.sleep(1)

    def scrape(self, journal):
        # Browser
        if (journal == "JAE") or (journal == "Journal of Econometrics"):
            my_url = self.wiley_home + self.JAE
        elif (journal == "econometrica") or (journal == "Econometrica"):
            my_url = self.wiley_home + self.econometrica
        else:
            raise ValueError("No such a Journal!")

        self.web = webbot.Browser()
        self.web.go_to(my_url)

        # crawler
        page = self.web.get_page_source()
        soup = BeautifulSoup(page, "html.parser")
        issues = soup.find_all('div', {'class': 'loi__issue'})

        titles = []
        authors = []
        links = []
        abstract = []
        for atag in issues:
            link = self.wiley_home + atag.a["href"]
            self.web.go_to(link)
            # time.sleep(1)
            page_sub = self.web.get_page_source()
            soup_sub = BeautifulSoup(page_sub, "html.parser")
            # articles = soup_sub.find_all('div', {'class': 'content-item-format-links'})
            articles = soup_sub.find_all('a', {'class': 'issue-item__title'})
            #articles = articles[2:-4]

            for i in articles:
                title_text = i.text.strip()  # titles
                titles.append(title_text)
                # print(title)
                link_art = self.wiley_home + i["href"]
                links.append(link_art)
                self.web.go_to(link_art)
                page_art = self.web.get_page_source()
                soup_art = BeautifulSoup(page_art, "html.parser")

                author_soup = soup_art.find_all('a', {'class': 'author-name'})
                if not author_soup:
                    # pass
                    # print("no author")
                    authors_text = "no author"
                else:
                    num_authors = len(author_soup) * 0.5
                    num_authors = int(num_authors)
                    authors_text = author_soup[0].text.strip()
                    if num_authors == 1:
                        pass
                    else:
                        blank_str = ", "
                        for a in range(1, (num_authors - 1)):
                            # print(author_soup[a].text.strip())
                            authors_text = authors_text +  blank_str + author_soup[a].text.strip()
                authors.append(authors_text)

                abstract_soup = soup_art.find_all('div', {'class': 'article-section__content'})
                if not abstract_soup:
                    # pass
                    # print("no abstract")
                    abstract_text = "no abstract"
                else:
                    abstract_text = abstract_soup[0].text.strip()
                    # print(abstract_text)
                abstract.append(abstract_text)

        article_dict = {'title': titles, 'author': authors, 'link': links, 'abstract': abstract}
        all_article_df = pd.DataFrame(article_dict)

        return all_article_df




if __name__ == "__main__":
    scraper = Wileyscraper()
    Journals = ["econometrica"]
    df = scraper.scrape("econometrica")
    df.to_csv("output.csv", header=True)

