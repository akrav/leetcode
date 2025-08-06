import os
import pandas as pd
from collections import defaultdict
import re
import shutil

def sanitize_filename(filename):
    # Remove invalid characters and extra whitespace from filename
    filename = str(filename).strip()
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Remove multiple spaces
    filename = re.sub(r'\s+', ' ', filename)
    return filename

def encode_path_for_markdown(path):
    # Split the path into directory parts
    parts = path.split('/')
    # Replace spaces with %20 in each part
    encoded_parts = [part.replace(' ', '%20') for part in parts]
    # Join back with forward slashes
    return '/'.join(encoded_parts)

def create_question_folder(row, base_path, questions_dir):
    # Skip if title is missing or empty
    if pd.isna(row['title']) or not row['title'].strip():
        return None
        
    # Create folder with sanitized title
    folder_name = sanitize_filename(row['title'].strip())
    folder_path = os.path.join(questions_dir, folder_name)
    
    try:
        os.makedirs(folder_path, exist_ok=True)
        
        # Handle NaN values
        code = row['code'] if pd.notna(row['code']) else "# Add your solution here"
        question = row['question'] if pd.notna(row['question']) else "Question description not available"
        
        # Create README.md
        readme_content = f"""[Back to Table of Contents](../../README.md)

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
            
        return folder_name
    except Exception as e:
        print(f"Error creating folder for {folder_name}: {str(e)}")
        return None

def create_table_of_contents(df, base_path, questions_dir):
    # Get list of actual folders in the questions directory
    actual_folders = {d for d in os.listdir(questions_dir) 
                     if os.path.isdir(os.path.join(questions_dir, d))}
    
    # Create dictionaries to organize questions by difficulty and category
    by_difficulty = defaultdict(list)
    by_category = defaultdict(lambda: defaultdict(list))
    
    # Create a mapping of sanitized titles to actual folder names
    folder_map = {}
    for folder in actual_folders:
        sanitized = sanitize_filename(folder)
        folder_map[sanitized] = folder
    
    for _, row in df.iterrows():
        if pd.isna(row['title']):  # Skip rows without titles
            continue
            
        title = row['title'].strip()
        sanitized_folder = sanitize_filename(title)
        
        # Only include questions whose folders actually exist
        if sanitized_folder not in folder_map:
            continue
            
        actual_folder = folder_map[sanitized_folder]
        difficulty = row['difficulty'] if pd.notna(row['difficulty']) else 'Unknown'
        tags = row['tags'] if pd.notna(row['tags']) else ''
        categories = [tag.strip() for tag in tags.split('&')] if tags else ['Uncategorized']
        
        by_difficulty[difficulty].append((title, actual_folder))
        
        for category in categories:
            by_category[category][difficulty].append((title, actual_folder))
    
    # Create README content
    toc_content = "# LeetCode Questions\n\n"
    
    # Questions by Difficulty
    toc_content += "## Questions by Difficulty\n\n"
    for difficulty in ['Easy', 'Medium', 'Hard', 'Unknown']:
        if difficulty in by_difficulty:
            toc_content += f"### {difficulty}\n\n"
            for title, folder in sorted(by_difficulty[difficulty]):
                encoded_path = encode_path_for_markdown(f"./Questions/{folder}/README.md")
                toc_content += f"- [{title}]({encoded_path})\n"
            toc_content += "\n"
    
    # Questions by Category
    toc_content += "## Questions by Category\n\n"
    for category in sorted(by_category.keys()):
        toc_content += f"### {category}\n\n"
        for difficulty in ['Easy', 'Medium', 'Hard', 'Unknown']:
            if difficulty in by_category[category]:
                toc_content += f"#### {difficulty}\n\n"
                for title, folder in sorted(by_category[category][difficulty]):
                    encoded_path = encode_path_for_markdown(f"./Questions/{folder}/README.md")
                    toc_content += f"- [{title}]({encoded_path})\n"
                toc_content += "\n"
    
    # Write README.md
    with open(os.path.join(base_path, 'README.md'), 'w') as f:
        f.write(toc_content)

def main():
    # Get the current directory
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Create Questions directory
    questions_dir = os.path.join(base_path, 'Questions')
    os.makedirs(questions_dir, exist_ok=True)
    
    # Move existing question folders to Questions directory
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and item != '.git' and item != 'Questions':
            target_path = os.path.join(questions_dir, item)
            if not os.path.exists(target_path):
                shutil.move(item_path, target_path)
    
    # Read the CSV file
    df = pd.read_csv('leetcode_template_with_question.csv')
    
    # Create folders and files for each question
    for _, row in df.iterrows():
        create_question_folder(row, base_path, questions_dir)
    
    # Create table of contents
    create_table_of_contents(df, base_path, questions_dir)

if __name__ == "__main__":
    main() 