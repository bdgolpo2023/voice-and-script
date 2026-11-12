#!/bin/bash
# Professional YouTube Video Creator using FFmpeg
# Creates 1080p video with burned-in subtitles

set -e

echo "🎬 Creating professional YouTube video..."

# Input files
AUDIO="ElevenLabs_2026-11-12T12_28_56_Jarnathan - Confident and Versatile_pvc_s50_sim75_v4.mp3"
SUBTITLE="ElevenLabs_2026-11-12T12_28_56_Jarnathan_-_Confident_and_Versatile_pvc_s50_sim75_v4_eng.srt"
OUTPUT="youtube_ocean_video.mp4"

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ Error: ffmpeg is not installed"
    echo "📦 Install it with:"
    echo "   Ubuntu/Debian: sudo apt-get install ffmpeg"
    echo "   macOS: brew install ffmpeg"
    echo "   Windows: Download from https://ffmpeg.org/download.html"
    exit 1
fi

echo "📻 Audio file: $AUDIO"
echo "📝 Subtitle file: $SUBTITLE"
echo "💾 Output: $OUTPUT"

# Create video with professional settings
echo "🎞️ Processing video..."

ffmpeg -y \
  -f lavfi -i "color=c=0x0f192d:s=1920x1080:r=30" \
  -i "$AUDIO" \
  -vf "subtitles='$SUBTITLE':force_style='FontName=Arial,FontSize=24,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=1,MarginV=50,Alignment=2'" \
  -shortest \
  -c:v libx264 \
  -preset medium \
  -crf 20 \
  -pix_fmt yuv420p \
  -c:a aac \
  -b:a 192k \
  -ar 48000 \
  "$OUTPUT"

if [ $? -eq 0 ]; then
    echo "✅ Video created successfully!"
    echo "📺 File: $OUTPUT"
    echo "📊 Resolution: 1920x1080 (Full HD)"
    echo "🎉 Ready to upload to YouTube!"
    
    # Show file info
    if command -v ffprobe &> /dev/null; then
        echo ""
        echo "📹 Video Information:"
        ffprobe -v error -show_entries format=duration,size,bit_rate -of default=noprint_wrappers=1 "$OUTPUT"
    fi
else
    echo "❌ Error creating video"
    exit 1
fi
