from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

file_path = "./sample/Ashish_Ubale_AI.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

full_text = " ".join([doc.page_content for doc in docs])
print(f"Total characters: {len(full_text)}")

# Split on space so chunk_size (characters) is respected
# Weakness: cuts mid-sentence — no awareness of meaning or structure
text_splitter = CharacterTextSplitter(separator=" ", chunk_size=300, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

print(f"Total chunks: {len(chunks)}")

# Observation: chunks can cut mid-thought (e.g. "including..." with no follow-up)
# This breaks context for RAG retrieval