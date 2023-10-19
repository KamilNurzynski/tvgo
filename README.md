This is a program to test orangetvgo.apk

To the tests I used orange-tv-go.apk version 3.29

Emulated device: Pixel3XL, Android 10, 

Instruction how to use it on Windows:
1. Install python 3.11
2. Install Appium 2.0
3. Install Java 1.8.0_381
4. Create project in your Python IDE
5. Install libraries/frameworks to your project from requirements.txt file
6. Copy/import repoistory. Make sure that conftest.py and test_OrangeTvGo.py are in the same folder.
7. Change *.apk path in conftest.py to lacation on your computer. conftest.py --> desired_capabilities -->  desired_caps['app'] = 'location on your computer' 
8. Start your appium server. Make sure to have
   Remote pathset like: /wd/hub
   Host: 0.0.0.0
   Port: 4723
9. Open in IDE terminal with location of your project.
10. Write command line: py.test -v -s test_OrangeTvGo.py
11. Tests are started
