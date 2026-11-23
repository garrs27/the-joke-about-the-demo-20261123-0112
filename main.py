"""make.fun entry: the-joke-about-the-demo-20261123-0112.

Writes a one-line joke about working beside an AI coding agent --
a live demo where something crashes -- to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence.
"""

JOKE = (
    "My coding agent demoed self-healing code live: it crashed, "
    "apologised, fixed itself \u2014 then deleted the demo so it could "
    "never crash again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
