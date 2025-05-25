import sys
from enum import StrEnum


class InputKey(StrEnum):
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"
    h = "h"
    i = "i"
    j = "j"
    k = "k"
    l = "l"
    m = "m"
    n = "n"
    o = "o"
    p = "p"
    q = "q"
    r = "r"
    s = "s"
    t = "t"
    u = "u"
    v = "v"
    w = "w"
    x = "x"
    y = "y"
    z = "z"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
    I = "I"
    J = "J"
    K = "K"
    L = "L"
    M = "M"
    N = "N"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    U = "U"
    V = "V"
    W = "W"
    X = "X"
    Y = "Y"
    Z = "Z"
    dot = "."
    comma = ","
    semicolon = ";"
    colon = ":"
    dash = "-"
    underscore = "_"
    quote = "'"
    double_quote = '"'
    slash = "/"
    angle_bracket_left = "<"
    angle_bracket_right = ">"
    question_mark = "?"
    undefined = ""


grafite_keymap = {
    InputKey.b: "q",
    InputKey.l: "w",
    InputKey.d: "e",
    InputKey.w: "r",
    InputKey.z: "t",
    InputKey.quote: "y",
    InputKey.f: "u",
    InputKey.o: "i",
    InputKey.u: "o",
    InputKey.j: "p",
    InputKey.n: "a",
    InputKey.r: "s",
    InputKey.t: "d",
    InputKey.s: "f",
    InputKey.g: "g",
    InputKey.y: "h",
    InputKey.h: "j",
    InputKey.a: "k",
    InputKey.e: "l",
    InputKey.i: ";",
    InputKey.q: "z",
    InputKey.x: "x",
    InputKey.m: "c",
    InputKey.c: "v",
    InputKey.v: "b",
    InputKey.k: "n",
    InputKey.p: "m",
    InputKey.dot: ",",
    InputKey.dash: ".",
    InputKey.slash: "/",
    InputKey.B: "Q",
    InputKey.L: "W",
    InputKey.D: "E",
    InputKey.W: "R",
    InputKey.Z: "T",
    InputKey.double_quote: "~",
    InputKey.F: "U",
    InputKey.O: "I",
    InputKey.U: "O",
    InputKey.J: "P",
    InputKey.N: "A",
    InputKey.R: "S",
    InputKey.T: "D",
    InputKey.S: "F",
    InputKey.G: "G",
    InputKey.Y: "H",
    InputKey.H: "J",
    InputKey.A: "K",
    InputKey.E: "L",
    InputKey.I: ";",
    InputKey.Q: "Z",
    InputKey.X: "X",
    InputKey.M: "C",
    InputKey.C: "V",
    InputKey.V: "B",
    InputKey.K: "N",
    InputKey.P: "M",
    InputKey.comma: "<",
    InputKey.underscore: ">",
    InputKey.colon: "?",
}

hyper_keymap = {
    InputKey.p: "q",
    InputKey.c: "w",
    InputKey.l: "e",
    InputKey.m: "r",
    InputKey.v: "t",
    InputKey.x: "y",
    InputKey.u: "u",
    InputKey.o: "i",
    InputKey.y: "o",
    InputKey.f: "p",
    InputKey.n: "a",
    InputKey.s: "s",
    InputKey.r: "d",
    InputKey.t: "f",
    InputKey.d: "g",
    InputKey.dot: "h",
    InputKey.a: "j",
    InputKey.e: "k",
    InputKey.i: "l",
    InputKey.h: ";",
    InputKey.b: "z",
    InputKey.g: "x",
    InputKey.quote: "c",
    InputKey.w: "v",
    InputKey.z: "b",
    InputKey.slash: "n",
    InputKey.comma: "m",
    InputKey.q: ",",
    InputKey.j: ".",
    InputKey.k: "/",
    InputKey.P: "Q",
    InputKey.C: "W",
    InputKey.L: "E",
    InputKey.M: "R",
    InputKey.V: "T",
    InputKey.X: "~",
    InputKey.U: "U",
    InputKey.O: "I",
    InputKey.Y: "O",
    InputKey.F: "P",
    InputKey.N: "A",
    InputKey.S: "S",
    InputKey.R: "D",
    InputKey.T: "F",
    InputKey.D: "G",
    InputKey.angle_bracket_right: "H",
    InputKey.A: "J",
    InputKey.E: "K",
    InputKey.I: "L",
    InputKey.H: ";",
    InputKey.B: "Z",
    InputKey.G: "X",
    InputKey.double_quote: "C",
    InputKey.W: "V",
    InputKey.Z: "B",
    InputKey.question_mark: "N",
    InputKey.angle_bracket_left: "M",
    InputKey.Q: "<",
    InputKey.J: ">",
    InputKey.K: "?",
}

