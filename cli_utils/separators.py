def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)


def print_char_separator(char):
    """Print a separator using a custom character."""
    print(char[0] * 30)


def print_custom_separator(char, length):
    """Print a separator with custom character and length."""
    
    if length <= 0:
        print("")
        return

    print(char[0] * length)


def print_labeled_separator(label, char="*", width=30):
    """Print a labeled separator."""
    print(label.center(width, char))


def print_box(message, char="*"):
    """Print text inside a box."""

    width = len(message) + 4
    border = char * width

    print(border)
    print(f"{char} {message} {char}")
    print(border)