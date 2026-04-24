from langchain_community.document_loaders import PyPDFLoader

file_path = "./sample/Ashish_Ubale_AI.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

full_text = " ".join([doc.page_content for doc in docs])

import re

sections = ["SUMMARY", "EDUCATION", "EXPERIENCE", "SKILLS", "PROJECTS"]

def split_resume(docs, sections):
    # Construct regex: (?:^|\n)(SUMMARY|EDUCATION|EXPERIENCE|...)
    pattern = r'(?:\n|^)\s*(?=' + r'|'.join(sections) + r')'
    
    # Split text by section headers
    parts = re.split(pattern, "\n".join([doc.page_content for doc in docs]))
    
    # Structure into dictionary
    section_dict = {}
    for part in parts:
        for section in sections:
            if part.startswith(section):
                # Clean content: remove section header from content
                section_dict[section] = part.replace(section, "", 1).strip()
    return section_dict

parsed_resume = split_resume(docs, sections)

# Structural chunking splits on known document headers using regex
# Most precise for well-structured docs — each section is a complete meaningful unit
# Weakness: brittle — breaks if headers change or PDF formatting shifts
# Best for: resumes, legal contracts, standardized forms