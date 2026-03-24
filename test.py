import whisper
import torch
import ffmpeg
import os

def format_timestamp(seconds: float):
    """แปลงวินาทีเป็นรูปแบบ HH:MM:SS"""
    td = int(seconds)
    hours = td // 3600
    minutes = (td % 3600) // 60
    secs = td % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def transcribe_with_timestamps(video_path):
    audio_temp = "timestamp_audio.wav"
    output_txt = "script_with_time.txt"
    device = "cuda"

    # 1. แยกเสียง (Pure & Clean)
    print("--- 1. กำลังสกัดเสียงจากวิดีโอ ---")
    try:
        (
            ffmpeg
            .input(video_path)
            .output(audio_temp, acodec='pcm_s16le', ac=1, ar='16k')
            .overwrite_output()
            .run(quiet=True)
        )
    except Exception as e:
        print(f"Error: {e}")
        return

    # 2. โหลดโมเดล (ใช้ Turbo เพื่อความเร็วและแม่นยำ)
    print(f"--- 2. กำลังโหลดโมเดลเข้า GPU ({torch.cuda.get_device_name(0)}) ---")
    model = whisper.load_model("large-v3-turbo", device=device)

    # 3. เริ่มถอดเสียงพร้อมดึงข้อมูล Segments
    print("--- 3. กำลังถอดเสียงและคำนวณเวลา ---")
    result = model.transcribe(
        audio_temp,
        language="th",
        fp16=True,
        temperature=0,  # บังคับให้ AI ไม่มโน
        beam_size=1,    # ลดอาการวนลูป
        initial_prompt="นี่คือบทสนทนาภาษาไทย มีคำทับศัพท์ภาษาอังกฤษ"
    )

    # 4. บันทึกผลลัพธ์พร้อมเวลาลงไฟล์
    print("--- 4. กำลังบันทึกไฟล์สคริปต์ ---")
    with open(output_txt, "w", encoding="utf-8") as f:
        for segment in result['segments']:
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            text = segment['text'].strip()
            
            # บันทึกในรูปแบบ [00:00:05 -> 00:00:10] ข้อความ...
            f.write(f"[{start} -> {end}] {text}\n")

    # ล้างไฟล์ขยะ
    if os.path.exists(audio_temp):
        os.remove(audio_temp)

    print("-" * 30)
    print(f"✅ เสร็จสมบูรณ์! ไฟล์ของคุณอยู่ที่: {output_txt}")

if __name__ == "__main__":
    transcribe_with_timestamps("test.mp4")