# Limited Languaged Translator Project(Shell Hacks)
Find text from any image and translate it to user's primary language of choice (Example: restaurant menu)

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
 - Put Json file with the rest of your files
 - Rename your .json file to "menuTranslatorAuthentication.json". This is for consistency's sake
 - Now make sure your billing for the project is enabled 
 ### Google Cloud SDK
 - Follow the instructions to download and use Google Cloud CDK [https://cloud.google.com/sdk/docs/quickstart]
 - At the project selection, choose the project that has the Vision API Json, so the project you just created
 - Once done with that follow these instructions to make sure you did everything correct [https://cloud.google.com/vision/docs/setup#windows]
 ### To run:
 - Download the associated files in this repository
 - In Anaconda, select the environment you created earlier and press the green triangle
 - Press "Open Terminal"
 - Find the location of your folder and go to it cd (path to your folder)
 - In your terminal, type "python gui.py"
 - Select the language you want to translate to
 - Select the image you want to be translated
 - Click on translate
 - Finish!
 
 
 ## Comments
First attempt at trying to translate image text to another language based on user request, thank you shellhacks, and google!

