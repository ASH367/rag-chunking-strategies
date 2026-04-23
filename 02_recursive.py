from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = "./sample/Ashish_Ubale_AI.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

full_text = " ".join([doc.page_content for doc in docs])
print(f"Total characters: {len(full_text)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""]
)
chunks = text_splitter.split_documents(docs)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ({len(chunk.page_content)} chars) ---")
    print(chunk.page_content)

print(f"Total chunks: {len(chunks)}")


# Recursive uses separator hierarchy: \n\n → \n → " " → ""
# Better than fixed size but still not meaning-aware
# Can still cut mid-sentence when no separator exists within chunk_size