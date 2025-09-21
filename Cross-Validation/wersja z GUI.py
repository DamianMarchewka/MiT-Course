import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from collections import defaultdict

# Klasa do reprezentowania pojedynczego wpisu temperatury
class TempDatum:
    def __init__(self, s):
        info = s.split(',')
        self.high = float(info[1])
        self.year = int(info[2][:4])
    def getHigh(self):
        return self.high
    def getYear(self):
        return self.year

# Wczytywanie danych z pliku
def getTempData(filename):
    data = []
    with open(filename) as inFile:
        next(inFile)  # pomiń nagłówek
        for line in inFile:
            if line.strip():
                data.append(TempDatum(line))
    return data

# Oblicz średnie roczne
def getYearlyMeans(data):
    years = defaultdict(list)
    for d in data:
        years[d.getYear()].append(d.getHigh())
    return {y: sum(vals)/len(vals) for y, vals in years.items()}

# Funkcja R-kwadrat
def r_squared(y_true, y_pred):
    y_mean = np.mean(y_true)
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    ss_res = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))
    return 1 - ss_res / ss_tot

# Główna klasa GUI
class TempApp:
    def __init__(self, master):
        self.master = master
        master.title("Temperature Model Viewer")

        # Przycisk do ładowania pliku
        self.load_button = tk.Button(master, text="Load CSV File", command=self.load_file)
        self.load_button.pack()

        # Menu wyboru stopnia wielomianu
        self.degree_var = tk.IntVar(value=1)
        tk.Label(master, text="Select Polynomial Degree:").pack()
        for i in (1, 2, 3):
            tk.Radiobutton(master, text=f"Degree {i}", variable=self.degree_var, value=i).pack()

        # Przycisk do wyświetlania wykresu
        self.plot_button = tk.Button(master, text="Plot", command=self.plot)
        self.plot_button.pack()

        # Miejsce na wykres
        self.canvas_frame = tk.Frame(master)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        self.data = None
        self.canvas = None

    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filename:
            self.data = getTempData(filename)
            self.years_data = getYearlyMeans(self.data)
            tk.messagebox.showinfo("Loaded", f"Loaded {len(self.data)} entries.")

    def plot(self):
        if not self.data:
            tk.messagebox.showerror("Error", "No data loaded.")
            return

        xVals = sorted(self.years_data)
        yVals = [self.years_data[year] for year in xVals]

        # Model
        deg = self.degree_var.get()
        model = np.polyfit(xVals, yVals, deg)
        y_pred = np.polyval(model, xVals)
        r2 = r_squared(yVals, y_pred)

        # Rysowanie wykresu
        fig, ax = plt.subplots()
        ax.plot(xVals, yVals, 'bo', label='Actual Data')
        ax.plot(xVals, y_pred, 'r-', label=f'Degree {deg} Fit\n$R^2$ = {r2:.4f}')
        ax.set_xlabel('Year')
        ax.set_ylabel('Mean Daily High (°C)')
        ax.set_title('Temperature Trends')
        ax.legend()

        # Wyświetlenie na tkinterze
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = TempApp(root)
    root.mainloop()
