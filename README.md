# Shell Hacks Project
Find text from any image and translate it to user's primary language of choice (Particularly a restaurant menu)

# Applications Used
API: Google Cloud Vision and Google Translator --  Environment: Anaconda  -- Programming Language: Python

# Instructions
## What do you need?
### Anaconda + Python
- Anaconda Navigator/Prompt (Your choice)
 -Download Anaconda here [https://www.anaconda.com/products/individual]
 - Work environment with Python 3.5 >=
  -Follow these instructions to set up an environment [https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/]
 - Python libraries: googletrans, pillow, google-cloud-vision
  -In your environment terminal either do "pip install 'python library'" or "conda install 'python library'" follow these instructions for help [https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/], [https://datatofish.com/how-to-install-python-package-in-anaconda/]
  
 ### Google Cloud
- A google cloud account with a project and google cloud vision API enabled and authenticated
 - Create  a google cloud account(https://cloud.google.com) go to "Console" in the top right corner of the screen
 - Create a project, name it based whatever suites you
 - In the search bar searrch for Vision API, click on the one in the "Marketplace"
 - Click 'Enable API' and then click on 'Create Credentials' 
 - When choosing API pick Cloud Vision API, then select 'No im not using them both' (Unless you do)
 - Create your own service name and set role to Project -> owner, and then pick JSON
 - 
 
 ### To run:
 - Download the associated files in this repository
 - Rename your .json file to "menuTranslatorAuthentication.json". This is for consistency's sake
 - In Anaconda, select the environment you created earlier and press the green triangle
 - Press "Open Terminal"
 - In your terminal, type "python main.py"
