from model import Argument, Function


def cpp_return(fn: Function) -> str:
    return fn.return_type or "void"


def cpp_calling(fn: Function) -> str:
    return fn.calling or ""


def cpp_typedef_name(fn: Function) -> str:
    return f"PFN_{fn.name}"


def cpp_argument(arg: Argument) -> str:
    return f"{arg.type} {arg.name}"


def cpp_argument_list(fn: Function) -> str:
    if not fn.arguments:
        return "void"

    return ", ".join(cpp_argument(arg) for arg in fn.arguments)


def cpp_argument_names(fn: Function) -> str:
    return ", ".join(arg.name for arg in fn.arguments)


def cpp_typedef(fn: Function) -> str:
    return (
        f"typedef {cpp_return(fn)} "
        f"({cpp_calling(fn)} *{cpp_typedef_name(fn)})"
        f"({cpp_argument_list(fn)});"
    )


def cpp_extern(fn: Function) -> str:
    return f"extern {cpp_typedef_name(fn)} p{fn.name};"


def cpp_variable(fn: Function) -> str:
    return f"{cpp_typedef_name(fn)} p{fn.name} = nullptr;"