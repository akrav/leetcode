import os
import pandas as pd
from collections import defaultdict
import re

def sanitize_filename(filename):
    # Remove invalid characters from filename
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def create_question_folder(row, base_path):
    # Create folder with sanitized title
    folder_name = sanitize_filename(row['title'].strip())
    folder_path = os.path.join(base_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # Handle NaN values
    code = row['code'] if pd.notna(row['code']) else "# Add your solution here"
    question = row['question'] if pd.notna(row['question']) else "Question description not available"
    
    # Create README.md
    readme_content = f"""[Back to Table of Contents](../README.md)

# {row['title']}
Difficulty: {row['difficulty']}

## Question
{question}

## Solution Template
```python
{code}
```
"""
    
    with open(os.path.join(folder_path, 'README.md'), 'w') as f:
        f.write(readme_content)
    
    # Create Python solution file
    with open(os.path.join(folder_path, 'solution.py'), 'w') as f:
        f.write(code)

def create_table_of_contents(df, base_path):
    # Create dictionaries to organize questions by difficulty and category
    by_difficulty = defaultdict(list)
    by_category = defaultdict(lambda: defaultdict(list))
    
    for _, row in df.iterrows():
        if pd.isna(row['title']):  # Skip rows without titles
            continue
            
        title = row['title'].strip()
        difficulty = row['difficulty'] if pd.notna(row['difficulty']) else 'Unknown'
        tags = row['tags'] if pd.notna(row['tags']) else ''
        categories = [tag.strip() for tag in tags.split('&')] if tags else ['Uncategorized']
        
        folder_name = sanitize_filename(title)
        by_difficulty[difficulty].append((title, folder_name))
        
        for category in categories:
            by_category[category][difficulty].append((title, folder_name))
    
    # Create README content
    toc_content = "# LeetCode Questions\n\n"
    
    # Questions by Difficulty
    toc_content += "## Questions by Difficulty\n\n"
    for difficulty in ['Easy', 'Medium', 'Hard', 'Unknown']:
        if difficulty in by_difficulty:
            toc_content += f"### {difficulty}\n\n"
            for title, folder in sorted(by_difficulty[difficulty]):
                toc_content += f"- [{title}](./{folder}/README.md)\n"
            toc_content += "\n"
    
    # Questions by Category
    toc_content += "## Questions by Category\n\n"
    for category in sorted(by_category.keys()):
        toc_content += f"### {category}\n\n"
        for difficulty in ['Easy', 'Medium', 'Hard', 'Unknown']:
            if difficulty in by_category[category]:
                toc_content += f"#### {difficulty}\n\n"
                for title, folder in sorted(by_category[category][difficulty]):
                    toc_content += f"- [{title}](./{folder}/README.md)\n"
                toc_content += "\n"
    
    # Write README.md
    with open(os.path.join(base_path, 'README.md'), 'w') as f:
        f.write(toc_content)

def main():
    # Get the current directory
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Read the CSV file
    df = pd.read_csv('leetcode_template_with_question.csv')
    
    # Create folders and files for each question
    for _, row in df.iterrows():
        if pd.notna(row['title']):  # Skip rows without titles
            create_question_folder(row, base_path)
    
    # Create table of contents
    create_table_of_contents(df, base_path)

if __name__ == "__main__":
    main() 