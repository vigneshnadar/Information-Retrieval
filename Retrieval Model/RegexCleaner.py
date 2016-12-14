import re

# String -> String
# Given a string gives the output as a string after transforming and
# cleaning it
def transform_data(input_text):
    # regex to remove inverted commas at start
    transformed_text = re.sub(r'^"|"$', '', input_text)

    # fullstop between letter and spaces
    transformed_text = re.sub(r'([A-Za-z]+),?(\s+]?)', r'\1\2', transformed_text)
    # fullstop at end of letter
    transformed_text = re.sub(r'([A-Za-z]+),?(\s+]?)', r'\1\2', transformed_text)
    # print s
    # replaces opening br
    transformed_text=re.sub('\[','',transformed_text)
    transformed_text = re.sub('\]', '', transformed_text)
    transformed_text = re.sub('\^', '', transformed_text)
    transformed_text = re.sub('\(', '', transformed_text)
    transformed_text = re.sub('\)', '', transformed_text)
    transformed_text = re.sub('\!', '', transformed_text)
    transformed_text = re.sub('\{', '', transformed_text)
    transformed_text = re.sub('\}', '', transformed_text)
    transformed_text = re.sub('\"', '', transformed_text)
    transformed_text = transformed_text.replace('^','')
    transformed_text = transformed_text.replace('"', '')
    transformed_text = transformed_text.replace('[', '')
    transformed_text = transformed_text.replace(']', '')
    transformed_text = transformed_text.replace('(', '')
    transformed_text = transformed_text.replace(')', '')
    transformed_text = transformed_text.replace(':', '')
    transformed_text = transformed_text.replace(';', '')
    transformed_text = transformed_text.replace('!', '')
    transformed_text = transformed_text.replace(']', '')
    transformed_text = transformed_text.replace("'", '')
    transformed_text = transformed_text.replace("#", '')



    transformed_text=re.sub(r'"(\d+?),(\d+?)"', r'\1\2', transformed_text)

    # regex to remove commas only between letters
    transformed_text =re.sub(r'([A-Za-z]+),?([A-Za-z]+]?)', r'\1\2', transformed_text)

    # regex to remove fullstop only between letters
    transformed_text =re.sub(r'([A-Za-z]+)\.?([A-Za-z]+]?)', r'\1\2', transformed_text)
    # print transformed_text

    # print transformed_text
    # comma between spaces
    transformed_text =re.sub(r'(\s+),?(\s+]?)', r'\1\2', transformed_text)
    # fullstop between spaces
    transformed_text =re.sub(r'(\s+)\.?(\s+]?)', r'\1\2', transformed_text)


    # comma between letter and spaces
    transformed_text =re.sub(r'([A-Za-z]+),?(\s+]?)', r'\1\2', transformed_text)
    # comma between spaces and letter
    transformed_text =re.sub(r'(\s+),?([A-Za-z]+]?)', r'\1\2', transformed_text)


    # fullstop between letter and spaces
    transformed_text =re.sub(r'([A-Za-z]+)\.?(\s+]?)', r'\1\2', transformed_text)
    # fullstop at end of letter
    transformed_text = re.sub(r'([A-Za-z]+).?(\,]?)', r'\1\2', transformed_text)
    # comme at end of word
    transformed_text = re.sub(r'([A-Za-z]+),?', r'\1', transformed_text)

    # regex to remove commas only between letters
    transformed_text =re.sub(r'([A-Za-z]+),?(\d+?)', r'\1\2', transformed_text)

    # regex to remove fullstop only between letters
    transformed_text =re.sub(r'([A-Za-z]+)\.?(\d+?)', r'\1\2', transformed_text)

    # regex to remove commas only between letters
    transformed_text = re.sub(r'(\d+?),?([A-Za-z]+)', r'\1\2', transformed_text)

    # regex to remove fullstop only between letters
    transformed_text = re.sub(r'(\d+?)\.?([A-Za-z]+)', r'\1\2', transformed_text)
    # print transformed_text
    print 'File data transformed'
    return transformed_text
