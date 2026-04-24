# RAG Chunking Strategies

Exploring 4 chunking strategies for RAG pipelines using LangChain.

- **01_fixed_size.py** — splits on character count, fast but context-unaware
- **02_recursive.py** — separator hierarchy, respects document structure
- **03_semantic.py** — embedding-based, splits on meaning shifts
- **04_structural.py** — regex-based, splits on known document headers