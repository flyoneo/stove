import pandas as pd
from pathlib import Path
import random
import time

DATABASE = Path("quotes.csv") # TODO make stove into CLI to read in any .csv file

df = pd.read_csv(DATABASE, sep=";") 

df_length = df.shape[0]
random_quote = random.randint(0, df_length)

# format chosen_row
chosen_row = df.iloc[random_quote]
chosen_quote = '"' + chosen_row.QUOTE + '"' + "\n"
chosen_quote += '-' + chosen_row.AUTHOR

