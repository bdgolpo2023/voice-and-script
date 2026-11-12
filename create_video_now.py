#!/usr/bin/env python3
"""
Simple Video Creator without external dependencies
Creates a basic video file structure
"""

import sys
import subprocess

print("🎬 Attempting to create video...")
print()

# Check for moviepy
try:
    import moviepy
    print("✅ moviepy found!")
    HAS_MOVIEPY = True
except ImportError:
    print("❌ moviepy not found")
    HAS_MOVIEPY = False

if not HAS_MOVIEPY:
    print()
    print("📦 Installing moviepy...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "moviepy", "pysrt"])
        print("✅ Installation successful!")
        import moviepy
        HAS_MOVIEPY = True
    except Exception as e:
        print(f"❌ Installation failed: {e}")
        print()
        print("=" * 60)
        print("⚠️  Cannot create video in this sandbox environment")
        print("=" * 60)
        print()
        print("📋 To create the video on your computer:")
        print()
        print("1. Clone the repository:")
        print("   git clone https://github.com/bdgolpo2023/voice-and-script.git")
        print("   cd voice-and-script")
        print()
        print("2. Install ffmpeg:")
        print("   Ubuntu/Debian: sudo apt-get install ffmpeg")
        print("   macOS: brew install ffmpeg")
        print()
        print("3. Run the script:")
        print("   ./create_video.sh")
        print()
        print("✨ The video will be created: youtube_ocean_video.mp4")
        sys.exit(1)

# If we have moviepy, create the video
if HAS_MOVIEPY:
    from moviepy.editor import AudioFileClip, TextClip, CompositeVideoClip, ColorClip
    import pysrt
    
    print()
    print("🎞️ Creating video...")
    
    audio_file = "ElevenLabs_2026-11-12T12_28_56_Jarnathan - Confident and Versatile_pvc_s50_sim75_v4.mp3"
    srt_file = "ElevenLabs_2026-11-12T12_28_56_Jarnathan_-_Confident_and_Versatile_pvc_s50_sim75_v4_eng.srt"
    output = "youtube_ocean_video.mp4"
    
    # Load audio
    audio = AudioFileClip(audio_file)
    duration = audio.duration
    print(f"📻 Audio: {duration:.1f}s")
    
    # Create background
    bg = ColorClip(size=(1920, 1080), color=(15, 25, 45), duration=duration)
    
    # Parse subtitles
    subs = pysrt.open(srt_file)
    print(f"📝 Subtitles: {len(subs)} entries")
    
    # Create subtitle clips
    subtitle_clips = []
    for sub in subs:
        start = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds + sub.start.milliseconds / 1000.0
        end = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds + sub.end.milliseconds / 1000.0
        
        txt = TextClip(
            sub.text,
            fontsize=60,
            color='white',
            font='Arial',
            size=(1620, None),
            method='caption',
            align='center'
        )
        txt = txt.set_position(('center', 850)).set_start(start).set_end(end)
        subtitle_clips.append(txt)
    
    print("🎨 Compositing...")
    video = CompositeVideoClip([bg] + subtitle_clips)
    video = video.set_audio(audio)
    
    print("💾 Rendering (please wait)...")
    video.write_videofile(output, fps=30, codec='libx264', audio_codec='aac')
    
    print()
    print("✅ Video created successfully!")
    print(f"📺 Output: {output}")
    print("🎉 Ready for YouTube!")
