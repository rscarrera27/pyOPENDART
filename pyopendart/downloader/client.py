from dataclasses import dataclass
from typing import Sequence

import requests
from furl import furl


class Filling:
    def __init__(self, filling_information: dict):
        self._filling_information = filling_information

    def _build_document_url(self, dcm_no: str, ele_id: str, offset: str, length: str):
        return furl(
            "http://dart.fss.or.kr/report/viewer.do",
            query_params={
                "rcpNo": self._filling_information["self"]["rcpNo"],
                "dcmNo": dcm_no,
                "eleId": ele_id,
                "offset": offset,
                "length": length,
            },
        ).tostr()

    def _modify_toc(self, toc_item: dict) -> dict:
        children = toc_item.get("children")
        new_children = []

        if children:
            for c_page in children:
                new_children.append(self._modify_toc(c_page))

        return {
            **toc_item,
            "documentUrl": self._build_document_url(
                toc_item["dcmNo"], toc_item["eleId"], toc_item["offset"], toc_item["length"]
            ),
            "children": new_children,
        }

    @property
    def table_of_contents(self) -> Sequence[dict]:
        toc = [self._modify_toc(p) for p in self._filling_information.get("toc", [])]
        return toc

    @property
    def attached_documents(self) -> Sequence["Filling"]:
        att_docs = [Filling(att_doc) for att_doc in self._filling_information.get("att", [])]
        return att_docs

    @property
    def available_downloads(self) -> Sequence[dict]:
        return []
