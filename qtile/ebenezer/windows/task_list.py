import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import json


def get_tasklist():
    """Fetch the current window names from Qtile."""
    try:
        # Get the list of open windows in JSON format
        output = subprocess.check_output(
            ["qtile", "cmd-obj", "-o", "cmd", "-f", "windows"], universal_newlines=True
        )

        output = output.replace("'", '"')
        output = output.replace("False", "false")
        output = output.replace("True", "true")

        # Print the raw output for debugging
        print("Raw output:", output)

        # Parse the JSON output
        windows_info = json.loads(output)

        # Extract window names
        tasklist = [win["id"] for win in windows_info]
        return tasklist
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return []
    except Exception as e:
        print(f"Error fetching task list: {e}")
        return []


def refresh_tasklist():
    """Update the dropdown menu with the current task list."""
    tasklist = get_tasklist()
    combo["values"] = tasklist
    if tasklist:
        combo.current(0)  # Select the first item if available


def on_select(event):
    """Handle selection from the dropdown menu."""
    selected_option = combo.get()
    print(f"Selected: {selected_option}")


def minimize_window():
    """Minimize the selected window."""
    window_id = combo.get()
    print(f"Selected: {window_id}")

    try:
        subprocess.run(
            [
                "qtile",
                "cmd-obj",
                "-o",
                "window",
                "-i",
                str(window_id),
                "-f",
                "toggle_minimize",
            ],
            capture_output=True,
            text=True,
        )
        update_window_list()  # Refresh the list after action
    except Exception as e:
        messagebox.showerror("Error", f"Failed to minimize window: {e}")


def maximize_window():
    """Maximize the selected window."""

    window_id = combo.get()
    print(f"Selected: {window_id}")

    try:
        subprocess.run(
            [
                "qtile",
                "cmd-obj",
                "-o",
                "window",
                "-i",
                str(window_id),
                "-f",
                "toggle_maximize",
            ],
            capture_output=True,
            text=True,
        )
        update_window_list()  # Refresh the list after action
    except Exception as e:
        messagebox.showerror("Error", f"Failed to maximize window: {e}")


def get_qtile_windows():
    # Run the qtile command to list windows
    try:
        result = subprocess.run(
            ["qtile", "cmd-obj", "-o", "group", "-f", "info"],
            capture_output=True,
            text=True,
        )
        output = result.stdout
        return output
    except Exception as e:
        return str(e)


def update_window_list():
    """Refresh the list of windows."""
    windows = get_qtile_windows()

    # Display windows in the listbox
    for window in windows:
        window_name = window.get("name", "Unknown")
        window_id = window["id"]
        print(f"{window_id}: {window_name}")


# Create the main application window
root = tk.Tk()
root.title("Qtile Task List")
root.geometry("400x200")  # Set the window size

# Create a label
label = tk.Label(root, text="Select a window:")
label.pack(pady=10)

# Create a dropdown menu (combobox)
combo = ttk.Combobox(root)
combo.bind("<<ComboboxSelected>>", on_select)  # Bind the select event
combo.pack(pady=20)

# Create a refresh button
refresh_button = tk.Button(root, text="Refresh Task List", command=refresh_tasklist)
refresh_button.pack(pady=10)

minimize_button = tk.Button(root, text="Minimize", command=minimize_window)
minimize_button.pack(pady=10)

maximize_button = tk.Button(root, text="Maximize", command=maximize_window)
maximize_button.pack(pady=10)

# Initialize the task list
refresh_tasklist()

# Start the Tkinter event loop
root.mainloop()
