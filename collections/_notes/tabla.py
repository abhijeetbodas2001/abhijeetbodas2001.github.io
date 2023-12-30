from dataclasses import dataclass

dha = "धा"
ti = "ति"
Ta = "ट"
dhin = "धिं"
ta = "ता"
na = "ना"
tin = "तिं"
ke = "के"
ge = "गे"
ghe = "घे"


@dataclass
class Palta:
    lines: list[list[str]]

    def __post_init__(self) -> str:
        assert len(self.lines) > 0

    def __str__(self) -> str:
        kayda_string = "<p>"

        for line in self.lines:
            kayda_string = kayda_string + " ".join(line) + "  <br>"

        return kayda_string + "</p>"


@dataclass
class Tihai:
    line: list[str]
    num_non_repeating_bols: int = 4

    def __str__(self) -> str:
        non_repeating = self.line[0 : self.num_non_repeating_bols]
        repeating = self.line[4:]
        tihai_string = ""
        non_repeating_string = ""
        repeating_string = ""

        for i in non_repeating:
            non_repeating_string = non_repeating_string + i + " "
        for i in repeating:
            repeating_string = repeating_string + i + " "

        tihai_string = tihai_string + non_repeating_string + repeating_string + "  <br>"
        for ii in range(0, 2):
            tihai_string = tihai_string + " " * len(non_repeating_string) + repeating_string + "  <br>"

        tihai_string = [tihai_string, tihai_string, tihai_string]
        return "--- Pause ---<br>".join(tihai_string)


@dataclass
class Kayda:
    title: str
    palte: list[Palta]
    tihai: Tihai

    def __str__(self) -> str:
        kayda_string = f'<h1>"{self.title}" कायदा</h1>'
        for palta in self.palte:
            # kayda_string = kayda_string + "## पलटा<br>"
            kayda_string = kayda_string + palta.__str__()
        kayda_string = kayda_string + self.tihai.__str__()
        return kayda_string


ti_kayda = Kayda(
    title=ti,
    palte=[
        Palta(
            lines=[
                [dha, ti, dha, ti, dha, dha, tin, na],
                [ta, ti, ta, ti, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, dha, dha, dha, ti, dha, dha],
                [dha, ti, dha, ti, dha, dha, tin, na],
                [ta, ti, ta, ta, ta, ti, ta, ta],
                [dha, ti, dha, ti, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, dha, ti, dha, ti, dha, dha],
                [dha, ti, dha, ti, dha, dha, tin, na],
                [ta, ti, ta, ti, ta, ti, ta, ta],
                [dha, ti, dha, ti, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, dha, ti, dha, dha, dhin, na],
                [ti, dha, dha, ti, dha, dha, tin, na],
                [ta, ti, ta, ti, ta, ta, tin, na],
                [ti, dha, dha, ti, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dhin, na, ti, dha, dha, ti, dha, dha],
                [dha, ti, dha, ti, dha, dha, tin, na],
                [tin, na, ti, ta, ta, ti, ta, ta],
                [dha, ti, dha, ti, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, dha, ti, dhin, na, ti, dha, dha],
                [dha, ti, dha, ti, dha, dha, tin, na],
                [ta, ta, ti, tin, na, ti, ta, ta],
                [dha, ti, dha, ti, dha, dha, dhin, na],
            ]
        ),
    ],
    tihai=Tihai(line=[dha, ti, dha, ti, dha, dha, tin, na, dha]),
)

tiT_kayda = Kayda(
    title=ti + Ta,
    palte=[
        Palta(
            lines=[
                [dha, dha, ti, Ta, dha, dha, tin, na],
                [ta, ta, ti, Ta, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, dha, ti, Ta, dha, dha, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, tin, na],
                [ta, ta, ti, Ta, ta, ta, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, dha, ti, Ta, ti, Ta, dha, dha],
                [ti, Ta, ti, Ta, dha, dha, tin, na],
                [ta, ta, ti, Ta, ti, Ta, ta, ta],
                [ti, Ta, ti, Ta, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, dha, ti, Ta, ti, Ta, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, tin, na],
                [ta, ta, ti, Ta, ti, Ta, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, tin, na],
                [ta, ti, Ta, ta, ta, ta, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, tin, na],
                [ta, ti, Ta, ta, ta, ta, ti, Ta],
                [ta, ti, Ta, ta, ta, ta, ti, Ta],
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, dhin, na],
            ]
        ),
        Palta(
            lines=[
                [dha, dha, dha, dha, dha, dha, ti, Ta],
                [dha, dha, dha, dha, dha, dha, ti, Ta],
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, tin, na],
                [ta, ta, ta, ta, ta, ta, ti, Ta],
                [ta, ta, ta, ta, ta, ta, ti, Ta],
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, dhin, na],
            ]
        ),
    ],
    tihai=Tihai(line=[dha, dha, ti, Ta, dha, dha, tin, na, dha]),
)

