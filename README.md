# Synthetic Question-Answer dataset generator

How this works:

When you run the program, it will pull a custom dolphin-mistral model for generating system prompts to steer a question-answering model. it will also pull phi:3 mini for generating questions. if you have these models already downloaded, it will skip that step.

From there you can enter a ollama model you already have to answer the questions, or you can let the program set up a new custom model to answer the questions, with the system prompt based on the behavior you want the custom model to have generated by the dolphin-mistral model.

It will then ask you how many pairs of questions and answers you want to generate.

It will then take a random topic, then generate a question about that topic using the question model.

the answering model will answer the question, and then you can see the question and answer. If you like the question and answer, you can let it run and generate all the pairs you want. If you don't like the question and answer, you can enter 'n' and the program will exit, and you can run the process over again.

when the pairs are generated it will ask you if you want to format the questions and answers to the FineTome-100k format. if yes, it will format them and save them to a csv file. if no, it will save them to a csv file without formatting.

the program will then exit after giving you some stats about the time it took to generate the pairs.

csv files are saved in the 'csv_files' folder in the utils folder.
modelfiles are saved in the 'model_files' folder in the utils folder.
script files are saved in the 'script_files' folder in the utils folder.

the scripts and modelfiles are how the custom models are made based on the system prompts generated by the dolphin-mistral model.
-------------------------------------------------------------------------------------------------------


To run the program, run main.py after installing the requirements.txt file.

Can control what topics the models can talk about by changing the topic list in main.py.
Default question model is 'phi3:mini', but can be changed by changing the question_model variable in main.py.

When asked if you want to format the questions and answers, it will format them to the FineTome-100k format.
https://huggingface.co/datasets/mlabonne/FineTome-100k


-------------------------------------------------------------------------------------------------------

Error if scripting is not allowed for windows: https://stackoverflow.com/questions/41117421/ps1-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system

