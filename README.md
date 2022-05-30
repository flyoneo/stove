# Stove
A tool for building resistance against bot-detectors on newly generated GVoice numbers.

## Configuration
Configuration is split between a `.env` file and command-line flags.

### Env File
Copy or rename the `template.env` file as `.env`. From there, the following
configuration options are available:
- **STOVE_GVMS_HOSTNAME=** the hostname for GVMS.
- **STOVE_GVMS_PORT=** the port for GVMS.

### Commandline Flags
The following flags offer configuration when running stove:
- **-r/--recipients-file=** text file containing possible recipients.
- **-d/--database-file=** csv file containing sources for text generation.
- **-p/--message-probability=** probability for sending a text. Value must be
  between 0 and 1.

## Recipient file
A recipient file is used to guide a GVoice number to a list of possible
numbers on which it can send text messages. This is necessary for reputation building
to take place.

The recipient file is simply a newline-separated file containing a list of numbers
(containing the country code).

Example of a recipient file:
```
11111111111
22222222222
```

## Setup
1. Ensure that [GVMS](https://github.com/kingcobra2468/GVMS) is setup and running.
2. Install dependencies with `pip3 install -r requirements.txt`
3. Run stove with `python3 src/main.py`. Example command:
```
python3 main.py -d datasets/quotes.csv -r recipients.txt -p 1
```