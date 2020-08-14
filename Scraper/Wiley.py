from bs4 import BeautifulSoup
import pandas as pd
import webbot


# import time
# from loutput import louput as lp

class Wileyscraper:
    """
    Wileyscraper
    """

    def __init__(self):
        # Browser
        self.wiley_home = 'https://onlinelibrary.wiley.com'
        self.econometrica = '/loi/14680262'
        self.JAE = '/loi/10991255'
        self.OBES = '/loi/14680084'
        self.economJ = '/loi/1368423x'
        self.IER = '/loi/14682354'
        self.JMCB = '/loi/15384616'
        self.JEMS = '/loi/15309134'
        self.FinM = '/loi/1755053x'
        self.FinR = '/loi/15406288'
        self.JFin = '/loi/15406261'
        self.JFinR = '/loi/14756803'
        self.JFM = '/loi/10969934'
        self.JRIns = '/loi/15396975'
        self.APPC = '/loi/19113838'
        self.JIFMA = '/loi/1467646x'
        self.JCAF = '/loi/10970053'
        self.IJAudi = '/loi/10991123'
        self.JAccR = '/loi/1475679x'
        self.FiscS = '/loi/14755890'
        self.CAccR = '/loi/19113846'
        self.JBFA = '/loi/14685957'
        self.BioJ = '/loi/15214036'
        self.CAJS = '/loi/1708945x'
        self.JRSSA = '/loi/1467985x'
        self.JRSSB = '/loi/14679868'
        self.JRSSC = '/loi/14679876'

        # self.url = self.wiley_home + '/loi/14680262'
        # self.web = webbot.Browser()
        # self.web.go_to(self.url)
        # time.sleep(1)

    def scrape(self, journal):
        # Browser
        if (journal == "JAE") or (journal == "Journal of Applied Econometrics"):
            my_url = self.wiley_home + self.JAE
        elif (journal == "econometrica") or (journal == "Econometrica"):
            my_url = self.wiley_home + self.econometrica
        elif (journal == 'OBES') or (journal == "Oxford Bulletin of Economics and Statistics"):
            my_url = self.wiley_home + self.OBES
        elif (journal == 'Econom. J.') or (journal == "The Econometrics Journal"):
            my_url = self.wiley_home + self.economJ
        elif (journal == 'IER') or (journal == "International Economic Review"):
            my_url = self.wiley_home + self.IER
        elif (journal == 'JMCB') or (journal == "Journal of Money, Credit and Banking"):
            my_url = self.wiley_home + self.JMCB
        elif (journal == 'JEMS') or (journal == "Journal of Economics & Management Strategy"):
            my_url = self.wiley_home + self.JEMS
        elif (journal == 'FinM') or (journal == "Financial Management"):
            my_url = self.wiley_home + self.FinM
        elif (journal == 'FinR') or (journal == "Financial Review"):
            my_url = self.wiley_home + self.FinR
        elif (journal == 'JFin') or (journal == "The Journal of Finance"):
            my_url = self.wiley_home + self.JFin
        elif (journal == 'JFinR') or (journal == "Journal of Financial Research"):
            my_url = self.wiley_home + self.JEMS
        elif (journal == 'JFM') or (journal == "Journal of Futures Markets"):
            my_url = self.wiley_home + self.JFM
        elif (journal == 'JRIns') or (journal == "Journal of Risk and Insurance"):
            my_url = self.wiley_home + self.JRIns
        elif (journal == 'APPC') or (journal == "Accounting Perspectives"):
            my_url = self.wiley_home + self.APPC
        elif (journal == 'JIFMA') or (journal == "Journal of International Financial Management & Accounting"):
            my_url = self.wiley_home + self.JIFMA
        elif (journal == 'JCAF') or (journal == "Journal of Corporate Accounting & Finance"):
            my_url = self.wiley_home + self.JCAF
        elif (journal == 'IJAudi') or (journal == "International Journal of Auditing"):
            my_url = self.wiley_home + self.IJAudi
        elif (journal == 'JAccR') or (journal == "Journal of Accounting Research"):
            my_url = self.wiley_home + self.JAccR
        elif (journal == 'FiscS') or (journal == "Fiscal Studies"):
            my_url = self.wiley_home + self.FiscS
        elif (journal == 'CAccR') or (journal == "Contemporary Accounting Research"):
            my_url = self.wiley_home + self.CAccR
        elif (journal == 'JBFA') or (journal == "Journal of Business Finance & Accounting"):
            my_url = self.wiley_home + self.JBFA
        elif (journal == 'BioJ') or (journal == "Biometrical Journal"):
            my_url = self.wiley_home + self.BioJ
        elif (journal == 'CAJS') or (journal == "Canadian Journal of Statistics"):
            my_url = self.wiley_home + self.CAJS
        elif (journal == 'JRSSA') or (journal == "Journal of the Royal Statistical Society: A"):
            my_url = self.wiley_home + self.JRSSA
        elif (journal == 'JRSSB') or (journal == "Journal of the Royal Statistical Society: B"):
            my_url = self.wiley_home + self.JRSSB
        elif (journal == 'JRSSC') or (journal == "Journal of the Royal Statistical Society: C"):
            my_url = self.wiley_home + self.JRSSC
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
            # articles = articles[2:-4]

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
                        for a in range(1, num_authors):
                            # print(author_soup[a].text.strip())
                            authors_text = authors_text + blank_str + author_soup[a].text.strip()
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
    Journals = ["econometrica", "JAE", "OBES", "Econom. J.", "IER", "JMBC", "JEMS", "FinM", "FinR", "JFin", "JFinR", "JFM", "JRIns", "APPC", "JIFMA", "JCAF", "IJAudi", "JAccR", "FiscS", "CAccR", "JBFA", "BioJ", "CAJS", "JRSSA", "JRSSB", "JRSSC"]
    for j in Journals:
        df = scraper.scrape(j)
        file_name = j + ".csv"
        df.to_csv(file_name, header=True)
