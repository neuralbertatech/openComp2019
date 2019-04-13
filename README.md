# Open Competition 2019
 
 ## Project Description
 
 
 ## How to run...
 ### Requirements
 * A muse headset
 * A bluegiga bled112 bluetooth dongle
 * A MacOS machine (should also work on linux, but it has not been tested)
 * Requires python3

 * open terminal with `command + space` and type `terminal` and press `enter`

 > install homebrew with

  ` ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" `

 > then install venv and pyenv with

  ` brew install venv pyenv `

 > download files using git in root directory


  ` cd ~ `
  ` git clone https://github.com/neuralbertatech/openComp2019 `



 > move to project folder 

 ` cd ~/openComp2019 `

 > Configure a virtual environment to contain dependencies

 ```
  pyenv install 3.6.5
  pyenv local 3.6.5
  python3 -m venv venv
 ```

 > Activate the environment

 ` source venv/bin/activate `

 > Update Pip installer

 ` pip install --upgrade pip`

 > To install the required software run 

 `pip install -r requirements.txt`



 ### To run
  > move to project folder 

 ` cd ~/openComp2019 `

 > Activate the environment

 ` source venv/bin/activate `


 Run `python3 src/Stream/muse-lsl.py` from the root of the repository, you should see
 ```
 Found device Muse-XXXX : XX:XX:XX:XX:XX:XX
 Connected
 Streaming
```
 If you do not try running again.
 
 Then, with the muse on your head, open a new terminal `Command + t` 

  > Activate the environment

 ```
  pyenv local 3.6.5
  source venv/bin/activate 
 ```


 and run: 

 ```
 cd src
 python3 main.py
 ```
