import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import sys
import random
import re
import argparse



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def PollNeighbours(prefix,CaseNum,neighbours=10,processingStr="we received your Form I-765"):
    processingCount=0
    CaseNumIter=CaseNum-int(neighbours/2)

    for i in range(neighbours):
        CaseNumIter+=1
        if(CaseNumIter != CaseNum):
            print(bcolors.OKBLUE+"checking USCIS for Reciept: "+prefix+str(CaseNumIter)+bcolors.ENDC)
            if processingStr in requestStatus(prefix+str(CaseNumIter)):
                processingCount+=1

    print(bcolors.BOLD+str(processingCount)+" out of "+str(neighbours)+" filed around your file date are still pending, don't give up!"+bcolors.ENDC+"\n")
    # print("")
    #changeLocale=&completedActionsCurrentPage=0&upcomingActionsCurrentPage=0&appReceiptNum=YSC1990011345&caseStatusSearchBtn=CHECK+STATUS

def requestStatus(caseID):
    #
    formData={"changeLocale":None,"completedActionsCurrentPage":0,"upcomingActionsCurrentPage":0,"appReceiptNum":caseID,"caseStatusSearchBtn":"CHECK STATUS"}
    response = requests.post('https://egov.uscis.gov/casestatus/mycasestatus.do',data=formData)
    soup=bs(response.content, "html.parser" )
    msg=soup.select("div form div div div div div div.rows.text-center p")[0].get_text()
    #print(bcolors.BOLD++bcolors.ENDC+"\n")
    return msg

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('Reciept Number',
                        help='Your USCIS Reciept Number, starts with 3 letters',
                        default='')
    parser.add_argument('-n', type=int,metavar='N',nargs='?', const=10 ,help='Enable Neighbour Polling, followed by # of neighbour to check, default is 10')

    args = parser.parse_args()
    # print(vars(args)['Reciept Number'])
    # print(args.n)
    #CaseNum=sys.argv[1]#1990011345 - int(neighbours/2) #
    CaseNum=vars(args)['Reciept Number']
    #try:
    match = re.match(r"([a-z|A-Z]+)([0-9]+)", CaseNum, re.I)
    prefix = match.groups()[0]
    CaseNum = int(match.groups()[1])
    print("Case entered:",prefix , CaseNum)
    if(args.n is None):
        msg=requestStatus(prefix+str(CaseNum))
        print(bcolors.OKGREEN+"USCIS Says"+bcolors.ENDC)
        print(bcolors.BOLD+msg+bcolors.ENDC)
    else:
        PollNeighbours(prefix,CaseNum,neighbours=args.n,processingStr="we received your Form I-765")


    # except:
    #     print("ERROR, Case number format incorrect, should start with 3 letters followed by digits")
