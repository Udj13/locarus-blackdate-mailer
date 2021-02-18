import requests
from requests.auth import HTTPBasicAuth
import datetime
import smtplib

emails_list = ["111@gmail.com", "222@gmail.com"]

my_email = "email"
mail_password = "password"

main_user = "user"
main_pwd = "password"
urlGet = "http://server:8091/do.admin?q=cs"


def locarus_request(url, user, pwd):
    response = requests.get(url, auth=HTTPBasicAuth(user, pwd))
    if not response:
        return ''
    return response.json()


r_json = locarus_request(urlGet, main_user, main_pwd)

day_of_check = str(datetime.date.today() + datetime.timedelta(days=5))

black_date_devices = []
license_black_date_devices = []

for client in r_json['result']:
    if client['inn'] != '':
        for device in client['devices']:
            if device['blackDate'].split('T')[0] == day_of_check:
                black_date_devices.append(f" {device['imei']},  {client['lastName']} (ИНН: {client['inn']}, email: {client['email']}), {device['type']},  {device['number']}, {device['model']}\n")
            if device['licenseBlackDate'].split('T')[0] == day_of_check:
                license_black_date_devices.append(f" {device['imei']},  {client['lastName']} (ИНН: {client['inn']}, email: {client['email']}), {device['type']},  {device['number']}, {device['model']}\n")

email_message = ""

if black_date_devices != []:
    email_message = f"С {day_of_check} в черном списке:\n"
    for device in black_date_devices:
        email_message += device

if license_black_date_devices != []:
    email_message += f"\n{day_of_check} заканчивается лицензия:\n"
    for device in license_black_date_devices:
        email_message += device



if email_message != "":
    with smtplib.SMTP("mail.tahovolga.ru") as connection:
        connection.starttls()
        connection.login(user=my_email, password=mail_password)
        for email in emails_list:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Блокировки локарусов\n\n{email_message}".encode('utf-8')
            )