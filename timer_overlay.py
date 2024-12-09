import time
import tkinter as tk

def show_overlay(message):
    """Mostra un overlay con il messaggio specificato."""
    root = tk.Tk()
    root.geometry("200x100+1160+20")  # Posizione in alto a destra per 1360x768
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    label = tk.Label(root, text=message, font=("Helvetica", 12))
    label.pack(expand=True)
    root.after(10000, root.destroy)
    root.mainloop()

def countdown(duration, alert_message):
    """Esegue un conto alla rovescia su una sola riga, poi mostra l'alert."""
    for remaining in range(duration, 0, -1):
        mins, secs = divmod(remaining, 60)
        # Stampa sulla stessa riga, sovrascrivendo il contenuto precedente
        print(f"Tempo rimanente: {mins:02d}:{secs:02d}", end="\r", flush=True)
        time.sleep(1)
    # Una volta terminato il countdown, pulisce la riga corrente
    print(" " * 30, end="\r")  
    # Ora va a capo e mostra il messaggio
    print(alert_message)
    # Mostra l'overlay grafico
    show_overlay(alert_message)

print("Inizia il conto alla rovescia per il primo alert (5 minuti).")
countdown(300, "Sono passati 5 minuti!")

print("Inizia il conto alla rovescia per il secondo alert (12 minuti totali).")
countdown(450, "Sono passati 12 30 minuti!")

