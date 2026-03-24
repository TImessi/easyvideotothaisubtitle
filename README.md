# 🎙️ easy video to Thai subtitle (GPU nvidia Accelerated)

ระบบถอดเสียงจากวิดีโอเป็นข้อความภาษาไทยและอังกฤษที่มีความแม่นยำสูง โดยใช้พลังประมวลผลจาก GPU (CUDA) เพื่อความรวดเร็วและทำงานแบบ Offline 100%

## ✨ คุณสมบัติเด่น (Features)
- **Fast & Powerful:** ประมวลผลผ่าน GPU ด้วย CUDA 12.6+
- **High Accuracy:** ใช้โมเดล `large-v3-turbo` เพื่อความแม่นยำในภาษาไทยและอังกฤษ
- **Auto Timestamps:** แสดงเวลาเริ่มต้นและสิ้นสุดของแต่ละประโยค [HH:MM:SS]
- **Universal Format:** รองรับทุกนามสกุลวิดีโอผ่าน FFmpeg (mp4, mkv, mov, avi, etc.)
- **Privacy First:** ทำงานแบบ Offline ไม่มีการส่งข้อมูลขึ้นคลาวด์ และฟรี 100%

## 🛠️ ความต้องการของระบบ (Prerequisites)
- **OS:** Windows 10/11
- **Hardware:** NVIDIA GPU (แนะนำ VRAM 8GB+) พร้อมติดตั้ง CUDA 12.4 และ cuDNN 8.9.7
- **Software:** [FFmpeg](https://ffmpeg.org/) (ต้องตั้งค่าใน System Path)

## 🚀 การติดตั้ง (Installation)

1. คลอนโปรเจกต์นี้:
```bash
git clone [https://github.com/TImessi/easyvideotothaisubtitle.git]
cd ชื่อโปรเจกต์ของคุณ