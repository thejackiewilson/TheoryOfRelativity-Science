import tkinter as tk
import relativity

class RelativityApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Relativity Time Dilation Calculator")
        
        self.velocity_var = tk.DoubleVar(value=0.9)
        
        velocity_label = tk.Label(text="Velocity as fraction of c:")
        velocity_entry = tk.Entry(textvariable=self.velocity_var)
        
        output_label = tk.Label(text="Time dilation factor:")
        self.output_var = tk.StringVar(value="")
        output_display = tk.Label(textvariable=self.output_var)
        
        calculate_button = tk.Button(text="Calculate", command=self.calculate)
        
        velocity_label.grid(row=0, column=0)
        velocity_entry.grid(row=0, column=1)
        output_label.grid(row=1, column=0)
        output_display.grid(row=1, column=1)
        calculate_button.grid(row=2, column=0, columnspan=2)
        
    def calculate(self):
        velocity = self.velocity_var.get()
        dilation = relativity.time_dilation_factor(velocity)
        self.output_var.set(dilation)
        
if __name__ == "__main__":
    app = RelativityApp()
    app.mainloop()