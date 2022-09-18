from ipynb.fs.full.profile import init,scrap_all
from dotenv import load_dotenv
import os
load_dotenv()

infile = os.getenv('IN_FILE')
url_list = []

with open(infile,"r") as url_fpt:
    url_list = url_fpt.readlines()
url_list = [url.strip() for url in url_list]

driver = init()

for url in url_list:
    try:
    	scrap_all(driver,url)
    except:
        pass

exit(0)
    


