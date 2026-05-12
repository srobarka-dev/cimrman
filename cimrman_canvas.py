import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Cimrman Canvas")
    root.geometry("400x300")

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    text_id = canvas.create_text(
        0,
        0,
        text="cimrman",
        font=("Arial", 32, "bold"),
        fill="blue",
    )

    def center_text(event: tk.Event) -> None:
        canvas.coords(text_id, event.width / 2, event.height / 2)

    canvas.bind("<Configure>", center_text)

    root.mainloop()


if __name__ == "__main__":
    main()
