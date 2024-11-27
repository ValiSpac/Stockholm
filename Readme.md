# Stockholm.py

**Stockholm.py** is a Python script designed to encrypt and decrypt files targeted by the WannaCry ransomware. It provides functionality to both simulate an infection and recover files using a generated decryption key.

## Usage

```bash
python stockholm.py -h

Command-line Arguments
Option	Description
-h, --help	Show help message and exit
-v	Display the version of the program
-r R	Reverse the infection using the generated key
-s	Suppress output for encryption
Features

    Encrypt multiple file types (.txt, .sql, .mp3, .bad) for testing.
    Reverse encryption using a decryption key.

Setup Instructions

    Clone the repository.
    Configure the environment:

make configure

Activate the Python virtual environment:

source venv/bin/activate

Run the script:

    python3 stockholm.py

Cleaning Up

To remove the environment and test files, run:

make fclean

