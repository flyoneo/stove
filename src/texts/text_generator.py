import random

import pandas as pd
import numpy as np


class TextGenerator:
    """Generates random texts messages from a csv file.
    """

    def __init__(self, csv_path):
        """Constructor.

        Args:
            csv_path (str): Path the the csv dataset.
        """
        self._df = pd.read_csv(csv_path)
        self._df_size = len(self._df)
        self._df_fields = set(self._df.columns)

    def random(self, *fields):
        """Generates a random text message via a permutation of
        a subset of fields using a uniformly-chosen random row.

        Raises:
            ValueError: Thrown if one of the specified fields is not in
            the dataset.

        Returns:
            str: A randomly generated text message.
        """
        # check if all fields exist in the database
        if not set(fields,) <= self._df_fields:
            unknown_fields = set(fields).difference(self._df_fields)
            raise ValueError(
                f'The fields {unknown_fields} are not present in the database.')

        if fields:
            text_fields = self._df.loc[random.randint(
                0, self._df_size), list(fields)].to_dict()
        # if no fields specified, use all of the fields
        else:
            text_fields = self._df.loc[random.randint(
                0, self._df_size), list(self._df_fields)].to_dict()

        text_phrases = np.random.permutation(list(text_fields.values()))
        return ' '.join(text_phrases)
