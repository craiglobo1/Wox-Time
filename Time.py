from wox import Wox, WoxAPI
import pyperclip

# Your class must inherit from Wox base class https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
# The wox class here did some works to simplify the communication between Wox and python plugin.


class Main(Wox):

    # A function named query is necessary, we will automatically invoke this function when user query this plugin
    def query(self, key):
        text = key.split(' ')[1]
        if text.isnumeric():
            num = int(text)
            results = {
                "Title": f'{num + 5}',
                "SubTitle": "clyde is annoying",
                "IcoPath": "Images/clock.ico",
                "JsonRPCAction": {
                    "method": "addToClipboard",
                    # you MUST pass parater as array
                    "parameters": [text],
                    # hide the query wox or not
                    "dontHideAfterAction": True
                }
            }
            return results
        else:
            return {}

    def addToClipboard(self, text):
        pyperclip.copy(text)


# Following statement is necessary
if __name__ == "__main__":
    Main()
