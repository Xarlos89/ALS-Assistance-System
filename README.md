# ALS-Assistance-System

The point of this Repository is to document the software and workarounds that I have implimented in my attempt at helping a man with ALS.

### Back Story
I was asked by a man with ALS to help him use a computer. He is unable to move his body for the most part, and only has control over his head and neck. Similar assistive solutions can be thousands of euros, and thus was not an option. I am creating this repository to document the software I used and the things I developed to assist him, in hopes that it helps others in similar situations. 

### Hardware
- Computer was a basic LENOVO IdeaCentre 310S-08ASR (90G900A2GE) connected to a 60" Samsung televeision.
  - Running Windows 10
- SANDBERG USB Webcam Pro+ 4K
- Anker Power Conf bluetooth conference speaker. 
 
# Mouse Tracking

We tried a variety of mouth-tracking, eye gaze and facial movement tracking softwares with varying results. Some didn't work well with the distance we were using. Naturally, we didn't want to sit him a half meter away from a big screen tv. We also didn't want a large obtrusive arm reaching out to put the camera on his face.
E-Viacam allows you to set up a profile for the user, so we dont have to reset any settings. This program starts on startup, allowing him to take control of the PC from first start. 

#### The best open source software in our use-case was 
- https://eviacam.crea-si.com/index.php

#### Notable software included 
- http://www.cameramouse.org/ 
- http://www.inference.org.uk/opengazer/

### A note on Facial Tracking
We struggled with getting the Webcam to track his face, since he was sitting about 2 meters from the camera. A workaround we discoverd was to use a streaming software called Splitcam. It allows you to digitally zoom the webcam feed, and thus allowed us to zoom in on his face and track it better. I highly reccomend using SplitCam with E-Viacam. You can also set up a profile with this software, which automatically zooms the camera after E-ViaCam is started. No messy settings when we start the camera system.
https://splitcam.com/

# Keyboards
While Windows 10 comes standard with a virtual keyboard, it proved to be tiring and cumbersome to use when paired with a facial tracking mouse. I also wanted to customize the keys since we were not using all of them.
To remedy this, we started searching for alternatives. Most alternatives are remakes of the standard keyboard, and are honestly no better than the Windows 10 keyboard.

One software stood out, with a fully customizable keyboard. Including the ability to run scripts using buttons on the board.
It is a paid software, but for $30... About the price of a keyboard. We didn't care.

### The Best option for our use-case
https://hotvirtualkeyboard.com/

Hot Virtual keyboard was a bit complex, but allowed us to fully customize key layouts and build a keyboard form scratch. It also allows me to map scripts to a key, which is excellent for running touch gesture scripts. We also have a button for entering his username and password, an 'undo' button, buttons for special German charaters, and a buch of other custom keys that make navigating this system much easier. 

#### Some notable runner ups were:
https://hodgef.com/simple-keyboard/
https://www.comfortsoftware.com/on-screen-keyboard/

# Phone
### Mirring the phone on the PC screen
We are using an open-source program called Scrcpy (https://github.com/Genymobile/scrcpy) to mirror the phone on the screen. SCRCPY allows us to mirror the screen of the phone on the TV screen, and connect this wirelessly. We are using a simple .BAT file to open the python script, however I may convert all these .py scripts to .exe files in the future. 
Clicking is handled fine with E-viacam, and touch gestures are handled with my custom scripts meantioned above. 
A problem we encountered was the microphone picking up sound from far away, since the phone isn't always nearby. To remedy this, we attached an Anker PowerConf bluetooth conference speaker to the computer via USB, and to the phone using bluetooth. Now when calls are received, he sees this on the screen and can click answer. The phone runs the sound and microphone through the bluetooth speaker and he is able to speak clearly on the phone. 

### Scripts
The scripts are custom and written by me using Python and a library called PyAutoGUI (https://pyautogui.readthedocs.io/en/latest/)
We currently use 5 different scripts to handle different touch functions. and one script to auto-connect the phone when it is detected. We have mapped these scripts to run when the arrow keys of the On-screen keyboard are pushed. Pressing the up arrow activates a swipe up, pressing down activates a swipe down, left is a left swipe and right is a right swipe. We also have a seperate button to pull down the top menu of the android phone. 

  
