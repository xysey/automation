#! python3
"""
opens up twitter.com to the default browser
"""
import webbrowser, sys

if len(sys.argv) == 2:
    if sys.argv[1] == "explore":
        webbrowser.open("https://twitter.com/explore")
    elif sys.argv[1] == "notifications":
        webbrowser.open("https://twitter.com/notifications")
    elif sys.argv[1] == "messages":
        webbrowser.open("https://twitter.com/messages")
else:
    webbrowser.open("https://twitter.com")
