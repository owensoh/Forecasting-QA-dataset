# Forecasting QA Dataset

I intend to create a high quality forecasting QA dataset for the cyber security domain that can be used for future forecasting purposes (i.e. Model Training).

The questions will be generated for each component of the MITRE Attack Framework via the selected ChatGPT model (3.5 or 4 Turbo), using the pre-processed CTI report summary generated using the MITRE Attack Framework. 

It will be run through an Alignment module to check if the question being generated is aligned with the summary itself. The alignment is then checked with manually by a domain specialist to determine the accuracy of alignment.

A simple Chain of Thought answering module is generated such that a confusion matrix of the generated answers (for MCQ) is created to determine the difficulty of each of the option. 
