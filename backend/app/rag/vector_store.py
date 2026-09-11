import logging
from typing import Any, Dict, List
import chromadb
from app.core.config import settings
from app.rag.mitre_loader import load_mitre_documents

logger = logging.getLogger(__name__)

_chroma_client = None
_collection = None


def get_chroma_client() -> chromadb.PersistentClient:
    global _chroma_client
    if _chroma_client is None:
        _chroma_client = chromadb.PersistentClient(path=settings.CHROMA_PERSIST_DIR)
    return _chroma_client


def get_mitre_collection():
    global _collection
    if _collection is None:
        client = get_chroma_client()
        _collection = client.get_or_create_collection(name=settings.CHROMA_COLLECTION_NAME)
        # Check if collection is empty, if so populate it
        if _collection.count() == 0:
            logger.info("ChromaDB collection empty. Ingesting MITRE ATT&CK & OWASP knowledge base...")
            docs, metadatas, ids = load_mitre_documents()
            if docs:
                _collection.add(documents=docs, metadatas=metadatas, ids=ids)
                logger.info(f"Successfully indexed {len(docs)} threat intelligence documents in ChromaDB.")
    return _collection


def query_threat_intelligence(query_text: str, n_results: int = 3) -> List[Dict[str, Any]]:
    """
    Performs semantic vector search across MITRE ATT&CK & OWASP knowledge base.
    Returns matched techniques, tactics, descriptions, and similarity distances.
    """
    collection = get_mitre_collection()
    if collection.count() == 0:
        return []

    results = collection.query(
        query_texts=[query_text],
        n_results=min(n_results, collection.count()),
    )

    matched_items = []
    if results and results.get("documents") and results["documents"][0]:
        docs = results["documents"][0]
        metadatas = results["metadatas"][0] if results.get("metadatas") else [{}] * len(docs)
        distances = results["distances"][0] if results.get("distances") else [0.0] * len(docs)
        ids = results["ids"][0] if results.get("ids") else [""] * len(docs)

        for doc, meta, dist, item_id in zip(docs, metadatas, distances, ids):
            matched_items.append({
                "id": item_id,
                "document": doc,
                "metadata": meta,
                "distance": dist,
            })

    return matched_items
