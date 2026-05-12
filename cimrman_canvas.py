import tkinter as tk


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Cimrman Canvas")
    root.geometry("400x300")

    # Create a canvas
    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    # Print "cimrman" on the canvas
    canvas.create_text(
        200,  # x coordinate (center)
        150,  # y coordinate (center)
        text="cimrman",
        font=("Arial", 32, "bold"),
        fill="blue"
    )

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()
