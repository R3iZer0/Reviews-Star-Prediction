import pandas as pd
import numpy as np
def compare_columns(df):
    conditions = [
        (df['roberta_neg'] > df['roberta_neu']) & (df['roberta_neg'] > df['roberta_pos']),
        (df['roberta_neu'] > df['roberta_neg']) & (df['roberta_neu'] > df['roberta_pos']),
        (df['roberta_pos'] > df['roberta_neg']) & (df['roberta_pos'] > df['roberta_neu'])
    ]

    choices = ['roberta_neg', 'roberta_neu', 'roberta_possss']
    df['result'] = pd.Series(np.select(conditions, choices, default='Equal'), index=df.index)
    return df

# Example usage:
# Assuming you have a DataFrame called 'data' with the columns roberta_neg, roberta_neu, roberta_pos
data = pd.DataFrame({'roberta_neg': [0.2, 0.4, 0.1],
                     'roberta_neu': [0.3, 0.5, 0.2],
                     'roberta_pos': [0.5, 0.1, 0.7]})

result_data = compare_columns(data)
print(result_data)
