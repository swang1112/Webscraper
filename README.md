# Journal Scraper
 Simple python webcrawler for finding journal articles issued in the current year. 
 
 If you are interested in finding information of articles from a specific journal,
 just parse the name (i.e. string) of the journal (see below) to the variable `target_journal` 
 in the file `main.py`, for example `target_journal = "International Economic Review"`. 
 Running the file `main.py` would collect the `title`, `authors`, `link` and `abstract` of all 
 articles from the journal published in the current year produce in a `.csv` file.
 
 If you want to collect all journals produced by a certain publisher, which will take a while,
 just go into the `Scraper` folder, find the name of that publisher and directly run that script,
 for example `Wiley.py` for Wiley & Sons.
 
Because all `html` source codes are acquired using `webbot`, it only works if you have 
installed Chrome on your maschine. If you intend to run the code on a remote maschine
e.g., server, running the code in the `screen` mode in recommended.
 
## Supported Journals
26 journals of Wiley & Sons are supported so far (not fully tested, bug reports are welcome!)
- Journal of Applied Econometrics (JAE)
- Econometrica
- Oxford Bulletin of Economics and Statistics (OBES)
- The Econometrics Journal (Econom. J.)
- International Economic Review (IER)
- Journal of Money, Credit and Banking (JMCB)
- Journal of Economics & Management Strategy (JEMS)
- Journal of Business Finance & Accounting (JBFA)
- Biometrical Journal (BioJ)
- Canadian Journal of Statistics (CAJS)
- Journal of the Royal Statistical Society: A (JRSSA)
- Journal of the Royal Statistical Society: B (JRSSB)
- Journal of the Royal Statistical Society: C (JRSSC)
- Financial Management (FinM)
- Financial Review (FinR)
- The Journal of Finance (JFin)
- Journal of Financial Research (JFinR)
- Journal of Futures Markets (JFM)
- Journal of Risk and Insurance (JRIns)
- Accounting Perspectives (APPC)
- Journal of International Financial Management & Accounting (JIFMA)
- Journal of Corporate Accounting & Finance (JCAF)
- International Journal of Auditing (IJAudi)
- Journal of Accounting Research (JAccR)
- Fiscal Studies (FiscS)
- Contemporary Accounting Research (CAccR)

More journals from Wiley and other publishers will be included in the upcoming future.
There will also be some search functions, which allow users to identify the articles of their interest.


 
