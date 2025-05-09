from enum import StrEnum, auto
import sys


class PhysicalKey(StrEnum):
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
    undifined = ""


grafite_keymap = {
    PhysicalKey.q: "b",
    PhysicalKey.w: "l",
    PhysicalKey.e: "d",
    PhysicalKey.r: "w",
    PhysicalKey.t: "z",
    PhysicalKey.y: "'",
    PhysicalKey.u: "f",
    PhysicalKey.i: "o",
    PhysicalKey.o: "u",
    PhysicalKey.p: "j",
    PhysicalKey.a: "n",
    PhysicalKey.s: "r",
    PhysicalKey.d: "t",
    PhysicalKey.f: "s",
    PhysicalKey.g: "g",
    PhysicalKey.h: "y",
    PhysicalKey.j: "h",
    PhysicalKey.k: "a",
    PhysicalKey.l: "e",
    PhysicalKey.semicolon: "l",
    PhysicalKey.z: "q",
    PhysicalKey.x: "x",
    PhysicalKey.c: "m",
    PhysicalKey.v: "c",
    PhysicalKey.b: "v",
    PhysicalKey.n: "k",
    PhysicalKey.m: "p",
    PhysicalKey.comma: ".",
    PhysicalKey.dot: "-",
    PhysicalKey.Q: "B",
    PhysicalKey.W: "L",
    PhysicalKey.E: "D",
    PhysicalKey.R: "W",
    PhysicalKey.T: "Z",
    PhysicalKey.Y: "'",
    PhysicalKey.U: "F",
    PhysicalKey.I: "O",
    PhysicalKey.O: "U",
    PhysicalKey.P: "J",
    PhysicalKey.A: "N",
    PhysicalKey.S: "R",
    PhysicalKey.D: "T",
    PhysicalKey.F: "S",
    PhysicalKey.G: "G",
    PhysicalKey.H: "Y",
    PhysicalKey.J: "H",
    PhysicalKey.K: "A",
    PhysicalKey.L: "E",
    PhysicalKey.colon: "L",
    PhysicalKey.Z: "Q",
    PhysicalKey.X: "X",
    PhysicalKey.C: "M",
    PhysicalKey.V: "C",
    PhysicalKey.B: "V",
    PhysicalKey.N: "K",
    PhysicalKey.M: "P",
}

qwerty_keymap = {
    PhysicalKey.q: "q",
    PhysicalKey.w: "w",
    PhysicalKey.e: "e",
    PhysicalKey.r: "r",
    PhysicalKey.t: "t",
    PhysicalKey.y: "y",
    PhysicalKey.u: "u",
    PhysicalKey.i: "i",
    PhysicalKey.o: "o",
    PhysicalKey.p: "p",
    PhysicalKey.a: "a",
    PhysicalKey.s: "s",
    PhysicalKey.d: "d",
    PhysicalKey.f: "f",
    PhysicalKey.g: "g",
    PhysicalKey.h: "h",
    PhysicalKey.j: "j",
    PhysicalKey.k: "k",
    PhysicalKey.l: "l",
    PhysicalKey.semicolon: ";",
    PhysicalKey.z: "z",
    PhysicalKey.x: "x",
    PhysicalKey.c: "c",
    PhysicalKey.v: "v",
    PhysicalKey.b: "b",
    PhysicalKey.n: "n",
    PhysicalKey.m: "m",
    PhysicalKey.comma: ",",
    PhysicalKey.dot: ".",
    PhysicalKey.Q: "Q",
    PhysicalKey.W: "W",
    PhysicalKey.E: "E",
    PhysicalKey.R: "R",
    PhysicalKey.T: "T",
    PhysicalKey.Y: "Y",
    PhysicalKey.U: "U",
    PhysicalKey.I: "I",
    PhysicalKey.O: "O",
    PhysicalKey.P: "P",
    PhysicalKey.A: "A",
    PhysicalKey.S: "S",
    PhysicalKey.D: "D",
    PhysicalKey.F: "F",
    PhysicalKey.G: "G",
    PhysicalKey.H: "H",
    PhysicalKey.J: "J",
    PhysicalKey.K: "K",
    PhysicalKey.L: "L",
    PhysicalKey.colon: ":",
    PhysicalKey.Z: "Z",
    PhysicalKey.X: "X",
    PhysicalKey.C: "C",
    PhysicalKey.V: "V",
    PhysicalKey.B: "B",
    PhysicalKey.N: "N",
    PhysicalKey.M: "M",
}


def transform_text(text: str, keymap: dict[PhysicalKey, str]) -> str:
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


def get_keymap() -> dict[PhysicalKey, str]:
    args = sys.argv
    if len(args) != 2:
        print("Usage: python main.py <keymap>")
        exit(1)

    keymap = args[1]

    if keymap == "qwerty":
        keymap = qwerty_keymap
    elif keymap == "grafite":
        keymap = grafite_keymap
    else:
        print("Invalid keymap")
        exit(1)
    return keymap


if __name__ == "__main__":
    keymap = get_keymap()
    text = input_text()
    output = transform_text(text, keymap)
    output_text(output)
