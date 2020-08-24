from wox import Wox, WoxAPI
import pyperclip
from math import floor
import datetime
from pytz import timezone
# Your class must inherit from Wox base class https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
# The wox class here did some works to simplify the communication between Wox and python plugin.


class Main(Wox):

    # A function named query is necessary, we will automatically invoke this function when user query this plugin
    def query(self, key):
        results = []
        VancouverTime = self.VanTime(key)
        results.append({
            "Title": f'Time: {VancouverTime}',
            "SubTitle": "clyde is annoying",
            "IcoPath": "Images/clock.ico",
            "JsonRPCAction": {

                "method": "copyToClipboard",
                # you MUST pass parater as array
                "parameters": [VancouverTime],
                # hide the query wox or not
                "dontHideAfterAction": False
            }
        })
        return results

    def VanTime(self, time):
        if self.validTime(time):
            nativeTime = datetime.datetime.strptime(
                time, "%H:%M") + datetime.timedelta(hours=13)
            return nativeTime.strftime("%H:%M")
        elif time == 'now':
            nativeTime = datetime.datetime.now(timezone(
                'Asia/Dubai')) + datetime.timedelta(hours=13)
            return nativeTime.strftime("%H:%M")

        else:
            return 'Error: Invalid Time'

    def validTime(self, time):
        return ':' in time

    def copyToClipboard(self, text):
        pyperclip.copy(text)


# Following statement is necessary
if __name__ == "__main__":
    Main()
