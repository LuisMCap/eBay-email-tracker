def prompt_user_for_item():
    prompt = input('What item do you want to track? ')
    prompt = prompt.replace(' ', '+')
    return prompt


def ask_wait_time():
    while True:
        try:
            down_time_hours = float(input('How much time do you want between updates in hours? '))
            return down_time_hours
        except ValueError:
            print('Insert a valid hour')


def ask_requested_price():
    while True:
        req_price = input(
            'What is a range of prices you would like to search the product for? input example: "200,250" ')
        req_price = req_price.split(',')

        if len(req_price) != 2:
            print('Insert a valid range')
            continue

        req_price = [float_error_price_range(price) for price in req_price]

        if False in req_price:
            print('Insert a valid range')
            continue

        if req_price[0] > req_price[1]:
            print('Insert a valid range')
            continue

        return req_price


def float_error_price_range(price):
    try:
        return float(price)
    except ValueError:
        return False


def ask_email():
    while True:
        user_email = input('Insert an email address to receive updates about your item: ')
        if '.' not in user_email[-6:] or '@' not in user_email:
            print('Insert a valid Email Address')
            continue

        return user_email
