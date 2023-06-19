from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys
from PIL import Image
symbol=[]
with open('symbol.csv', encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        symbol.append(((row[0])))
    print(symbol)    

driver = webdriver.Firefox()
#symbol=['CANBK','TITAN','IDEA','MANAPPURAM','TATACOMM','DIXON','ICICIPRULI','BEL','INDIACEM','HAL','L&TFH','IDFC','PIIND','ABB','DALBHARAT','SIEMENS','JKCEMENT','SBILIFE','LAURUSLABS','BHARATFORG','AUROPHARMA','CUMMINSIND','ICICIGI','HINDCOPPER','TRENT','CHOLAFIN','NTPC','CROMPTON','RAMCOCEM','MCDOWELL-N','RAIN','M&M','APOLLOHOSP','ZYDUSLIFE','TVSMOTOR','MCX','RECLTD','BRITANNIA','IDFCFIRSTB','CIPLA','ASIANPAINT','TATAMOTORS','INDIAMART','GODREJPROP','BHEL','PFC','INDHOTEL','JSWSTEEL','TORNTPHARM','ABBOTINDIA','ASTRAL','COLPAL','BERGEPAINT','DEEPAKNTR','TATASTEEL','APOLLOTYRE','DABUR','ITC','M&MFIN','BALKRISIND','BAJFINANCE','ULTRACEMCO','ASHOKLEY','NAUKRI','LT','TATACONSUM','AMBUJACEM','EXIDEIND','MUTHOOTFIN','SHREECEM','HDFCLIFE','CANFINHOME','ATUL','IRCTC','NESTLEIND','INDUSTOWER','METROPOLIS','GRASIM','AUBANK','IOC','AXISBANK','PIDILITIND','OBEROIRLTY','RELIANCE','IPCALAB','BATAINDIA','POLYCAB','DIVISLAB','DRREDDY','HINDUNILVR','BAJAJFINSV','MOTHERSON','HAVELLS','BIOCON','GODREJCP','OFSS','LICHSGFIN','COFORGE','RBLBANK','LALPATHLAB','JUBLFOOD','PEL','INTELLECT','HINDALCO','SYNGENE','BPCL','BANKBARODA','PAGEIND','ABCAPITAL','HCLTECH','SUNPHARMA','JINDALSTEL','HINDPETRO','INDIGO','BANDHANBNK','SBICARD','VEDL','POWERGRID','DLF','LTIM','LUPIN','MARUTI','MARICO','NAVINFLUOR','TATAPOWER','DELTACORP','ACC','INDUSINDBK','MRF','BHARTIARTL','AARTIIND','ESCORTS','UBL','HDFCAMC','PETRONET','ONGC','ADANIPORTS','MFSL','GRANULES','PNB','GLENMARK','GAIL','SHRIRAMFIN','UPL','ADANIENT','GNFC','MGL','BOSCHLTD','SRF','ALKEM','CONCOR','SAIL','HEROMOTOCO','BSOFT','NATIONALUM','CUB','COROMANDEL','IGL','HDFCBANK','ABFRL','COALINDIA','CHAMBLFERT','ICICIBANK','LTTS','INFY','BALRAMCHIN','PVRINOX','TATACHEM','NMDC','PERSISTENT','FEDERALBNK','TECHM','SUNTV','HDFC','KOTAKBANK','GUJGASLTD','BAJAJ-AUTO','EICHERMOT','VOLTAS','SBIN','MPHASIS','TCS','IBULHSGFIN','GMRINFRA','WIPRO','IEX','ZEEL']
try:
 for x in symbol:
  try:   
   driver.get("https://www.screener.in/company/"+x+"/consolidated/#chart")
   time.sleep(2)
#driver.find_element_by_name('days')[5].click()
   driver.find_element('xpath','//*[@id="company-chart-days"]/button[7]').click()
   time.sleep(5)
   driver.find_element('xpath','//*[@id="company-chart-metrics"]/button[2]').click()
#driver.find_elements_by_xpath('//*[@id="company-chart-days"]/button[7]').click()
#driver.find_element_by_xpath('//*[@id="company-chart-metrics"]/button[2]').click()
#driver.find_element_by_name('days')[6].click()
   time.sleep(2)
   driver.save_screenshot(x+'.png')
  except:
   continue 
#//*[@id="company-chart-metrics"]/button[2]
except:
    print('end')