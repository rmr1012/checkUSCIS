import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

CaseNum=sys.argv[1]
print(bcolors.OKBLUE+"checking USCIS for Reciept: "+CaseNum+bcolors.ENDC)
print("")
formData={"changeLocale":None,"completedActionsCurrentPage":0,"upcomingActionsCurrentPage":0,"appReceiptNum":CaseNum,"caseStatusSearchBtn":"CHECK STATUS"}
#changeLocale=&completedActionsCurrentPage=0&upcomingActionsCurrentPage=0&appReceiptNum=YSC1990011345&caseStatusSearchBtn=CHECK+STATUS
response = requests.post('https://egov.uscis.gov/casestatus/mycasestatus.do',data=formData)
soup=bs(response.content, "html.parser" )
msg=soup.select("div form div div div div div div.rows.text-center p")
print(bcolors.BOLD+msg[0].get_text()+bcolors.ENDC+"\n")
