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
    with open(filename, "r") as fd:
        contents = [n.strip() for n in fd.readlines()]
        return contents


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stove.")
    parser.add_argument(
        "-r",
        "--recipients-file",
        required=True,
        help="text file containing possible recipients",
        type=str,
    )
    parser.add_argument(
        "-d",
        "--database-file",
        help="csv file contain sources for sending text messages",
        type=str,
    )
    parser.add_argument(
        "-p",
        "--message-probability",
        help="probability for sending a text",
        type=float,
        default=0.25,
    )
    args = parser.parse_args()

    text_generator = TextGenerator(args.database_file)
    account_store = AccountStore(
        os.environ["STOVE_GVMS_HOSTNAME"], os.environ["STOVE_GVMS_PORT"]
    )

    randomizer = Randomizer(args.message_probability)

    account_store.setup()
    accounts = account_store.get_accounts()
    recipient_numbers = get_recipient_numbers(args.recipients_file)
    for account in np.random.permutation(accounts):
        for recipient in np.random.permutation(recipient_numbers):
            time.sleep(random.random() * 5)
            ok = randomizer.randomize(
                lambda: account.send_text(text_generator.randomize(), recipient)
            )
            if ok:
                print("Account", account.get_number(), "|", "Recipient", recipient)
