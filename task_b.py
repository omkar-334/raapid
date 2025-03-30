import json
import os
import re
import zipfile

import pandas as pd

# start with an "in" tag and are followed by one or more "nn" tags.
# PATTERN_1 = r"\bin\b\s+(\bnn\b\s+)+"
PATTERN_1 = r"(?<!\S|-)in\b\s+(\bnn\b\s+)+"

# start with an "jj" tag and are followed by one or more "nn" tags
# PATTERN_2 = r"\bjj\b\s+(\bnn\b\s+)+"
# the above regex did not work because '\b' (word boundary) was matching other non-space characters like hypen. Example "in-jj nn" was matching but it should not.
# in the new pattern, we are using negative lookbehind to ensure that the "jj" tag is not preceded by a non-space character or hyphen.
PATTERN_2 = r"(?<!\S|-)jj\b\s+(\bnn\b\s+)+"
EMAIL = "omkarkabde@gmail.com"

patterns = {"pattern_1": PATTERN_1, "pattern_2": PATTERN_2}


def create_match_dict(words, tags):
    """Creates a mapping of tag positions to word positions."""
    tag_length = 0
    word_length = 0
    match_dict = {0: 0}

    for word, tag in zip(words, tags):
        tag_length += len(tag) + 1
        word_length += len(word) + 1
        match_dict[tag_length] = word_length

    return match_dict


def create_entry(row, pattern):
    """Create an entry for a given row and pattern."""
    text = row["raw_text"]

    # separate the words
    splits = text.split(" ")
    # separate the words and tags
    words = [i.split("/")[0] for i in splits]
    tags = [i.split("/")[1] for i in splits]

    # create separate text sentences
    tags_text, words_text = " ".join(tags), " ".join(words)

    # initialize the entry with the row data
    entry = row.to_dict()
    entry.pop("raw_text")
    entry["sent_text"] = words_text

    match_dict = create_match_dict(words, tags)
    matches = re.finditer(pattern, tags_text)

    phrases = []
    for match in matches:
        phrase = {}
        tag_begin, tag_end = match.span()
        phrase["begin"] = match_dict[tag_begin]
        phrase["end"] = match_dict[tag_end]
        # map the tag positions to word positions
        phrase["text"] = words_text[phrase["begin"] : phrase["end"] - 1]
        # remove the last space from the text
        phrase["phrase_type"] = match.group().removesuffix(" ")
        phrases.append(phrase)
    entry["phrases"] = phrases

    return entry


def check_pattern(pattern_name):
    """Create a zip file for the given pattern."""
    df = pd.read_csv("dataset_B.csv")
    pattern_dict = {}
    pattern_dict["pattern"] = pattern_name.replace("_", " ")
    pattern = patterns[pattern_name]

    sents = []
    for idx, row in df.iterrows():
        try:
            entry = create_entry(row, pattern)
            if len(entry["phrases"]) > 0:
                # print(f"Entry: {entry}")
                sents.append(entry)
        except Exception as e:
            print(f"ERROR --- {idx} --- {e}")

    pattern_dict["sents"] = sents

    filename = f"{pattern_name}_{EMAIL}"
    create_zip(pattern_dict, filename)
    return pattern_dict


def create_zip(pattern_dict, filename):
    json_filename = f"{filename}.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(pattern_dict, f, indent=4, ensure_ascii=False)

    zip_filename = f"{filename}.zip"
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(json_filename, os.path.basename(json_filename))

    print(f"Created {zip_filename} containing {json_filename}")
    # os.remove(json_filename)


def create_script_zip():
    script_filename = "task_a.py"
    filename = f"{EMAIL}.zip"
    with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(script_filename, os.path.basename(script_filename))

    print(f"Created {filename} containing {script_filename}")
    # os.remove(script_filename)


if __name__ == "__main__":
    for pattern_name in patterns:
        check_pattern(pattern_name)
    create_script_zip()

    print("All patterns processed.")
