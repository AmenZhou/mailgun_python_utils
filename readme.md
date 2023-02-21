# MailGun Python Util

### An example of send email API via curl in Mailgun
```
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <mailgun@YOUR_DOMAIN_NAME>' \
    -F to=YOU@YOUR_DOMAIN_NAME \
    -F to=bar@example.com \
    -F subject='Hello' \
    -F text='Testing some Mailgun awesomeness!'
```

### Reverse engineering from the above command
It is a post request, it adds "Authorization" to the headers. The username is 'api', and the password is your Mailgun API key. Replace the domain name on the URL by your Mailgun authenticated domain name.
