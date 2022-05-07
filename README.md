# 2021_IBM_Code_Challenge_Social_Distancing
Download this & move to yolo-coco folder
# For CPU:
## To run this code in your terminal:
 Open your terminal**
 Change directory to where you have downloaded this code
 Install python3 if you have not, if installed already then it's ok!First we have to create the virtual environment.
Run - `python3 -m venv venv` -to create a virtual environment named venv
Run -`source venv/bin/activate'to activate your environment
Write   -`pip install -r requirements.txt `to install the python dependencies related to this project like opencv,numpy,scipy etc
Run the command- `time python social_distance_detector.py --input pedestrians.mp4 --output output.avi --display 1' to run your social distance detection project
After you run the last line of the project,a window will pop up and after execution of the file a `output.avi` file will be showing up in our directory
This is how it looks https://drive.google.com/file/d/1f4mWJjYlkq5lSO1aUJtmjz7a3ClfC-ZL/view?usp=drivesdk
