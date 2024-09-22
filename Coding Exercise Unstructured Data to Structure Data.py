import pandas as pd
import re


df = pd.read_excel("C:/Users/0rame/Downloads/LM-Assignment-Test.xlsx",header=1)


def split(attributes):

    attr_dict = dict(re.findall(r'(\w+)=([\w\.]+)', str(attributes)))
    return attr_dict


parsed_attributes = df['Attributes'].apply(split)


attributes_df = pd.json_normalize(parsed_attributes)
structured_df = pd.concat([df['Time'], attributes_df], axis=1)

print(structured_df)

structured_df.to_csv('structured_output2.csv', index=False)
