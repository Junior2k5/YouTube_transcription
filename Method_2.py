import youtube_transcript_api
import speech_recognition as sr

# YouTube video link
video_url = ""

# Get the video ID from the URL
video_id = video_url.split("?v=")[-1]

# Attempt to fetch transcripts directly
try:
    print("Attempting to fetch transcripts using youtube-transcript-api...")
    transcript_list = youtube_transcript_api.YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript(['pt-BR', 'pt'])
    if transcript:
        # Join the text elements
        text = ' '.join(item['text'] for item in transcript.fetch())
        print(f"Transcription:\n{text}")

        # Save to a .txt file
        with open("transcription.txt", "w", encoding='utf-8') as text_file:
            text_file.write(text)
        print("Transcription saved to 'transcription.txt'")
    else:
        print("Brazilian Portuguese transcript not found, falling back to audio method.")

except Exception as e:
    print(f"Error fetching transcripts directly: {e}. Falling back to audio method.")

# Fallback: Audio transcription method if direct fetch fails
if 'text' not in locals():  # Check if we already have a transcript
    print("Using SpeechRecognition for audio transcription...")
    # ... (Insert the download, audio extraction, and transcription code from the previous answer here)
