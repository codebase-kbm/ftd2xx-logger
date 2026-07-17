from model import Module


def validate(module: Module) -> None:
    """
    Validate parsed module.
    Raises RuntimeError if something is inconsistent.
    """

    if not module.functions:
        raise RuntimeError("No functions found.")

    names = set()

    for fn in module.functions:

        if not fn.name:
            raise RuntimeError("Function without name found.")

        if fn.name in names:
            raise RuntimeError(f"Duplicate function '{fn.name}'.")

        names.add(fn.name)

        if fn.ordinal <= 0:
            raise RuntimeError(f"{fn.name}: Invalid ordinal.")

        if fn.return_type is None:
            raise RuntimeError(f"{fn.name}: Missing return type.")

        if fn.calling is None:
            raise RuntimeError(f"{fn.name}: Missing calling convention.")