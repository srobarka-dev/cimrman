import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Cimrman Canvas")
    root.geometry("400x300")

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas.create_text(
        200,
        150,
        text="cimrman",
        font=("Arial", 32, "bold"),
        fill="blue",
    )

    root.mainloop()


if __name__ == "__main__":
    main()
