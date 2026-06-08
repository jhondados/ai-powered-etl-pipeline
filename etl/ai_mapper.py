"""LLM-powered schema mapper."""
from langchain_google_vertexai import ChatVertexAI
import json
from typing import List, Dict

class AISchemaMapper:
    def __init__(self):
        self.llm = ChatVertexAI(model_name="gemini-1.5-flash-002", temperature=0)

    def map_schemas(self, source_columns: List[str], target_columns: List[str]) -> Dict[str, str]:
        prompt = f"""Map source columns to target columns semantically.
Source: {source_columns}
Target: {target_columns}
Return JSON: {{"source_col": "target_col", ...}}
Use null if no match. Consider abbreviations, translations (PT/EN), synonyms."""
        response = self.llm.invoke(prompt)
        return json.loads(response.content)

    def self_heal(self, error: str, code: str) -> str:
        prompt = f"""This ETL code failed with error: {error}
Code: {code}
Fix the issue and return only the corrected code."""
        return self.llm.invoke(prompt).content