tiTa_dhaGe_tinna_kena_kayda = Kayda(
    title=ti + Ta + " " + dha + ge + " " + tin + na + " " + ke + na,
    palte=[
        Palta(
            lines=[
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ta, ti, Ta, ta, ti, Ta, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ta, ti, Ta, ta, ti, Ta, ta, ta],
                [ta, ti, Ta, ta, ti, Ta, ta, ta],
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ta, ti, Ta, ta, ti, Ta, ta, ta],
                [ta, ti, Ta, ta, ta, ta, ti, Ta],
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [dha, ti, Ta, dha, dha, dha, ti, Ta],
                [dha, dha, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ta, ti, Ta, ta, ti, Ta, ta, ta],
                [ta, ti, Ta, ta, ta, ta, ti, Ta],
                [dha, dha, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, dha, ti, Ta, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ti, Ta, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ta, ti, Ta, ta, ti, Ta, ta, ta],
                [ti, Ta, ta, ke, tin, na, ke, na],
                [ti, Ta, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [ti, Ta, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [dha, dha, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, ta, ke, tin, na, ke, na],
                [ti, Ta, ta, ti, Ta, ta, ta, ta],
                [ti, Ta, ta, ke, tin, na, ke, na],
                [dha, dha, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, dha, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ti, Ta, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ta, ta, ta, ti, Ta, ta, ta, ta],
                [ti, Ta, ta, ke, tin, na, ke, na],
                [ti, Ta, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, dha, dha, ti, Ta, dha, dha, dha, ti, Ta],
                [ti, Ta, dha, dha, ti, Ta],
                [ti, Ta, dha, ti, Ta, ti, Ta, dha, ti, Ta],
                [dha, ge, tin, na, ke, na],
                [ta, ta, ta, ti, Ta, ta, ta, ta, ti, Ta],
                [ti, Ta, ta, ta, ti, Ta],
                [ti, Ta, dha, ti, Ta, ti, Ta, dha, ti, Ta],
                [dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, ti, Ta, dha, ti, Ta, ti, Ta],
                [ti, Ta, dha, dha, ti, Ta],
                [ti, Ta, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, ge, tin, na, ke, na],
                [ta, ti, Ta, ti, Ta, ta, ti, Ta, ti, Ta],
                [ti, Ta, ta, ta, ti, Ta],
                [ti, Ta, dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, ti, Ta, dha, ti, Ta, ti, Ta],
                [dha, dha, ti, Ta, dha, dha, ti, Ta],
                [dha, ti, Ta, ti, Ta, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ta, ti, Ta, ti, Ta, ta, ti, Ta, ti, Ta],
                [ta, ta, ti, Ta, ta, ta, ti, Ta],
                [dha, ti, Ta, ti, Ta, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
        Palta(
            lines=[
                [dha, ti, Ta, dha, dha, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
                [dha, dha, ti, Ta, dha, ti, Ta, ti, Ta, dha],
                [ti, Ta, dha, ge, tin, na, ke, na],
                [ta, ti, Ta, ta, ta, ta],
                [ti, Ta, ta, ke, tin, na, ke, na],
                [dha, dha, ti, Ta, dha, ti, Ta, ti, Ta, dha],
                [ti, Ta, dha, ge, dhin, na, ghe, na],
            ]
        ),
    ],
    tihai=Tihai(
        line=[dha, ti, Ta, dha, ti, Ta, dha, dha, ti, Ta, dha, ge, tin, na, ke, na, dha],
        num_non_repeating_bols=6,
    ),
)

with open("/home/apb/code/abhijeetbodas2001.github.io/collections/_notes/tabla.md", "w") as f:
    f.write("""---
layout: post
title: "Tabla"
---\n\n""")
    f.write("<div style='text-align:center; font-size: 24px; font-weight: 500'>")
    f.write(ti_kayda.__str__())
    f.write(tiT_kayda.__str__())
    f.write(tiTa_dhaGe_tinna_kena_kayda.__str__())
    f.write("</div>")
