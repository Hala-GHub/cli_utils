from cli_utils import (
    print_separator,
    print_char_separator,
    print_custom_separator,
    print_labeled_separator,
    print_box,
)

print_separator()
print_char_separator("-")
print_char_separator("=")

print_custom_separator("*", 10)
print_custom_separator("#", 20)

print_labeled_separator("START")
print_labeled_separator("DONE", "-", 40)

print_box("Hello World")