from os import environ
import smtplib
from email.message import EmailMessage
import functools


def set_environ_variables():
    global EMAIL
    global PASSWORD

    EMAIL = environ.get('EBAY_TRACKER_EMAIL')
    PASSWORD = environ.get('EBAY_TRACKER_PASSWORD')


def set_html_format():
    hyperlink_format = '<a href="{link}">{text}</a> <i>${price}</i>'
    link_text = functools.partial(hyperlink_format.format)
    return link_text


def build_content_email(df, link_text):
    message = '<h2><p>Here is a list of items that meet your price range</h2></p>'
    for i in range(len(df)):
        message += f"{link_text(link=df['link'].loc[i], text=df['name'].loc[i], price=df['price'].loc[i])}<br>"

    return message


def send_email(user_email, prompt, message):
    msg = EmailMessage()
    msg['Subject'] = 'eBay tracker update for: %s' % prompt
    msg['From'] = EMAIL
    msg['To'] = user_email

    msg.add_alternative(message, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)


def main_email_module(df, user_email, prompt):
    set_environ_variables()
    link_text = set_html_format()
    message = build_content_email(df, link_text)
    send_email(user_email, prompt, message)
