"""Provides shared components for models functionality"""

from dataclasses import asdict
from typing import Any, TypedDict

from .data import Data


class BaseModel:
    """
    Serves as basis to creating application models
    """

    _collection: str
    _doc: dict[str, Any]
    _diff: dict[str, Any]

    @classmethod
    def from_doc(cls, doc: dict[str, Any], /):
        """
        Factory for new instance from data doc
        """

        c = cls(**{k: v for k, v in doc.items() if k != "_id"})
        c._doc = doc
        return c

    @property
    def uid(self) -> str:
        """
        Shorthand property for _doc[_id]
        """

        return str(self._doc["_id"])

    def __setattr__(self, name, value):
        if getattr(self, "_doc", None):
            if not getattr(self, "_diff", None):
                super().__setattr__("_diff", {})
            self._diff[name] = value
        super().__setattr__(name, value)

    async def _pre_insert(self):
        pass

    async def _on_insert(self):
        pass

    async def _on_insert_failure(self, e: Exception):
        pass

    async def _pre_update(self):
        pass

    async def _on_update(self):
        pass

    async def _on_update_failure(self, e: Exception):
        pass

    async def save(self):
        """
        Save current model. If new, it would be inserted. If current it would be updated
        """

        if getattr(self, "_doc", None):
            if not getattr(self, "_diff", None):
                raise Exception("No changes to save")
            # Update mode
            await self._pre_update()
            try:
                await Data.update(
                    collection=self._collection, uids=(self.uid,), doc=self._diff
                )
            except Exception as e:
                await self._on_update_failure(e)
                raise e

            await self._on_update()
            self._diff = {}
            return self

        await self._pre_insert()
        try:
            self._doc = {
                "_id": await Data.insert(collection=self._collection, doc=asdict(self))
            }
        except Exception as e:
            await self._on_insert_failure(e)
            raise e

        await self._on_insert()
        return self


class AttrLocale(TypedDict, total=False):
    """
    Provides type-hint for Localized string value in models
    """

    en_GB: str
    ar_AE: str


class AttrGeoJSON(TypedDict, total=False):
    """
    Provides type-hint for GeoJSON value in models
    """

    type: str
    coordinates: list[int]
