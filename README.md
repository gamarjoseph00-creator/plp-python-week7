# PLP Python Week 7 — List Operations and Management

## File Descriptions

- **`list_warmup.py`**: Demonstrates basic Python list manipulation, including index access, appending, removing items, and checking list length with `len()`.
- **`shopping_list.py`**: An interactive, menu-driven program that manages a shopping list with a `while` loop and checks for missing items before attempting to remove them.
- **`list_report.py`**: Analyzes a predefined list by generating a numbered report, counting items based on character length, and identifying the longest item name manually using loop comparisons.

## Safety Reflection

Checking whether an item exists with the `in` keyword before calling `.remove()` prevents a `ValueError`. If the item is missing, the program can display a clear message instead of terminating unexpectedly.
