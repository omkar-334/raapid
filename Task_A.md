# Task A:- Natural Language Inference

## Problem statement

Natural Language Inference (NLI), also known as
Recognizing Textual Entailment (RTE), is the task of determining the
inference relation between two (short, ordered) texts: entailment,
contradiction, or neutral (MacCartney and Manning 2008).

## Task Description

For this task, the participants are
asked to develop a GenAI base solution for the given problem. You can
use any small version of llama and it should be fine-tuned(instruction
tuning) only with the training dataset and the validation dataset should
be used to tune the hyperparameters of the model. Finally, the model
performance has to be tested on test datasets. All the participants
should submit both the validation accuracy as well as test the accuracy
along with the output prediction files, training script and the model.
The prediction files should be in .tsv format where the model prediction
should be appended at the last column in the validation and test
dataset.

## Data

The corpus consists of 570k sentence pairs manually labeled for balanced
classification with the labels entailment, contradiction, and neutral,
supporting the task of natural language inference (NLI), also known as
recognizing textual entailment (RTE). The dataset consist of three
parts, training, testing and validation datasets. The premise and
hypothesis are provided as PCFG parsed output. So, the participants have
to extract the raw sentences from the parsed outputs. The extracted raw
sentences should be used as input to the model.

| Task Name | Training pairs | Validation pairs | Test pairs |
|-----------|----------------|------------------|------------|
| NLI       | 550,152        | 10,000           | 10,000     |

## Dataset Link

The dataset can be downloaded from
[[here]{.underline}](https://drive.google.com/file/d/14kplogWzU2JsIB04ENeLtgtYTt0kYyxU/view?usp=sharing).

**[Evaluation metrics:]{.underline}** Accuracy and Macro average
F1-score will be used as the evaluation metrics for this task.

## Submission guidelines

[Every participant has to submit their scripts in a well structured
format. And, the submitted results should be easily reproduced from the
scripts.]{.mark}
