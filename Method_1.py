import youtube_dl
import moviepy.editor as mp
import speech_recognition as sr

# YouTube video link
video_url = ""

# Download options
ydl_opts = {
    'format': 'bestaudio/best',  # Download only the audio
    'outtmpl': 'downloaded_video.%(ext)s',
}

# Download the video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# Extract audio
clip = mp.AudioFileClip("downloaded_video.mp4")  # Adjust if the format is different
clip.write_audiofile("extracted_audio.wav")

# Transcription
r = sr.Recognizer()
with sr.AudioFile("extracted_audio.wav") as source:
    audio = r.record(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')  # Brazilian Portuguese
        print(f"Transcription:\n{text}")
        # Save to a .txt file
        with open("transcription.txt", "w", encoding='utf-8') as text_file:
            text_file.write(text)
        print("Transcription saved to 'transcription.txt'")
    except sr.UnknownValueError:
        print("Audio could not be understood")
    except sr.RequestError as e:
        print(f"Error from Google Speech Recognition service; {e}")
