# Kali_T00ls2Ubuntu !
## @Author : M3tr1c_r00t
KaliT00ls2Ubuntu is a python script which is made for new ubuntu users, to help them install all the default and basic kali linux tools as ubuntu does not come defaultly installed with them.

### Setup...
For the script to run effectively, you need  to run the following commands on your terminal.
```
sudo apt update
sudo apt install git
sudo apt install python3
sudo apt-get -y install python3-pip
sudo pip install fade
```
if the fade module doesnt install, try this :
```
sudo pip3 install fade
```

### Installation...
```
1. git clone https://github.com/MetricCode/Kali_T00ls2Ubuntu.git
2. cd Kali_T00ls2Ubuntu
3. chmod +x KaliT00ls2Ubuntu.py
4. sudo mv KaliT00ls2Ubuntu.py /usr/bin/KaliT00ls2Ubuntu
```
### Execution...
For the script to work, you need to run it as root and also you need to have installed python3 on your system.
```
sudo KaliT00ls2Ubuntu
```
##### If there is this error;
```
/usr/bin/env: ‘python2\r’: No such file or directory
/usr/bin/env: use -[v]S to pass options in shebang lines
```
we can fix it by runing this command:
```
sudo dos2unix /usr/bin/KaliT00ls2Ubuntu
```
- Basically, the script first of checks if your system is updated.
- Afterwards, it confirms whether the snap package is installed on the system. 
- Next, it checks the tools which are not installed on your system and then installs them. 
![image](https://github.com/MetricCode/Kali_T00ls2Ubuntu/assets/99975622/07c51a9a-256e-4a15-86de-a39a23f17d9d)


#### Feel free to checkout my other repos for awesome content!
#### You can also visit the other repos while you're at it! 
## My socials:
<br>@ twitter: https://twitter.com/M3tr1c_root
<br>@ instagram: https://instagram.com/m3tr1c_r00t/
