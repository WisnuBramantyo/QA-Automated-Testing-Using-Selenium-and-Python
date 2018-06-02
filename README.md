[Tutorial for installing and testing python and selenium library on Linux] 

This tutorial is one of many ways to create an automated testing using Python + Selenium Library + Mozilla Firefox

#INSTALLING SYSTEM
=> Install Pip
sudo apt-install pip

=> Install Robot Framework
pip install robotframework

=> Install Selenium2Library
pip install robotframework-selenium2library

=> Install Selenium Library
pip install -U selenium

=> Install Geckodriver
Geckodriver is a web browser engine used in Mozilla Firefox. Gecko Driver is the link between your tests in Selenium and the Firefox browser[1].
1. Go to the geckodriver releases page. Find the latest version of the driver for your platform and download it : https://github.com/mozilla/geckodriver/releases
2. Extract the file with: tar -xvzf geckodriver*
3. Make it executable: chmod +x geckodriver
4. Add the driver to your PATH so other tools can find it: sudo mv geckodriver /usr/local/bin/ 

#Testing
Testing Description	: We are going to test our automation for logging in gmail
Pre-Conditions		: Prepare your gmail acccount to login, install tools required above

Steps :
1. Go to your working directory (Desktop, Home, or others)
2. Create web_test_python folder (you can create with command : mkdir web_test_python)
You can use, change or improve my test.py file attached here
3. Create or copy my test.py file into web_test_python folder 
4. Execute  test.python file using this command : python test.py
5. Wait. You can check the automation is running. On this testing, you will not get a report of your testing like robot framework does(check my other repo about automated testing using robot framework). 
But I think python is really powerfull if it is used on automated testing. 

Your automated testing is successfully done.
6. If the test works well, give a reward to yourself or shut your PC down, or get some foods. 

That's all guys. Thank you. 
I'm out.

References :
[1] https://www.linkedin.com/pulse/what-geckodriver-amith-wijesiri
