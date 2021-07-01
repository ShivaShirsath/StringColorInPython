def attach_color(__color):
    return \
        "\033[0;3" \
        + str(
            ["default", "red", "green", "yellow", "blue", "pink", "cyan", "gray", ]
            .index(color)
        ) \
        + "m"


if __name__ == "__main__":
    for color in ["default", "red", "green", "yellow", "blue", "pink", "cyan", "gray", ]:
        print(attach_color(color) + color.upper())
