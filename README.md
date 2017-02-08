# Installation

1. Install two apps - Termux and Termux:API
2. Run Termux
3. Type commands:

    apt update
    apt upgrade -y
    apt install termux-api python git -y
    git clone https://github.com/aol1306/android-morse

4. Now every time you want to run the app type:
    cd android-morse
    python morse.py [here-the-text-you-want-to-transmit]
5. Enjoy

# Usage example
    python morse.py 'Mary had a little lamb.'

# Quitting
To kill Termux process press 'Volume Down + C'
