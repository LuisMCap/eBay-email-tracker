from user_prompt import *
from scrape_get_data import *
from email_module import *
from misc_module import *
from wait_module import *
from compare_old_and_new_entry import *


def tracker():
    prompt = prompt_user_for_item()
    df = get_data_in_df_format(prompt)

    down_time_hours = ask_wait_time()

    req_price = ask_requested_price()
    req_df = filter_data_for_user(df, req_price)
    user_email = ask_email()

    main_email_module(req_df, user_email, prompt)

    save_df(df)

    while True:
        down_time_seconds = calculate_total_wait_time(down_time_hours)
        sleep_time(down_time_seconds)

        df = get_data_in_df_format(prompt)
        original_df = get_original_df()

        updated_df = compare_old_new_entry_in_df_format(df, original_df)

        req_df = filter_data_for_user(updated_df, req_price)
        save_df(updated_df)
        main_email_module(req_df, user_email, prompt)
