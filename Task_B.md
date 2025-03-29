
# Task B:- Data Processing

## Problem statement

From the given sentences, list down all sentences
into the format provided below where the given patterns are found.

## Task Description

For this task, the participants are
required to find out the phrases present in sentences that matched the
given patterns. The extracted phrases should be stored in the mentioned
json format. The sentences are provided in the format word1/posTag1
word2/posTag2 word3/posTag3 etc. The words and the tokens are separated
by "/".

select largest phrase if smaller pattern is also found for e.g. if raw
text is "of/in engine/nn cowling/nn" here "in nn nn" and "in
nn" pattern are found, select only largest matching pattern i.e "in nn
nn"

## Pattern 1

identify patterns that start with an "in" tag and are
followed by one or more "nn" tags. for ex. "in nn","in nn nn","in nn nn
nn","in nn nn nn nn" etc.

### Input 1

`'A/at large/jj piece/nn of/in engine/nn cowling/nn vanished/vbd ./.'`

filename, para_id and sent_id are also provided as input

### Output 1

```json
{
    "pattern": "pattern 1",
    "sents":
    [
        {
            "filename": "cn15",
            "para_id": 0,
            "sent_id": 0,
            "sent_text": "A large piece of engine cowling vanished .",
            "phrases":
            [
                {
                    "begin": 14,
                    "end": 31,
                    "text": "of engine cowling",
                    "phrase_type": "in nn nn"
                }
            ]
        }
    ]
}
```


## Pattern 2

identify patterns that start with an "jj" tag and are
followed by one or more "nn" tags. for ex."jj nn","jj nn nn","jj nn nn
nn","jj nn nn nn nn".. etc

### Input 2

`'A/at large/jj piece/nn of/in engine/nn cowling/nn vanished/vbd ./.'`

filename, para_id and sent_id are also provided as input

### Output 2

```json
{
    "pattern": "pattern 2",  
    "sents":  
    [  
        {  
            "filename": "cn15",  
            "para_id": 0,  
            "sent_id": 0,  
            "sent_text": "A large piece of engine cowling vanished .",  
            "phrases":  
            [  
                {  
                    "begin": 2,  
                    "end": 13,  
                    "text": "large piece",  
                    "phrase_type": "jj nn"  
                }  
            ]  
        }  
    ]  
}
```

## Data

Dataset consists of sentence wise data
containing

| Task Name       | files | paragraphs     | sentences |
|-----------------|-------|----------------|-----------|
| Data Processing | 500   | 15667 | 57340     |

[Dataset Link](https://drive.google.com/file/d/18I0-BhF2czFA_i6qCcMbDS9mBWknSrDF/view?usp=share_link)

## Evaluation metrics

F measure for each json element present in "sents" key

## Submission guideline

Participants should submit 2 json files named
"pattern_1_abc@gmail.com.zip\" and \"pattern_2_abc@gmail.com.zip\" along
with scripts used. And, the submitted results should be easily
reproduced from the scripts.

[json file name should be \"pattern_1_abc@gmail.com.json\" after zipping
this file resulting file should be named
\"pattern_1_abc@gmail.com.zip\"]{.mark}

## Submission Form

> [Task A](https://forms.gle/uosVJ4v3uopXgKfg6)  
> [Task B](https://forms.gle/fZm2ZCsYVDhbP7Ai8)  
