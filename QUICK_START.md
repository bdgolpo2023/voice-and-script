# 🚀 ভিডিও তৈরি করুন - ৩ মিনিটে!

## 📥 Step 1: ফাইল ডাউনলোড করুন

### Option A: Git দিয়ে (সবচেয়ে সহজ)
```bash
git clone https://github.com/bdgolpo2023/voice-and-script.git
cd voice-and-script
```

### Option B: ZIP ডাউনলোড করুন
1. যান: https://github.com/bdgolpo2023/voice-and-script
2. Click করুন: **Code** → **Download ZIP**
3. Unzip করুন এবং folder এ যান

---

## ⚡ Step 2: ভিডিও তৈরি করুন

### 🪟 Windows:

#### পদ্ধতি ১: FFmpeg দিয়ে (fastest)

1. **FFmpeg Install করুন**:
   - Download: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
   - Unzip করুন `C:\ffmpeg`
   - System PATH এ যোগ করুন: `C:\ffmpeg\bin`

2. **CMD বা PowerShell খুলুন** এবং চালান:
```cmd
cd voice-and-script

ffmpeg -f lavfi -i "color=c=0x0f192d:s=1920x1080:r=30" -i "ElevenLabs_2026-11-12T12_28_56_Jarnathan - Confident and Versatile_pvc_s50_sim75_v4.mp3" -vf "subtitles='ElevenLabs_2026-11-12T12_28_56_Jarnathan_-_Confident_and_Versatile_pvc_s50_sim75_v4_eng.srt':force_style='FontName=Arial,FontSize=24,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=1,MarginV=50,Alignment=2'" -shortest -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 youtube_ocean_video.mp4
```

#### পদ্ধতি ২: Python দিয়ে

1. Python 3 install করুন (যদি না থাকে): https://www.python.org/downloads/
2. CMD খুলে চালান:
```cmd
cd voice-and-script
pip install moviepy pysrt
python create_video_simple.py
```

---

### 🍎 macOS:

#### পদ্ধতি ১: FFmpeg দিয়ে (fastest)

1. **Terminal খুলুন** এবং FFmpeg install করুন:
```bash
# Homebrew দিয়ে (recommended)
brew install ffmpeg

# অথবা MacPorts দিয়ে
sudo port install ffmpeg
```

2. **ভিডিও তৈরি করুন**:
```bash
cd voice-and-script
./create_video.sh
```

#### পদ্ধতি ২: Python দিয়ে

```bash
cd voice-and-script
pip3 install moviepy pysrt
python3 create_video_simple.py
```

---

### 🐧 Linux (Ubuntu/Debian):

#### পদ্ধতি ১: FFmpeg দিয়ে (fastest)

```bash
# FFmpeg install করুন
sudo apt-get update
sudo apt-get install ffmpeg

# ভিডিও তৈরি করুন
cd voice-and-script
chmod +x create_video.sh
./create_video.sh
```

#### পদ্ধতি ২: Python দিয়ে

```bash
cd voice-and-script
pip3 install moviepy pysrt
python3 create_video_simple.py
```

---

## 🎯 Output:

✅ **File name**: `youtube_ocean_video.mp4` (FFmpeg) বা `youtube_ocean_story.mp4` (Python)  
✅ **Resolution**: 1920x1080 Full HD  
✅ **Duration**: ~18 seconds  
✅ **Size**: ~2-5 MB  
✅ **Format**: MP4 (YouTube-ready)  

---

## 📤 Step 3: YouTube এ Upload করুন

1. যান: https://studio.youtube.com
2. Click করুন: **CREATE** → **Upload videos**
3. Video file select করুন
4. Title দিন: "Ocean Adventure Story"
5. Description লিখুন
6. Thumbnail add করুন (optional)
7. **Publish** click করুন

---

## 🆘 সমস্যা হচ্ছে?

### FFmpeg not found:
- Windows: PATH ঠিকমত add করেছেন কিনা check করুন
- macOS/Linux: `which ffmpeg` চালিয়ে দেখুন

### Python error:
```bash
# Update pip
pip install --upgrade pip

# Then install again
pip install moviepy pysrt
```

### "Font not found" error:
- FFmpeg command এ `FontName=Arial` কে `FontName=DejaVu-Sans` দিয়ে replace করুন

### Video too large:
- FFmpeg তে `-crf 20` কে `-crf 23` করুন (smaller size)

---

## 💡 Tips:

✨ FFmpeg পদ্ধতি সবচেয়ে দ্রুত (~1-2 মিনিট)  
✨ Python পদ্ধতি সবচেয়ে customizable  
✨ প্রথমবার একটু সময় নিতে পারে  
✨ সব পদ্ধতি একই quality দেয়  

---

## 🎉 সফল!

আপনার প্রফেশনাল ভিডিও তৈরি হয়ে গেছে!  
এখন YouTube এ upload করুন এবং viral হোন! 🚀

---

**প্রশ্ন? সমস্যা?** Issue create করুন: https://github.com/bdgolpo2023/voice-and-script/issues
