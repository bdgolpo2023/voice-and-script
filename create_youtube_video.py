#!/usr/bin/env python3
"""
Professional YouTube Video Creator
Creates a high-quality video with audio, animated subtitles, and visual effects
Perfect for YouTube content
"""

from moviepy.editor import (
    AudioFileClip, TextClip, CompositeVideoClip, 
    ColorClip, concatenate_videoclips
)
from moviepy.video.tools.subtitles import SubtitlesClip
import pysrt
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Configuration for YouTube
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30
BACKGROUND_COLOR = (10, 20, 40)  # Dark blue professional color
TEXT_COLOR = 'white'
TEXT_SIZE = 70
TEXT_FONT = 'Arial-Bold'
SUBTITLE_POSITION = ('center', 'bottom')

def create_animated_background(duration):
    """Create a professional animated gradient background"""
    def make_frame(t):
        # Create gradient that shifts over time
        y = np.linspace(0, 1, VIDEO_HEIGHT)
        x = np.linspace(0, 1, VIDEO_WIDTH)
        X, Y = np.meshgrid(x, y)
        
        # Animated gradient
        shift = np.sin(t * 0.5) * 0.3
        r = (10 + 30 * (Y + shift)) % 255
        g = (20 + 40 * (Y + shift)) % 255
        b = (40 + 60 * (Y + shift)) % 255
        
        frame = np.dstack([r, g, b]).astype('uint8')
        return frame
    
    from moviepy.editor import VideoClip
    return VideoClip(make_frame, duration=duration)

def parse_srt(srt_file):
    """Parse SRT file and return subtitles"""
    subs = pysrt.open(srt_file, encoding='utf-8')
    return subs

def create_subtitle_clip(txt, start, end):
    """Create a single animated subtitle clip with professional styling"""
    # Create text with shadow effect
    txt_clip = TextClip(
        txt, 
        fontsize=TEXT_SIZE, 
        color=TEXT_COLOR,
        font=TEXT_FONT,
        size=(VIDEO_WIDTH - 200, None),
        method='caption',
        align='center',
        stroke_color='black',
        stroke_width=3
    )
    
    # Position at bottom with padding
    txt_clip = txt_clip.set_position(('center', VIDEO_HEIGHT - 200))
    txt_clip = txt_clip.set_start(start)
    txt_clip = txt_clip.set_end(end)
    txt_clip = txt_clip.set_duration(end - start)
    
    # Add fade in/out animation
    txt_clip = txt_clip.crossfadein(0.3).crossfadeout(0.3)
    
    return txt_clip

def create_youtube_video(audio_file, srt_file, output_file):
    """Create professional YouTube video with all elements"""
    print("🎬 Starting YouTube video creation...")
    
    # Load audio
    print("📻 Loading audio...")
    audio = AudioFileClip(audio_file)
    duration = audio.duration
    
    # Create background
    print("🎨 Creating animated background...")
    background = create_animated_background(duration)
    background = background.set_duration(duration)
    
    # Parse subtitles
    print("📝 Parsing subtitles...")
    subs = parse_srt(srt_file)
    
    # Create subtitle clips
    print("✨ Creating animated subtitles...")
    subtitle_clips = []
    for sub in subs:
        start_time = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds + sub.start.milliseconds / 1000
        end_time = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds + sub.end.milliseconds / 1000
        
        subtitle_clip = create_subtitle_clip(sub.text, start_time, end_time)
        subtitle_clips.append(subtitle_clip)
    
    # Add intro title
    print("🎯 Adding intro title...")
    intro_text = TextClip(
        "Ocean Adventure", 
        fontsize=120, 
        color='white',
        font=TEXT_FONT,
        stroke_color='black',
        stroke_width=5
    )
    intro_text = intro_text.set_position('center')
    intro_text = intro_text.set_duration(3)
    intro_text = intro_text.crossfadein(1).crossfadeout(1)
    
    # Composite all elements
    print("🎞️ Compositing video...")
    video = CompositeVideoClip(
        [background] + [intro_text] + subtitle_clips,
        size=(VIDEO_WIDTH, VIDEO_HEIGHT)
    )
    
    # Add audio
    video = video.set_audio(audio)
    video = video.set_duration(duration)
    
    # Export with YouTube-optimized settings
    print("💾 Exporting video (this may take a few minutes)...")
    video.write_videofile(
        output_file,
        fps=FPS,
        codec='libx264',
        audio_codec='aac',
        bitrate='8000k',
        preset='medium',
        threads=4
    )
    
    print(f"✅ Video created successfully: {output_file}")
    print(f"📊 Duration: {duration:.2f} seconds")
    print(f"📺 Resolution: {VIDEO_WIDTH}x{VIDEO_HEIGHT} @ {FPS}fps")
    print("🎉 Ready to upload to YouTube!")

if __name__ == "__main__":
    # File paths
    audio_file = "ElevenLabs_2026-11-12T12_28_56_Jarnathan - Confident and Versatile_pvc_s50_sim75_v4.mp3"
    srt_file = "ElevenLabs_2026-11-12T12_28_56_Jarnathan_-_Confident_and_Versatile_pvc_s50_sim75_v4_eng.srt"
    output_file = "youtube_video_professional.mp4"
    
    create_youtube_video(audio_file, srt_file, output_file)
