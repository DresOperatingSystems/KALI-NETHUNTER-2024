# 3rd Party build for Kali NetHunter on Android
#### (updated for 2026).

This repository provides a 3rd party build of Kali NetHunter designed for installation on Android devices using Termux. It enables a full Kali Nethunter desktop environment on a VNC for security research.

**Estimated Installation Time:** 45 minutes to 1 hour, depending on your network speed.  
**Minimum Device Requirements:** 2 GB RAM, 15 GB storage.

## Dependencies
Before starting, download the following applications:
- **Termux:** Install from F-Droid (recommended for regular updates; avoid the Google Play Store version).  
   - Download link: [https://f-droid.org/repo/com.termux_1022.apk](https://f-droid.org/repo/com.termux_1022.apk)  
   - GitHub Repository: [https://github.com/termux/termux-app](https://github.com/termux/termux-app)

- **VNC Viewer:** We recommended this one for accessing the desktop environment.  
    - Download link: [https://github.com/gujjwal00/avnc](https://github.com/gujjwal00/avnc)
## Setting Up Termux
After installing Termux, open the app and run the following commands one by one. Press `Y` to confirm any prompts.
```bash
pkg update && pkg upgrade -y
```
```bash
pkg install x11-repo -y
```
```bash
apt-get update && apt full-upgrade -y
```
```bash
termux-setup-storage
```
```bash
pkg install git && \
pkg install python && \
pkg install python3 && \
pkg install wget && \
pkg install curl && \
pkg install cmake && \
pkg install rust && \
pkg install proot
```
Your Termux environment is now set up. Now lets move onto the build.
## Installing Kali Linux environment
#### Run the following commands one by one:
```bash
pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh
```
#### After installation, start Kali:
```bash
./start-kali.sh
```
Your prompt should change to `root@localhost:~#`.
## Fixing Kali keyring 
Input these commands in the Kali environment before starting or this will not work at all.
```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys 827C8569F2518CC677FECA1AED65462EC8D5E4C5
```
```bash
gpg --export --armor 827C8569F2518CC677FECA1AED65462EC8D5E4C5 |  tee /etc/apt/trusted.gpg.d/kali-archive-2025.asc
```
## Installing the Desktop Environment (XFCE)
It is important that on this first part you do not kill the vncserver as we are building a desktop enviroment inside it.
#### Run the following:
```bash
wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/DesktopEnvironment/Apt/Xfce4/de-apt-xfce4.sh --no-check-certificate && bash de-apt-xfce4.sh
```
Follow the on screen instructions to complete the installation.
#### Then update the system:
```bash
apt update && apt full-upgrade -y
```
## Building Kali NetHunter
#### Install the NetHunter package:
```bash
apt install -y kali-linux-nethunter
```
#### Follow the prompts to build Nethunter: 
Answer `yes` to all questions. For Kismet, select `yes`, press Enter, leave the field blank and press Enter again. 
#### Error fix: 
After running `apt install -y kali-linux-nethunter` it will fail and when it does just input 
```bash
apt --fix-broken install
```
The error happens because we are missing certain packages in Termux needed for the build and the cmd above resolves the missing packages and continues the build like we could sit here and create a shell script that installs the right packages manually so we don't get this error at all but this just works plus every device is different.

Also The process may appear idle while configuring packages in the background do not interrupt or close Termux or you'll need to restart. 
#### Once finished continue with:
```bash
apt install apt-file
```
```bash
apt-file update
```
```bash
apt update && apt full-upgrade -y
```
#### If no updates are needed exit Kali:
```bash
exit
```
Press Ctrl + Z, then type `exit` twice.
#### Open Termux and start Kali again asap:
```bash
./start-kali.sh
```
Your prompt should now be the Nethunter one `┌──(root㉿localhost)-[~]`. Ignore any messages from Kali developers (it's an advertisement). 
#### Now run:
```bash
touch ~/.hushlogin
```
```bash
apt-get update && \
apt-get upgrade -y && \
apt autoremove -y && \
apt update && apt full-upgrade -y
```
## Starting the Desktop Environment
#### Start the VNC server:
```bash
vncserver
```
#### Open your VNC Viewer app and connect using:  
- Host: `127.0.0.1` (localhost)  
- Port: Typically `5902` (check Termux output for the exact port).  
- Password: The one you set during VNC setup.
Once logged in return to Termux and stop the initial VNC session:
```bash
vncserver -kill :1
```
It is no longer needed as by this point our desktop environment should be built
#### Troubleshooting: 
If you encounter a black screen on VNC run:
```bash
vncserver -kill :1
```
```bash
chmod +x ~/.vnc/xstartup
```
```bash
vncserver
```
The blackscreen error can happen for multiple reasons most of the time it is to do with connections to the VNC (it isnt a Kali specific error it is why we added this part). You should only get this error if you killed the first vncserver before logging back into the Nethunter environment and starting the second one.
## Nethunters toolkit and dependencies
Okay we are now on the final steps of the build. We now need to add the Nethunter toolkit to the desktop environment along with some dependencies.
#### follow the steps below to build Nethunters toolkit
Make sure the vncserver is running then make sure you're in Nethunters cmd line either in Termux or the Nethunter gui terminal on the vnc app.
Then run these commands below.
```bash
git clone https://github.com/DresOperatingSystems/Third-Party-Kali-Nethunter-Build
```
```bash
cd Third-Party-Kali-Nethunter-Build
```
```bash
python nhtools.py
```
yes we made a python script to automate the final steps, just let it run and once its done it will tell you `ALL DONE YOU SHOULD NOW HAVE A FULL WORKING NETHUNTER DESKTOP ENVIROMENT`.

## Exiting NetHunter
To exit follow the steps we took earlier to stop the VNC and exit Kali/Termux.
## Uninstalling Nethunter
just input this into the Termux cmd line not Nethunters
```bash
wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Uninstaller/Kali/UNI-kali.sh && bash UNI-kali.sh
```
Now Nethunter is removed from your device.
## end notes
> Our very first project release was this 3rd party build of NetHunter back in 2024 (now updated and working again). Honestly, we never thought back then that we'd take things as far as we have now and that's 100% thanks to all of our supporters. Truth is, we started this whole thing just messing around now we have a lifetime of work to be proud of. 

Anyways NetHunter was (and kinda still is) notorious for being broken. Rootless installs came with a million errors that made most people just give up and rooted ones could easily bootloop you or straight up hard brick your device. We spent way too many sleepless nights piecing it all together just because it was a challenge.

Seriously at the time you couldn't find any real fixes for Nethunter anywhere. Just hundreds of people on forums like Reddit, XDA, github etc asking the exact same thing: "how do I fix NetHunter??"

Instead of just trying to fix it we thought there has to be a another way. We already loved Kali Linux (we use it for our bot servers), the whole Linux community loves Kali and let's be real running Kali on your phone is just kinda cool y'know?

So out of that love, dedication and our respect for Kali plus the frustration with how broken Nethunter was this project was born.

Imagine if we never bothered or couldn't figure it out our whole organisation probably wouldn't even exist right now.

So we want to give the OffSec community a massive thank you especially the Nethunter team for being a massive inspiration to us 

---
Thank You and lets keep building            
**The DresOS Team**           

For questions or issues contact us directly you can find ways to contact us on our website here: https://dresoperatingsystems.github.io/
