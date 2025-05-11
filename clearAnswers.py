import os
import re

# Define the base path
base_path = r"D:\!!@@Coursera_Deep_Learning\Workspace\feature_master\coursera-deep-learning-specialization"

# Function to process .md files and remove 'x' marks
def remove_correct_answers(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regex to remove '[x]' and replace it with '[ ]'
    updated_content = re.sub(r'\[x\]', '[ ]', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Walk through the directory and process .md files
for root, _, files in os.walk(base_path):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            remove_correct_answers(file_path)

print("Correct answer indications removed from all .md files.")