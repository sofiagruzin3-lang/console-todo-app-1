# Console To-Do App 📝

A lightweight, reliable, and bulletproof console-based application for managing everyday tasks. Built entirely from scratch as a final graduation project for Month 1 of Python learning.

### 🚀 Key Features & Implementation Details

* **Task Addition with Validation:** Automatically packs user text into dictionary data structures. It strictly prevents adding empty tasks or creating duplicate task names.
* **Smart Dashboard & Statistics:** Displays a clean list of tasks with interactive status icons (`✅` / `❌`). It automatically calculates the real-time completion percentage rounded to one decimal place using the `round()` function.
* **Direct Status Toggling:** Allows users to change a task's status instantly using its list number, leveraging direct index access without running heavy and unnecessary loops.
* **Secure Task Deletion:** Removes elements completely using the `.pop()` method. It prevents invalid negative indexing or zero entries by triggering custom validation chains with the `raise` keyword.
* **Bulletproof Error Handling:** Thanks to robust `try/except` blocks, the application is completely crash-proof. It smoothly intercepts and handles potential user typos like letters instead of digits (`ValueError`) or non-existent task numbers (`IndexError`).

### 🛠️ Technical Stack
* **Language:** Python 3
* **Concepts Used:** Control flow (`while`, `if/elif/else`), Functions (`def`), Data Structures (`list`, `dict`), Exception Handling (`try/except`, `raise`), In-place modification, and built-in helpers (`enumerate()`, `len()`, `round()`, `.strip()`, `.lower()`).

### 💻 How to Run
1. Run the `main.py` file in your terminal.
2. Follow the intuitive text menu instructions to add, view, update, or delete your tasks!
