import telegram_send
import time
import requests
import datetime as dt
import tweepy

#Add your Twitter api Credential
consumer_key = '' 
consumer_secret = ''
key = ''
secret = ''

def tweet(msg):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    try:
        api.update_status(msg)
    except:
        msg = msg + "Рађ"
        api.update_status(msg)


def cost_for(vaccine_fees, session_vaccine):
    for vaccine_fee in vaccine_fees:
        if vaccine_fee['vaccine'] == session_vaccine:
            return vaccine_fee['fee']
    return 'Free'


x = 0  # counter

payload = {}
headers = {
    'authority': 'cdn-api.co-vin.in',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'origin': 'https://www.cowin.gov.in',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cowin.gov.in/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
}

#Add pincode for which you want to send notification
pincodes = [421301, 421201]

temp_txt = {}

while True:

    x = x + 1
    print("Run Number " + str(x))

    date = dt.date.today().strftime("%d-%m-%Y")  # Date for the url
    
    # change District id to your dist. 
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=392&date=" + str(
        date)
    response = requests.get(url, headers=headers, data=payload)
    data = response.json()
    centers = data['centers']

    # block of code for region with pincode requirements
    for center in centers:
        # print(center['name'])
        for i in pincodes:
            if center['pincode'] == i:  # filter centers in pincode list
                sessions = center['sessions']
                for session in sessions:
                        if session['available_capacity'] > 0:  # filter sessions with availability
                            # session_id = session['session_id']
                            availability = session['available_capacity']
                            age = session['min_age_limit']
                            center_name = center['name']
                            pincode = center['pincode']
                            fee_type = center['fee_type']
                            vaccine = session['vaccine']
                            date = session['date']
                            slots = session['slots']
                            address = center['address']
                            dose1 = session['available_capacity_dose1']
                            dose2 = session['available_capacity_dose2']

                            txt = "For age: " + str(age) + "+"  "\nCenter: " + str(
                                center_name) + "\nTotal Available Capacity: " + str(availability) + "\nAvailable Capacity Dose 1: " +str(dose1)+  "\nAvailable Capacity Dose 2: " +str(dose2)+ "\nVaccine: " + str(
                                vaccine) + "\nFee Type: " + str(fee_type) + "\nCost: " + cost_for(center['vaccine_fees'], session['vaccine']) + "\nDate: " + str(date) + "\nAddress: " + str(
                                address) + "\nPincode: " + str(
                                pincode) + "\nBook Now: https://selfregistration.cowin.gov.in/ \n\nJai Shree Ram"
                            msg = "For age: " + str(age) + "+"  "\nCenter: " + str(
                                center_name) + "\nAvailable Capacity: " + str(availability) + "\nVaccine: " + str(
                                vaccine) + "\nFee Type: " + str(fee_type) + "\nDate: " + str(date) + "\nAddress: " + str(
                                address) + "\nPincode: " + str(
                                pincode) + "\nBook Now: https://selfregistration.cowin.gov.in/ \n\n#KDMCVaccination #KDMCVaccineNotification"
                            if not temp_txt.get(center_name) == txt:
                                temp_txt[center_name] = txt
                                telegram_send.send(messages=[txt])
                                tweet(msg)
                                print("This is Telegram msg \n", txt)
                                print("This is tweet \n", msg)

    time.sleep(15)
