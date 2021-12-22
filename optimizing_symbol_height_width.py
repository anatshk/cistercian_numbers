""" scratch for finding the best ratio of height to width """
import numpy as np

from show_cistercian_number import main
from symbol_generation.symbol_mapping import create_symbols, show_mapping
import pandas as pd
from pathlib import Path

HEIGHT = 'height'
WIDTH = 'width'
IS_GOOD = 'is_good'

pth_save_file = 'log_height_width.csv'

MIN_HEIGHT, MAX_HEIGHT = 5, 35
MIN_WIDTH, MAX_WIDTH = 5, 35

if Path(pth_save_file).exists():
    df = pd.read_csv(pth_save_file)
else:
    df = pd.DataFrame(columns=[HEIGHT, WIDTH, IS_GOOD])
    for h in range(MIN_HEIGHT, MAX_HEIGHT):
        for w in range(MIN_WIDTH, MAX_WIDTH):
            df = df.append(pd.DataFrame(data={HEIGHT: [h], WIDTH: [w], IS_GOOD: [np.nan]}), ignore_index=True)
    df.to_csv(pth_save_file, index=False)


for ix, row in df.iterrows():
    height, width, is_good = int(row[HEIGHT]), int(row[WIDTH]), row[IS_GOOD]

    # skip if already tested
    if not pd.isna(is_good):
        print(f'Already checked ({(height, width)})')
        continue

    print(f'checking ({(height, width)})')

    symbol_mapping = create_symbols(symbol_height=height, symbol_width=width)
    show_mapping(symbol_mapping)

    # TODO: instead of one number 1993, add 4723, 6859, 7085, 9433, 3333, 4444, 5555, 9999
    #  use num = arabic_to_cistercian and then use 1 - num.symbol.symbol ? and concatenate numpy arrays --> plt.show
    main(number_to_convert=1993, height=height, width=width, symbol_mapping=symbol_mapping)

    does_this_look_good = input('does this look good? (Y)es, (N)o, Stop increasing (W)idth, (S)top and save: ').lower()

    if does_this_look_good in ['y', 'n']:
        numerical_value = 1 if does_this_look_good == 'y' else 0
        df[IS_GOOD].iloc[ix] = numerical_value
    elif does_this_look_good == 's':
        df.to_csv(pth_save_file, index=False)
        break
    elif does_this_look_good == 'w':
        ix_to_update = (df[HEIGHT] == height) & (df[WIDTH] >= width) & pd.isna(df[IS_GOOD])
        df[IS_GOOD].iloc[ix_to_update] = 0
        break

    df.to_csv(pth_save_file, index=False)

# TODO: run the code until every height and width combination is filled
# TODO: analyze ratio between all good combinations (IS_GOOD = 1)
# TODO: make changes to CistercianSymbol class to only accept height and calculate with according to the ratio
# TODO: then create a dataset of different sizes and train model that takes the number, splits it into quarters,
#  flips accordingly and detects digits - then returns the digit * its quarter order
