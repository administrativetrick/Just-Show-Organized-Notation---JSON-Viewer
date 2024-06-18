import tkinter as tk
from tkinter import ttk, messagebox
import json
import re


class JustShowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Just Show: Organized Notation - JSON Viewer")

        # Create main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input JSON label
        self.input_label = ttk.Label(self.main_frame, text="Input JSON Events:")
        self.input_label.grid(row=0, column=0, sticky=tk.W)

        # Input JSON text box
        self.input_text = tk.Text(self.main_frame, width=50, height=10)
        self.input_text.grid(row=1, column=0, pady=5, sticky=(tk.W, tk.E))

        # Parse button
        self.parse_button = ttk.Button(self.main_frame, text="Parse JSON", command=self.parse_json)
        self.parse_button.grid(row=2, column=0, pady=5)

        # Output JSON label
        self.output_label = ttk.Label(self.main_frame, text="Parsed Events:")
        self.output_label.grid(row=3, column=0, sticky=tk.W)

        # Output JSON text box
        self.output_text = tk.Text(self.main_frame, width=50, height=10, state='disabled')
        self.output_text.grid(row=4, column=0, pady=5, sticky=(tk.W, tk.E))

        # Configure column and row weights
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(4, weight=1)

    def parse_json(self):
        try:
            input_data = self.input_text.get("1.0", tk.END).strip()
            json_data = json.loads(input_data)
            formatted_output = self.format_json(json_data)

            self.output_text.config(state='normal')
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, formatted_output)
            self.output_text.config(state='disabled')
        except json.JSONDecodeError as e:
            messagebox.showerror("Invalid JSON", f"Failed to parse JSON: {e}")

    def format_json(self, json_data):
        formatted_str = ""
        for event in json_data:
            formatted_str += f"Event: {event['event']}\n"
            details = event.get('details', {})
            for key, value in details.items():
                if isinstance(value, dict):
                    formatted_str += f"  {key.capitalize()}:\n"
                    for k, v in value.items():
                        formatted_str += f"    {k.capitalize()}: {v}\n"
                elif isinstance(value, list):
                    formatted_str += f"  {key.capitalize()}:\n"
                    for item in value:
                        formatted_str += f"    - {item['name']}: {item['topic']}\n"
                else:
                    formatted_str += f"  {key.capitalize()}: {value}\n"
            formatted_str += "\n"
        return formatted_str.strip()


if __name__ == "__main__":
    root = tk.Tk()
    app = JustShowApp(root)
    root.mainloop()
