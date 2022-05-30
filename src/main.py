import time
import os
import argparse
import random

from dotenv import load_dotenv
import numpy as np

from texts.text_generator import TextGenerator
from accounts.account_store import AccountStore
from adapters.randomizer import Randomizer

load_dotenv()


def get_recipient_numbers(filename):
    """Reads the newline seperated recipient numbers from the file.

    Args:
        filename (str): the path to the recipient file.

    Returns:
        list(str): a list of the recipients to which to send texts to.
    """
    with open(filename, 'r') as fd:
        return [n.strip() for n in fd.readlines()]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Stove.')
    parser.add_argument(
        '-r',
        '--recipients-file',
        required=True,
        help='text file containing possible recipients',
        type=str,
    )
    parser.add_argument(
        '-d',
        '--database-file',
        help='csv file containing sources for text generation',
        type=str,
    )
    parser.add_argument(
        '-p',
        '--message-probability',
        help='probability for sending a text',
        type=float,
        default=0.25,
    )
    args = parser.parse_args()

    account_store = AccountStore(
        os.environ['STOVE_GVMS_HOSTNAME'], os.environ['STOVE_GVMS_PORT']
    )

    text_generator = TextGenerator(args.database_file)
    accounts = account_store.get_accounts()
    randomizer = Randomizer(args.message_probability)

    recipient_numbers = get_recipient_numbers(args.recipients_file)
    # go through all of the gvoice numbers
    for account in np.random.permutation(accounts):
        for recipient in np.random.permutation(recipient_numbers):
            time.sleep(random.random() * 3600) # randomly sleep up to an hour
            success = randomizer.might_run(
                lambda: account.send_text(
                    text_generator.randomize(), recipient)
            )
            # the text message was sent successfully (positive sample against
            # the probabilistic lottery)
            if success:
                print('Account', account.get_number(),
                      '|', 'Recipient', recipient)
