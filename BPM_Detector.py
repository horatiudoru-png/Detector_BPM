import librosa
import numpy as np

def calculeaza_bpm(cale_fisier):
    """
    Încarcă un fișier audio și îi calculează numărul de bătăi pe minut (BPM).
    """
    try:
        
        print("Încărcare melodie... (poate dura câteva secunde)")
        y, sr = librosa.load(cale_fisier, sr=None)
        
        print("Analizez tempo-ul...")
        # Funcția beat_track din librosa folosește algoritmi avansați pentru a estima tempo-ul
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        
       
        if isinstance(tempo, np.ndarray):
            tempo = tempo[0]
            
        return round(tempo, 2)
    
    except Exception as e:
        return f"Eroare la procesarea fișierului: {e}"

if __name__ == "__main__":
    
    cale_audio = r"C:\Horatiu\Python\125bpmc#minor.mp3"
    
    bpm_rezultat = calculeaza_bpm(cale_audio)
    
    if isinstance(bpm_rezultat, (int, float)):
        print(f"\n🎵 Melodia are un tempo de aproximativ: {bpm_rezultat} BPM")
    else:
        print(bpm_rezultat)