![Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![Relase Version](https://img.shields.io/github/release/kbot-lyfe/chipper-app.svg)

# chipper-app
Chipper app is a program that can encrypt or decrypt a given file from a given text. The algorithm used is based on the classic Vigenère cipher method. Click [here](https://en.wikipedia.org/wiki/Vigenère_cipher) for further information about Vigenère chipper.

## Prerequisites
This program runs on [Python3](https://www.python.org/downloads/). If you haven't got Python3 installed, you can download it in [here](https://www.python.org/downloads/). Additionally, this program requires some modules (shown below) which can be obtained by using package manager [pip](https://pip.pypa.io/en/stable/) to install the required modules.

```bash
pip install termcolor
pip install getpass
```

## Installation
Clone this repository and save it somewhere in your local directory. That's all :)

## Usage
Place the "to be encrypted" file in `src` directory, `cd` into `src` directory and run the program in the following format
```bash
python chipper.py [filename]
```
Where `[filename]` is the name of the text file that will be encrypted or decrypted which is located at the same directory as `chipper.py` file.

_(Note that you have to be inside the directory where `chipper.py` is stored to run the program)_

The program will prompt the user to set the program **mode** (e.g. **_decrypt_** or **_encrypt_** mode). Then, the program will ask the user to enter the **key** to either encrypt or decrypt the given file.

If the program is on encrypt mode, it will create a new file `encrypted.txt` which contains the encrypted text. If the program is on decrypt mode, it will create a new file called `decrypted.txt` which contains the decrypted text.

## Disclaimer
The encrypted file is not 100% guaranteed to be safe, as there are other programs that could crack the chipper (such as brute force method). The software and code in this project are provided "as is" without warranty of any kind, either express or implied. Use at your own risk.


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