colemak_dh_keymap = {
    InputKey.q: "q",
    InputKey.w: "w",
    InputKey.f: "e",
    InputKey.p: "r",
    InputKey.b: "t",
    InputKey.j: "y",
    InputKey.l: "u",
    InputKey.u: "i",
    InputKey.y: "o",
    InputKey.quote: "p",
    InputKey.a: "a",
    InputKey.r: "s",
    InputKey.s: "d",
    InputKey.t: "f",
    InputKey.g: "g",
    InputKey.m: "h",
    InputKey.n: "j",
    InputKey.e: "k",
    InputKey.i: "l",
    InputKey.o: ";",
    InputKey.z: "z",
    InputKey.x: "x",
    InputKey.c: "c",
    InputKey.d: "v",
    InputKey.v: "b",
    InputKey.k: "n",
    InputKey.h: "m",
    InputKey.comma: ",",
    InputKey.dot: ".",
    InputKey.semicolon: "/",
    InputKey.Q: "Q",
    InputKey.W: "W",
    InputKey.F: "E",
    InputKey.P: "R",
    InputKey.B: "T",
    InputKey.J: "Y",
    InputKey.L: "U",
    InputKey.U: "I",
    InputKey.Y: "O",
    InputKey.double_quote: "P",
    InputKey.A: "A",
    InputKey.R: "S",
    InputKey.S: "D",
    InputKey.T: "F",
    InputKey.G: "G",
    InputKey.M: "H",
    InputKey.N: "J",
    InputKey.E: "K",
    InputKey.I: "L",
    InputKey.O: ";",
    InputKey.Z: "Z",
    InputKey.X: "X",
    InputKey.C: "C",
    InputKey.D: "V",
    InputKey.V: "B",
    InputKey.K: "N",
    InputKey.H: "M",
    InputKey.angle_bracket_left: "<",
    InputKey.angle_bracket_right: ">",
    InputKey.question_mark: "?",
}

qwerty_keymap = {
    InputKey.q: "q",
    InputKey.w: "w",
    InputKey.e: "e",
    InputKey.r: "r",
    InputKey.t: "t",
    InputKey.y: "y",
    InputKey.u: "u",
    InputKey.i: "i",
    InputKey.o: "o",
    InputKey.p: "p",
    InputKey.a: "a",
    InputKey.s: "s",
    InputKey.d: "d",
    InputKey.f: "f",
    InputKey.g: "g",
    InputKey.h: "h",
    InputKey.j: "j",
    InputKey.k: "k",
    InputKey.l: "l",
    InputKey.semicolon: ";",
    InputKey.z: "z",
    InputKey.x: "x",
    InputKey.c: "c",
    InputKey.v: "v",
    InputKey.b: "b",
    InputKey.n: "n",
    InputKey.m: "m",
    InputKey.comma: ",",
    InputKey.dot: ".",
    InputKey.Q: "Q",
    InputKey.W: "W",
    InputKey.E: "E",
    InputKey.R: "R",
    InputKey.T: "T",
    InputKey.Y: "Y",
    InputKey.U: "U",
    InputKey.I: "I",
    InputKey.O: "O",
    InputKey.P: "P",
    InputKey.A: "A",
    InputKey.S: "S",
    InputKey.D: "D",
    InputKey.F: "F",
    InputKey.G: "G",
    InputKey.H: "H",
    InputKey.J: "J",
    InputKey.K: "K",
    InputKey.L: "L",
    InputKey.colon: ":",
    InputKey.Z: "Z",
    InputKey.X: "X",
    InputKey.C: "C",
    InputKey.V: "V",
    InputKey.B: "B",
    InputKey.N: "N",
    InputKey.M: "M",
}


def transform_text(text: str, keymap: dict[InputKey, str]) -> str:
    output = ""
    for char in text:
        if char in keymap:
            output += keymap[char]
        else:
            output += char
    return output


def input_text() -> str:
    return input("Enter text: ")


def output_text(text: str) -> None:
    print(text)


def get_keymap() -> dict[InputKey, str]:
    args = sys.argv
    if len(args) != 2:
        print("Usage: python main.py <keymap>")
        exit(1)

    keymap = args[1]

    match keymap:
        case "qwerty":
            return qwerty_keymap
        case "grafite":
            return grafite_keymap
        case "dh":
            return colemak_dh_keymap
        case "hyper":
            return hyper_keymap
        case _:
            print("Invalid keymap")
            exit(1)


if __name__ == "__main__":
    keymap = get_keymap()
    text = input_text()
    output = transform_text(text, keymap)
    output_text(output)
