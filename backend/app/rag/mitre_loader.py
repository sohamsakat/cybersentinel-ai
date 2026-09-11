import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

KNOWLEDGE_BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent / "knowledge_base"


def load_mitre_documents() -> Tuple[List[str], List[Dict[str, Any]], List[str]]:
    """
    Loads MITRE ATT&CK and OWASP knowledge files, formats them for semantic vector embedding,
    and returns (documents, metadatas, ids).
    """
    documents: List[str] = []
    metadatas: List[Dict[str, Any]] = []
    ids: List[str] = []

    # 1. Load MITRE ATT&CK Techniques
    mitre_file = KNOWLEDGE_BASE_DIR / "mitre_attack_enterprise.json"
    if mitre_file.exists():
        with open(mitre_file, "r", encoding="utf-8") as f:
            techniques = json.load(f)
            for item in techniques:
                tech_id = item["technique_id"]
                name = item["name"]
                tactic = item["tactic"]
                desc = item["description"]
                detection = item["detection"]
                mitigations = " ".join(item.get("mitigations", []))
                cves = ", ".join(item.get("cve_references", []))

                doc_text = (
                    f"MITRE ATT&CK Technique {tech_id}: {name}\n"
                    f"Tactic: {tactic}\n"
                    f"Description: {desc}\n"
                    f"Detection Criteria: {detection}\n"
                    f"Mitigations: {mitigations}\n"
                    f"Related CVEs: {cves}"
                )
                documents.append(doc_text)
                metadatas.append({
                    "type": "mitre_technique",
                    "technique_id": tech_id,
                    "name": name,
                    "tactic": tactic,
                })
                ids.append(f"mitre_{tech_id}")

    # 2. Load OWASP Top 10
    owasp_file = KNOWLEDGE_BASE_DIR / "owasp_top10.json"
    if owasp_file.exists():
        with open(owasp_file, "r", encoding="utf-8") as f:
            categories = json.load(f)
            for item in categories:
                cat_id = item["category_id"]
                name = item["name"]
                desc = item["description"]
                patterns = ", ".join(item.get("common_patterns", []))
                mitigation = item.get("mitigation", "")

                doc_text = (
                    f"OWASP Vulnerability {cat_id}: {name}\n"
                    f"Description: {desc}\n"
                    f"Common Attack Patterns: {patterns}\n"
                    f"Mitigation: {mitigation}"
                )
                documents.append(doc_text)
                metadatas.append({
                    "type": "owasp_vulnerability",
                    "category_id": cat_id,
                    "name": name,
                })
                ids.append(f"owasp_{cat_id.replace(':', '_')}")

    return documents, metadatas, ids
