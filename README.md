# What Is Ar-Bot-Rage?
Ar-Bot-Rage is a punny arbitrage script written entirely in Python 3. It is designed to watch and execute trades on cryptocurrency exchange CoinExchange.io, but it can easily be addapted to work on other exchanges that offer market data REST APIs.

# Dependencies
Ar-Bot-Rage tries to use as few third-party modules as possible. It's api calls use python's included requests module and it's timing systems use python's included time module. Finally, it also uses python's sys module for some file linking and exiting sequences. Note: because python's sys module is inherently system specific I can't guarantee this script will run on any systems other than OSX though I highly doubt you'll have any problems on other OSs.

Finally, as I am currently trying to impliment an automated trading system using GUI automation the script will also require the PyAutoGUI module. PyAutoGUI is a third-party python module and can be installed using pip.

# Roadmap
Ar-Bot-Rage's core codebase is complete. It can form 3-market arbitrage paths and evaluate them both as buy -> sell -> sell (forwards) and buy -> buy -> sell (backwards). Additionally, it has a fairly easy to understand command line interface.

Down the road I hope to upgrade Ar-Bot-Rage's capabilities in a few ways.

1 - I plan to make a rudementary AI (nural network) to allow the system to decide how to exit unsuccessful trades. Ex, if it completes 2 of the 3 trades necessary for an arbitrage opportunity and the 3rd changes at the last seconds to make the path unprofitable this AI would evaluate the situation to determine if it should simply take the hit, hold the position with the expectation of finishing the trade later at a profit, or make some other sort of trade sequence to salvage the situation.

2 - I plan to impliment a way for this system to trade 100% autonomously. This is currently very hard due to CoinExchange.io's lack of trading API. The only current way to impliment this would be GUI automation using image recognition to allow it to work on screens of different sizes and aspect ratios.

3 - I plan to add a GUI for Ar-Bot-Rage at some point. This is the least important of the changes I'm planning, but it is on the list. The GUI would be simple and clean. No advanced options or endless settings pages.

# Running the script
Running Ar-Bot-Rage is easy.

1 - Install python 3

2 - Press the green download button in the upper right-hand corner of the screen

3 - Find the zip on your machine and unpack it

4 - Find main.py in the unpacked file

5 - run main.py using python 3. For most this can be done in the command line with "python3 main.py" assuming your working directory is the same as the main.py directory.
