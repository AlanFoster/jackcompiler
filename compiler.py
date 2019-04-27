import antlr4
from pathlib import Path
from dataclasses import dataclass
from compiler import compiler
from typing import List, Any
import sys


@dataclass(frozen=True)
class CompileTarget:
    file: Path

    @property
    def output(self):
        return self.file.with_suffix(".vm")


@dataclass(frozen=True)
class Configuration:
    targets: List[CompileTarget]


def parse_argv(argv: List[Any]) -> Configuration:
    input_path = Path(argv[1]).absolute()
    files = [input_path] if input_path.is_file() else list(input_path.glob("*.jack"))
    targets = []
    for path in files:
        targets.append(CompileTarget(file=path))

    return Configuration(targets=targets)


def main(argv: List[Any]) -> None:
    configuration = parse_argv(argv)

    for target in configuration.targets:
        input_stream = antlr4.FileStream(str(target.file))
        result = compiler.generate(input_stream)

        with target.output.open(mode="w") as file:
            file.write(result)


if __name__ == "__main__":
    main(sys.argv)
