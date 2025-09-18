import speech_recognition as sr
import os
import subprocess

script = '''
tell application "System Events"
    key down command
    delay 0.05
    key up command
    delay 0.2
    key down command
    delay 0.05
    key up command
end tell
'''

subprocess.run(["osascript", "-e", script])