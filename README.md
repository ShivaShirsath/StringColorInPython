# String Color In Python
```python
def attachColor(color):
    colors = ["black", "red", "green", "blue", "yellow", "pink", "cyan", "white", ]
    return "\033[0;3" + str(colors.index(color)) + "m"

if __name__ == "__main__" :
    colors = ["black", "red", "green", "blue", "yellow", "pink", "cyan", "white", ]
    for color in colors :
        print(attachColor(color) + "Hello")
```
## Colors (color Name) :
+ Black   : `black`
+ Red     : `red`
+ Green   : `green`
+ Blue    : `blue`
+ Yellow  : `yellow`
+ Pink    : `pink`
+ Cyan    : `cyan`
+ White   : `white`

## Method / Function :
+ attach Color  : `attachColor( colorName )`

## How To use :
+ `print( attachColor("red") + "Red", attachColor("yellow") + "Yellow", attachColor("blue") + "Bule")`

