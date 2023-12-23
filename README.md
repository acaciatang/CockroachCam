# CockroachCam
CockroachCam contains code that labels cockroaches with their names and instructions for setting up a cockroach livestream.

<br><br>

## Requirements
### Hardware
- Raspberry Pi (tested on Raspberry Pi 4 Model B)
- webcam
- SD card
- monitor
- HDMI cable
- internet access

### Software
- Raspberry Pi OS Bullseye (Legacy, 32-bit)
- OBS studio ([Click here for installation instructions](https://raspberrytips.com/install-obs-studio-raspberry-pi/): follow section for Legacy OS)
- python package: opencv
    ```
    #install opencv on the raspberry pi using this code:
    sudo apt-get install python3-opencv
    ```

<br><br>

## Set up
1. Clone this repository and run CockroachCam.py
   ```
   git clone https://github.com/acaciatang/CockroachCam.git
   ```
2. Log into twitch account
3. Go to creator dashdoor → settings → stream, then copy primary stream key
4. Open OBS Studio
5. Follow instructions of set-up wizard, inputting stream key when prompted
6. Run CockroachCam.py
   ```
   #cd into this repository, then run
   python3 CockroachCam.py
   ```
7. Add source → Window Capture (Xcomposite), choose output from CockroachCam.py
8. Turn off all sound
9. Start stream

<br><br>

## Maintainers
Acacia Tang -- [ttang53@wisc.edu](mailto:ttang53@wisc.edu)