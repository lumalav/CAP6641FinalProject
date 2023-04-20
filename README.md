# CAP6641FinalProject
Model Distillation as a defensive mechanism against BadPrompt

This repo references [BadPrompt](https://github.com/papersPapers/BadPrompt)

We used roberta-base in a sentiment analysis tasks using the following [dataset](https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset)

Then, we distilled the model using distilroberta-base and the [subj](https://github.com/princeton-nlp/LM-BFF) dataset and used this as the victim model over BadPrompt hoping to decrease its vulnerability.

[narrator]: it did not.
