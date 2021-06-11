def attachColor(color):
    colors = ["black", "red", "green", "blue", "yellow", "pink", "cyan", "white", ]
    return "\033[0;3" + str(colors.index(color)) + "m"

if __name__ == "__main__" :
    colors = ["black", "red", "green", "blue", "yellow", "pink", "cyan", "white", ]
    for color in colors :
        print(attachColor(color) + "Hello")

