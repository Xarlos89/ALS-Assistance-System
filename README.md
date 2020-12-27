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

### The best open source software in our use-case was 
- https://eviacam.crea-si.com/index.php

#### Notable software included 
- http://www.cameramouse.org/ 
- http://www.inference.org.uk/opengazer/

### A note on Facial Tracking
We struggled with getting the Webcam to track his face, since he was sitting about 2 meters from the camera. A workaround we discoverd was to use a streaming software called Splitcam. It allows you to digitally zoom the webcam feed, and thus allowed us to zoom in on his face and track it better. I highly reccomend using SplitCam with E-Viacam. Website below
https://splitcam.com/

# Keyboards
While Windows 10 comes standard with a virtual keyboard, it proved to be tiring and cumbersome to use when paired with a facial tracking mouse.
To remedy this, we started searching for alternatives. Most alternatives are remakes of the standard keyboard, and are honestly not better than the Windows 10 keyboard.

One software stood out, with a fully customizable keyboard. Including the ability to run scripts using buttons on the board.
It is a paid software, but for $30... About the price of a keyboard. We didn't care.
### The Best option for our use-case
https://hotvirtualkeyboard.com/

#### Some notable runner ups were:
https://hodgef.com/simple-keyboard/
https://www.comfortsoftware.com/on-screen-keyboard/
  
