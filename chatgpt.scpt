tell application "ChatGPT"
    activate
end tell

delay 1 -- wait for app to be ready

tell application "System Events"
    keystroke "Hello, ChatGPT!" -- your prompt
    key code 36 -- press Return
end tell