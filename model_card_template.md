# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was developed by Shaun Loya, a student of Western Governors University, in 2024.
The model uses a SciKit Learn Random Forest Classifier to process demographical data, anwsering questions regrading the 
likely outcome of a given variable. This model starts with many default hyperparameters as the intended nature is to
apply the model to slices of the data. Tuning the model to any specific slice would generate bias or overfitting however,
based on the specific question, some adjustments could be added for more insights. 


## Intended Use
The base line of this model is evalutation the many other factors of the demographic data against whether that instance's "Salary" is greater or less than 50,000 USD. This data can be useful to many different stakeholders that may need at assess a target populations annual income based on the other factors. Such groups or stakeholders could be marketing groups for advertisement or reasearch groups like government entities looking for trends in populations. 


## Training Data
This data was provided in the project's starter package but is a commonly available and used census data set from the early 1990s. The sourced information and details can be found at this link: https://archive.ics.uci.edu/dataset/20/census+income. The data is split in with 75% of the data going into training. 

Some basic processing was completed on this data to make it viable for machine learning algorithms. This included the OneHotEncoder and label binarizer to generate binary values for the machine learning process. 

## Evaluation Data
The source data is the same location as the training data. The data, after the preprocessing steps of OneHotEncoder and LabelBinarizer, is split with 25% of the data set aside for testing. The output of evaluation is the the Percision, Recall and F1 Scores. 

## Metrics
The primary questions is how the identified categorical features can be used to identify the outcome of the "salary" feature. 
With the RandomForestClassifier model, the following scores were generated:
Precision: 0.7469 | Recall: 0.6326 | F1: 0.6850.
_Please include the metrics used and your model's performance on those metrics._

## Ethical Considerations
Demographic data, while publicly available, should still be treated and used with respect as each instance is a profile of a specific person or household. While not specifically Person Identification Infomation, users of this information should not use the information in malicious ways. 

## Caveats and Recommendations
This project develops a base functioning pipeline and model. Further investigating of the bias of the model using tools such as Aequitas might help tune the model into developing more complete insights. 