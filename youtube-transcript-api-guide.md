# YouTube Transcript API Quick Guide

## Installation
```bash
pip install youtube-transcript-api
# or if you get externally-managed-environment error:
python3 -m pip install --break-system-packages youtube-transcript-api
```

## Key API Details
- The library uses an instance-based approach, not static methods
- You must instantiate `YouTubeTranscriptApi()` first
- The `fetch()` method returns a `FetchedTranscript` object with these attributes:
  - `snippets`: List of transcript segments
  - `language`: Display name of the language
  - `language_code`: ISO language code
  - `is_generated`: Boolean indicating if auto-generated
  - `video_id`: The video ID

## Snippet Structure
Each snippet in `fetched_transcript.snippets` has:
- `start`: Start time in seconds (float)
- `text`: The transcript text
- `duration`: Duration in seconds (float)

## Working Example
```python
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    if 'v=' in url:
        return url.split('v=')[1].split('&')[0]
    elif 'youtu.be/' in url:
        return url.split('youtu.be/')[1].split('?')[0]
    else:
        return url

# Initialize API
api = YouTubeTranscriptApi()

# Fetch transcript
video_id = get_video_id(video_url)
transcript = api.fetch(video_id)

# Access snippets
for snippet in transcript.snippets:
    timestamp = snippet.start  # float in seconds
    text = snippet.text       # string
    duration = snippet.duration  # float in seconds
```

## Common Mistakes to Avoid
1. Don't use `YouTubeTranscriptApi.get_transcript()` - this method doesn't exist
2. Don't use `YouTubeTranscriptApi.fetch()` as a class method - instantiate first
3. Don't try to index snippets with `snippet['start']` - use dot notation: `snippet.start`
4. The API returns snippet objects, not dictionaries

## Time Formatting Helper
```python
def format_time(seconds):
    """Convert seconds to MM:SS format"""
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{minutes:02d}:{secs:02d}"
```