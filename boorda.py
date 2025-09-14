import pandas as pd
import sys

def rank(df, category):
    boorda = df[['votes', category]]
    return boorda.groupby(category).sum().sort_values(by='votes',ascending=False)

def main():
    category = sys.argv[1]
    df = pd.read_csv('draft_data_2024.csv')
    df['votes'] = len(df) + 1 - df['pick']
    result = rank(df, category)
    return result.head(20)

if __name__ == '__main__':
    print(main())