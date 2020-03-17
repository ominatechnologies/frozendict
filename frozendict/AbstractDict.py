from __future__ import annotations

from typing import (AbstractSet, ValuesView,
                    Optional, TypeVar, Tuple)

from typing_extensions import Protocol, runtime_checkable

T = TypeVar('T', covariant=True)
S = TypeVar('S')


@runtime_checkable
class AbstractDict(Protocol[S, T]):
    def __contains__(self, item): ...

    def keys(self) -> AbstractSet[S]: ...

    def items(self) -> AbstractSet[Tuple[S, T]]: ...

    def values(self) -> ValuesView[T]: ...

    def get(self, k: S) -> Optional[T]: ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...
