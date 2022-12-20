import pandas as pd

def get_signup_conversion_rate(x):
    new_cols = []
    new_cols.append(x['views'].sum())
    new_cols.append(x['registrations'].sum())
    new_cols.append((x['registrations'].sum() / x['views'].sum()) * 100)
    return pd.Series(new_cols, index=['views', 'registration', 'conversion'])

columns_to_check = [
        "popup_name",
        "blog_post_url",
        "popup_version|start_date|popup_category",
        "popup_header",
        "popup_description",
        "popup_image_url",
        "popup_title"
    ]

totals_df = pd.DataFrame(columns=['col_val','source','views','registration','conversion'])
df_orig = pd.read_table('dataset.tsv', sep="\t", converters={'COLUMN_NAME': pd.eval})
df = df_orig


for val in columns_to_check:
    fresh_df = df
    updated_df = fresh_df.groupby(val).apply(get_signup_conversion_rate).sort_values(by=['conversion'], ascending=False)
    updated_df.insert(loc=0,
          column='source',
          value=val)
    updated_df.to_csv('qu4'+ val +'.tsv', sep="\t")
    updated_df.rename(columns={val: 'col_val'})
    totals_df = totals_df.append([updated_df])
    totals_df = totals_df.sort_values(by=['conversion','registration'], ascending=False)

totals_df.to_csv('qu4_totals.tsv', sep="\t")