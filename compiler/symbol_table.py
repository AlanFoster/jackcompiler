from abc import abstractmethod
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
        if self.kind is SymbolType.LOCAL:
            return "local"
        elif self.kind is SymbolType.ARGUMENT:
            return "argument"
        elif self.kind is SymbolType.FIELD:
            return "this"
        else:
            raise ValueError(f"No segment for {self.kind}")


class SymbolTable:
    @abstractmethod
    def add(self, symbol: Symbol):
        raise NotImplementedError()

    @abstractmethod
    def get(self, name: str):
        raise NotImplementedError()

    @abstractmethod
    def enter_scope(self):
        raise NotImplementedError()

    @abstractmethod
    def exit_scope(self):
        raise NotImplementedError()

    @abstractmethod
    def field_variable_count(self):
        raise NotImplementedError()

    @abstractmethod
    def local_variable_count(self):
        raise NotImplementedError()


class EmptySymbolTable(SymbolTable):
    def add(self):
        raise NotImplementedError()

    def get(self, name):
        raise ValueError(f"Missing variable '{name}'.")

    def enter_scope(self):
        return ChildSymbolTable(self)

    def exit_scope(self):
        raise NotImplementedError()

    def field_variable_count(self):
        return 0

    def local_variable_count(self):
        return 0


@dataclass
class ChildSymbolTable(SymbolTable):
    parent: Optional[SymbolTable]
    symbols: Dict[str, Symbol] = field(default_factory=dict)

    def add(self, symbol: Symbol):
        if symbol.name in self.symbols:
            raise ValueError(f"Duplicate variable {symbol.name} found.")

        symbol.number = sum(v.kind is symbol.kind for k, v in self.symbols.items())
        self.symbols[symbol.name] = symbol

    def get(self, name: str):
        if name in self.symbols:
            return self.symbols[name]

        return self.parent.get(name)

    def enter_scope(self):
        return ChildSymbolTable(self)

    def exit_scope(self):
        return self.parent

    def field_variable_count(self):
        return sum(v.kind is SymbolType.FIELD for k, v in self.symbols.items()) + self.parent.field_variable_count()

    def local_variable_count(self):
        return sum(v.kind is SymbolType.LOCAL for k, v in self.symbols.items())
