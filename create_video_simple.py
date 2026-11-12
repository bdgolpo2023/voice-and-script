#!/usr/bin/env python3
"""
Simple but Professional YouTube Video Creator
Requires: moviepy (pip install moviepy)
"""

from moviepy.editor import AudioFileClip, TextClip, CompositeVideoClip, ColorClip
import pysrt

# YouTube HD settings
WIDTH = 1920
HEIGHT = 1080
FPS = 30

def create_video(audio_file, srt_file, output_file):
    """Create professional video with audio and subtitles"""
    
    print("🎬 Creating YouTube video...")
    
    # Load audio
    audio = AudioFileClip(audio_file)
    duration = audio.duration
    print(f"📻 Audio duration: {duration:.2f}s")
    
    # Create solid color background (professional dark blue)
    background = ColorClip(
        size=(WIDTH, HEIGHT),
        color=(15, 25, 45),
        duration=duration
    )
    
    # Parse subtitles
    subs = pysrt.open(srt_file, encoding='utf-8')
    print(f"📝 Found {len(subs)} subtitle entries")
    
    # Create subtitle clips
    subtitle_clips = []
    for i, sub in enumerate(subs):
        # Calculate time in seconds
        start = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds + sub.start.milliseconds / 1000.0
        end = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds + sub.end.milliseconds / 1000.0
        
        # Create text clip with professional styling
        txt_clip = TextClip(
            sub.text,
            fontsize=65,
            color='white',
            font='Arial-Bold',
            size=(WIDTH - 300, None),
            method='caption',
            align='center',
            stroke_color='black',
            stroke_width=2
        )
        
        # Position and timing
        txt_clip = txt_clip.set_position(('center', HEIGHT - 250))
        txt_clip = txt_clip.set_start(start).set_end(end)
        txt_clip = txt_clip.crossfadein(0.2).crossfadeout(0.2)
        
        subtitle_clips.append(txt_clip)
        print(f"  ✓ Subtitle {i+1}/{len(subs)} processed")
    
    # Combine everything
    print("🎞️ Compositing video...")
    final = CompositeVideoClip([background] + subtitle_clips)
    final = final.set_audio(audio)
    final = final.set_duration(duration)
    
    # Export with YouTube settings
    print("💾 Exporting (this will take a few minutes)...")
    final.write_videofile(
        output_file,
        fps=FPS,
        codec='libx264',
        audio_codec='aac',
        bitrate='5000k',
        preset='medium'
    )
    
    print(f"✅ Done! Video saved as: {output_file}")
    print(f"📺 Resolution: {WIDTH}x{HEIGHT} @ {FPS}fps")
    print("🎉 Ready for YouTube!")

if __name__ == "__main__":
    create_video(
        "ElevenLabs_2026-11-12T12_28_56_Jarnathan - Confident and Versatile_pvc_s50_sim75_v4.mp3",
        "ElevenLabs_2026-11-12T12_28_56_Jarnathan_-_Confident_and_Versatile_pvc_s50_sim75_v4_eng.srt",
        "youtube_ocean_story.mp4"
    )
