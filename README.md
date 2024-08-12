# Developing a ML Pipeline using FASTAPI

##Synopsis
This project is designed to explore and practice the connecting the following abilities:
    Producing a viable ML model for classifing data and predicting a single outcome
    Saving the model for additional queries
    Generating a pipeline for the future queries
    Completing the project with GitHub actions


## Environment Set up (pip or conda)
This project was developed under a WSL vitrual environment and VS Code. A requirements.txt file is available for specific dependency versioning. Using following code or close variation of the code will give the deisred environment dependencies:

    #Intial environment code:
    conda env create -f environment.yml


    
## GitHub Repository
GitHub repo link: https://github.com/Sloya7/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

## Data
This project using the census.csv data supplied in the initial project package. This project avoids hard-coding so the file input lines in train_model line 17 will help with any adjustments for different files. 

## Model
A random forest classifier is utilized for this project. If different types of data is used in the future, a new file testing the efficiency of different models could be added. The used model is then saved and called upon from a sub directory of the parent directory for the project. 

## API Functionallity
The API functions are simple to display the ability to successfully integrate API communication into a pipeline. This project used a local 127.0.0.1 api system for testing and dispays a simple message. The local_apy.py file is best used to check for api functionallity on new machines or environments in the following code line:

    #testing local_api
    python local_api.py
Inside the local_api.py file on line 7 is the line for adjusting the local address if needed. 


##Project function
Once any adjustments for files and API integration are completed, to stay cmopliant with project stipulations, this set up takes in the data in local_api.py to process. Further development could make the input a user direct input or fill in a file that is already formatted for a parser. 

Initial project packet sourced from the branch:  udacity/Deploying-a-Scalable-ML-Pipeline-with-FastAPI
