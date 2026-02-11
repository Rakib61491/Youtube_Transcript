import os
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime

def extract_video_id(url):
    parsed = urlparse(url)
    if parsed.netloc == 'youtu.be':
        return parsed.path[1:].split('?')[0]
    if parsed.netloc in ('www.youtube.com', 'youtube.com'):
        if parsed.path == '/watch':
            return parse_qs(parsed.query)['v'][0]
        if parsed.path.startswith('/embed/'):
            return parsed.path.split('/')[2].split('?')[0]
        if parsed.path.startswith('/shorts/'):
            return parsed.path.split('/')[2].split('?')[0]
    return None

def main():
    url = input("Enter YouTube video URL: ").strip()
    video_id = extract_video_id(url)
    
    if not video_id:
        print("Invalid YouTube URL.")
        return
    
    folder = "txt"
    
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created folder '{folder}'")
    
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)
        
        # Convert to plain text
        full_text = " ".join([seg.text for seg in transcript])
        
        # Timestamp filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}.txt"
        filepath = os.path.join(folder, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print(f"Transcript saved to {filepath}")
        print(f"Total segments: {len(transcript)}")
        
    except Exception as e:
        print(f"Error fetching transcript: {e}")

if __name__ == "__main__":
    main()