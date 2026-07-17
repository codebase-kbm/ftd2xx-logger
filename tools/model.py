from dataclasses import dataclass, field


@dataclass
class Argument:
    type: str
    name: str


@dataclass
class Function:
    name: str
    ordinal: int = 0
    hint: int = 0
    rva: int = 0

    return_type: str | None = None
    calling: str | None = None

    arguments: list[Argument] = field(default_factory=list)


@dataclass
class Module:
    name: str
    functions: list[Function] = field(default_factory=list)