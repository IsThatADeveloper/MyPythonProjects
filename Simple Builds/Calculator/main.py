import tkinter as tk

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except: 
        clear_field()
        text_result.insert(1.0, "Error")
        pass

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("375x325")

text_result = tk.Text(root, height=2, width=20, font=("Arial", 24))
text_result.grid(columnspan=5)


w = 5
s = 18

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=w, padx=0, pady=0, font=("Arial", s))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=w, padx=0, pady=0, font=("Arial", s))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=w, padx=0, pady=0, font=("Arial", s))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=w, padx=0, pady=0, font=("Arial", s))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=w, padx=0, pady=0, font=("Arial", s))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=w, padx=0, pady=0, font=("Arial", s))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=w, padx=0, pady=0, font=("Arial", s))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=w, padx=0, pady=0, font=("Arial", s))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=w, padx=0, pady=0, font=("Arial", s))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=w, padx=0, pady=0, font=("Arial", s))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=w, padx=0, pady=0, font=("Arial", s))
btn_plus.grid(row=2, column=4)
btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=w, padx=0, pady=0, font=("Arial", s))
btn_subtract.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=w, padx=0, pady=0, font=("Arial", s))
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="÷", command=lambda: add_to_calculation("/"), width=w, padx=0, pady=0, font=("Arial", s))
btn_divide.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=w, padx=0, pady=0, font=("Arial", s))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=w, padx=0, pady=0, font=("Arial", s))
btn_close.grid(row=5, column=3)

btn_clear = tk.Button(root, text="C", command=clear_field, width=11, padx=0, pady=0, font=("Arial", s))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, padx=0, pady=0, font=("Arial", s))
btn_equals.grid(row=6, column=3, columnspan=2)




root.mainloop()