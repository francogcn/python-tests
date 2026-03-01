#AUTO LOGIN
import requests

url = str(input('LOGIN_URL'))
# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': 'username',
    'inUserPass': 'password'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(url, data=payload)
    # Print the HTML returned or something more intelligent
    # to see if it's a successful login page.
    print(p.text)

    # An authorised request.
    r = s.get('A protected web page URL')
    print(r.text)
