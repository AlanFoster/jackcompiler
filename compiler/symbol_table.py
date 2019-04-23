from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional


@dataclass
class SymbolType(Enum):
    LOCAL = 1
    ARGUMENT = 2
    FIELD = 3
    STATIC = 4


@dataclass
class Symbol:
    name: str
    type_name: str
    kind: SymbolType
    number: int = None

    @property
    def segment(self):
        if self.kind == SymbolType.LOCAL:
            return "local"
        elif self.kind == SymbolType.ARGUMENT:
            return "argument"
        else:
            return ValueError(f"No segment for {self.kind}")


@dataclass
class SymbolTable:
    parent: Optional["SymbolTable"]
    symbols: Dict[str, Symbol] = field(default_factory=dict)

    def add(self, symbol: Symbol):
        if symbol.name in self.symbols:
            raise ValueError(f"Duplicate variable {symbol.name} found.")

        symbol.number = sum(v.kind == symbol.kind for k, v in self.symbols.items())
        self.symbols[symbol.name] = symbol

    def get(self, name: str):
        print(self.symbols)

        if name in self.symbols:
            return self.symbols[name]

        if self.parent is None:
            raise ValueError(f"Missing variable '{name}' in current scope.")

        return self.parent.get(name)

    def local_variable_count(self):
        return sum(v.kind == SymbolType.LOCAL for k, v in self.symbols.items())


EmptySymbolTable = SymbolTable(None)
