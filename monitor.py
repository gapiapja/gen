import requests
from requests import exceptions as  req_exc
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import logging
#from keep import keep_alive
from time import sleep, time, strftime

#keep_alive()

def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    data = "Current Time = " + current_time
    return data
    
format_string = '%(levelname)s: %(asctime)s: %(message)s'
logging.basicConfig(level=logging.INFO, filename="platform_script.log", format=format_string)

def telegram_bot_sendtext(bot_message):
 bot_token = '6466982936:AAHPbxxelVAmCc9C1fNNtg7aB8hmWtyPf-M'
 bot_chatID = '1903595159'
 send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
 response = requests.get(send_text)
 return response.json()

def main():
 for url in ['https://ab6709f0-9367-49fe-9ede-cf2fb3ede96d-00-2c1vjoq8t7qfr.spock.replit.dev/']:
     try:
         response = requests.get(url, verify=False)
         response.raise_for_status()
         # if response are successful , no exception is raised
     except req_exc.HTTPError as http_error:
         print(f'HTTP error occurred: {http_error}')
         error_message = "GAPIAPJA SYSTEM❗❗\nStatus Bot: {} Mati: {}.".format(url, http_error)
         telegram_bot_sendtext(str(error_message))
         logging.error(str(error_message))
     except req_exc.ConnectionError as connection_error:
         print(f'Connection error occured: {connection_error}')
         error_message = "Checked URL: {} has an issue: {}.".format(url, connection_error)
         telegram_bot_sendtext(str(error_message))
         logging.error(str(error_message))
 else:
         print("Success!")
         telegram_bot_sendtext("Link is UP and accessible..")
      #   logging.info("ALL link accessible")
         
#main()
u = 2
while True:
   # main()
    sleep(30)
    main()
    