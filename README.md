# String Color In Python
```python
def attachColor(color):
    return \
        "\033[0;3" \
        + str(
            ["black", "red", "green", "yellow", "blue", "pink", "cyan", "gray", ]
            .index(color)
        ) \
        + "m"


if __name__ == "__main__":
    for color in ["black", "red", "green", "yellow", "blue", "pink", "cyan", "gray", ]:
        print(attachColor(color) + color.upper())

```
## Colors :

| ColorName | colorName |
| :---: | :---: |
| Black | `black` |
| Red | `red` |
| Green | `green` |
| Blue | `blue` |
| Yellow | `yellow` |
| Pink | `pink` |
| Cyan | `cyan` |
| White | `white` |

```python
\033031m
```

## Method / Function :
+ attach Color  : `attachColor( colorName )`

## How To use :
```python
colorName = "red"
string = "Red" # Red is a String
print( attachColor( colorName ) + string )
```

