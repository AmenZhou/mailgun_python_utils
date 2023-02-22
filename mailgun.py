import requests
from dotenv import load_dotenv
import os

if os.environ.get("ENV") == "production":
    load_dotenv()
else:
    load_dotenv(".env.development.local")

url = os.getenv('URL')
api_key = os.getenv('API_KEY')

params={
  'from': os.getenv('FROM'),
  'to': os.getenv('TO'),
  'subject': 'Hello',
  'text': 'Testing some Mailgun awesomeness!'
}

with open('./attachment1.txt', 'rb') as f:
    attachment = f.read()

files = [('attachment', ('attachment1.txt', attachment))]

response = requests.post(url, auth=('api', api_key), data=params, files=files)

if response.status_code == 200:
  print('An email has been sent successfully')
else:
  print('Fail! - An email has NOT been sent successfully')
  print(response.text)


