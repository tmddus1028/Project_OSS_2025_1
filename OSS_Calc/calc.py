import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 결과 출력 
        self.result_label = tk.Label(root, text="", font=("Arial", 16), anchor="e")
        self.result_label.pack(fill="both", padx=10, pady=5)

        # 버튼 구성 (BIN 추가)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', 'BIN']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.result_label.config(text="")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
                self.result_label.config(text=f"DEC: {result}")
            except Exception:
                self.expression = ""
                self.result_label.config(text="에러")
        elif char == 'BIN':
            try:
                decimal = int(eval(self.expression))
                binary = bin(decimal)[2:]  # '0b' 제거
                self.result_label.config(text=f"BIN: {binary}")
            except Exception:
                self.result_label.config(text="에러")
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
