def check_entries(df, old_df):
    updated_entries = df[df['name'].isin(old_df['name'])].drop_duplicates(subset=['name'])

    new_entries = df[~df['name'].isin(old_df['name'])]

    return updated_entries, new_entries


def update_entries_price_in_original_df(updated_entries, old_df):
    updated_entries = updated_entries.sort_values('name').reset_index()

    temporary_df = old_df[old_df['name'].isin(updated_entries['name'])].sort_values('name').drop_duplicates(
        subset=['name']).reset_index()

    updated_entries.loc[(updated_entries.previous_price == 'new entry'), 'previous_price'] = 'no change in price'

    price_mask = temporary_df['price'] != updated_entries['price']
    updated_entries.loc[price_mask, 'previous_price'] = temporary_df.loc[price_mask, 'price']

    temporary_df[temporary_df.columns[1:6]] = updated_entries[updated_entries.columns[1:6]]

    temporary_df = temporary_df.set_index('index')

    old_df.loc[temporary_df.index] = temporary_df

    old_df.loc[(old_df.status == 'new'), 'status'] = 'old'
    old_df.loc[(old_df.previous_price == 'new entry'), 'previous_price'] = 'was not seen'

    return old_df


def append_new_entries(updated_df, new_entries):
    updated_df = updated_df.append(new_entries, ignore_index=True)

    return updated_df


def compare_old_new_entry_in_df_format(df, old_df):
    updated_entries, new_entries = check_entries(df, old_df)

    updated_df = update_entries_price_in_original_df(updated_entries, old_df)

    updated_df = append_new_entries(updated_df, new_entries)

    return updated_df
