#! python3
"""
Opens up google search
"""
import webbrowser as wb, sys

if len(sys.argv) > 1:
    item = "+".join(sys.argv[1:])
    wb.open("https://www.google.com/search?q=" + item)
else:
    wb.open("https://www.google.com")
