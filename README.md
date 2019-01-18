# checkUSCIS
A quick Python script that checks your case status for your USCIS case

If you are like me who have been anxiously waiting to hear back from USCIS about a form you've submitted, and is tired of checking on their website every hour, worry no more! Use this handy little script to check your status from commandline. If you'd like, borrow the few lines of code and have it send yourself daily test reminders, etc... 

Happy hacking!

### Neighbour Polling
It's useful to check the status of your adjacent reciept numbers to get a general idea of how your application is moving compared to others. use the -n argument to enable it, pass it a integer to specify how many neighbours you want to check.

## External Dependencies
BeautifulSoup 4

## Usage
python3 checkUSCISstats.py -h
usage: checkUSCISstats.py [-h] [-n [N]] Reciept Number

Process some integers.

positional arguments:
  Reciept Number  Your USCIS Reciept Number, starts with 3 letters

optional arguments:
  -h, --help      show this help message and exit
  -n [N]          Enable Neighbour Polling, followed by # of neighbour to
                  check, default is 10


## Example 
<<<< python3 checkUSCIS.py YSC1xxxxx1336

>>>> checking USCIS for Reciept: YSC1xxxxx1336

>>>> On January x, 2019, the Post Office delivered your new card for Receipt Number YSC1xxxxx1336, to the address that you gave us.  The tracking number assigned is 9205590153xxxxxxxxx.  You can use your tracking number at www.USPS.com in the Quick Tools Tracking section.  If you move, go to www.uscis.gov/addresschange to give us your new mailing address.

<<<< python3 checkUSCISstats.py YSC1xxxxx1345 -n 20
>>>> Case entered: YSC 1xxxxx1345
>>>> checking USCIS for Reciept: YSC1xxxxx1336
>>>> checking USCIS for Reciept: YSC1xxxxx1337
>>>> checking USCIS for Reciept: YSC1xxxxx1338
>>>> checking USCIS for Reciept: YSC1xxxxx1339
>>>> checking USCIS for Reciept: YSC1xxxxx1340
>>>> checking USCIS for Reciept: YSC1xxxxx1341
>>>> checking USCIS for Reciept: YSC1xxxxx1342
>>>> checking USCIS for Reciept: YSC1xxxxx1343
>>>> checking USCIS for Reciept: YSC1xxxxx1344
>>>> checking USCIS for Reciept: YSC1xxxxx1346
>>>> checking USCIS for Reciept: YSC1xxxxx1347
>>>> checking USCIS for Reciept: YSC1xxxxx1348
>>>> checking USCIS for Reciept: YSC1xxxxx1349
>>>> checking USCIS for Reciept: YSC1xxxxx1350
>>>> checking USCIS for Reciept: YSC1xxxxx1351
>>>> checking USCIS for Reciept: YSC1xxxxx1352
>>>> checking USCIS for Reciept: YSC1xxxxx1353
>>>> checking USCIS for Reciept: YSC1xxxxx1354
>>>> checking USCIS for Reciept: YSC1xxxxx1355
>>>> 3 out of 20 filed around your file date are still pending, don't give up!
