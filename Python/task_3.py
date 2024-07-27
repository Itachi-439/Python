import tkinter as tk
from tkinter import messagebox
import requests

def fetch_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    
    if artist and song:
        url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, data['lyrics'])
        else:
            messagebox.showerror("Error", "Lyrics not found.")
    else:
        messagebox.showwarning("Input Error", "Both fields are required.")

app = tk.Tk()
app.title("Lyrics Fetcher")

tk.Label(app, text="Artist:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(app, text="Song:").grid(row=1, column=0, padx=10, pady=10)

artist_entry = tk.Entry(app)
song_entry = tk.Entry(app)

artist_entry.grid(row=0, column=1, padx=10, pady=10)
song_entry.grid(row=1, column=1, padx=10, pady=10)

fetch_button = tk.Button(app, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

lyrics_text = tk.Text(app, height=10, width=50)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
