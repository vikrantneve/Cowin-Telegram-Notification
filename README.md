# Cowin Telegram and Tweet Notification
This code will send vaccination slot notification for pincode enter by you in your telegram channel and tweet same from your profile. It checks slots every 15 sec and send notification when avaliable. Send message directly in your telegram channel. 

## Installation

Follow all steps :

1. Clone Repo


2. Run command 
```bash
pip3 install -r requirement.txt
```

3. Add your Twitter api credential in code (If you want only telegram you can skip this step)
```bash
#Add your Twitter api Credential here
consumer_key = ''
consumer_secret = ''
key = ''
secret = ''
```

4. Configure Telegram_send. Create BOT from BOTFather and get key. Run command and add your key and channel id.
```bash
telegram-send --configure-channel
```  

5. In pincodes list and your pincodes.
```bash
pincodes = [421301, 421201]
```
6. In URl change District id to your district id. 
```bash
 url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=392&date=" + str(date)
```

7. In txt and msg variable you can change message which you want to send. 

8. Run 
```bash 
python3 cowin.py    
```

## Contributing
Pull requests are welcome. For any changes, please open an issue first to discuss what you would like to change.
