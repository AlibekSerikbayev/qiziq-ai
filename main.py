from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def local_summarize(text):
    inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


# import streamlit as st
# import tempfile
# import os
# import torch
# import whisper
# import requests
# from moviepy.editor import VideoFileClip
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# from transformers import pipeline

# # Telegram sozlamalari
# TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
# TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

# def send_feedback_to_telegram(message):
#     url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
#     data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
#     requests.post(url, data=data)

# # Whisper modelini yuklash (Speech-to-Text)
# whisper_model = whisper.load_model("base")

# # AI Summarization
# summary_pipeline = pipeline("summarization")

# def transcribe_audio(audio_path):
#     result = whisper_model.transcribe(audio_path, language="uz")
#     return result['text']

# def analyze_text_and_get_highlight_time(transcription_text, total_duration):
#     try:
#         summary = summary_pipeline(transcription_text[:1000])[0]['summary_text']
#         start_time = int(total_duration * 0.3)
#         return start_time, min(start_time + 120, int(total_duration))
#     except:
#         return 0, min(120, int(total_duration))

# # Streamlit ilovasi
# st.set_page_config(page_title="AI bilan Qiziq Qism", layout="centered")
# st.title("🎬 AI yordamida eng qiziq 2 daqiqani aniqlash")
# st.markdown("🔊 **Endi matn real ravishda audiodan olinadi!**\n\n🧠 AI matnni tahlil qiladi va video ichidan qiziq joyni topadi.")

# uploaded_file = st.file_uploader("🎥 Videoni yuklang (MP4)", type=["mp4"])

# if uploaded_file:
#     with tempfile.TemporaryDirectory() as tmpdir:
#         try:
#             input_video = os.path.join(tmpdir, "input.mp4")
#             with open(input_video, "wb") as f:
#                 f.write(uploaded_file.read())

#             # Audio chiqarib olish
#             video = VideoFileClip(input_video)
#             audio_path = os.path.join(tmpdir, "audio.wav")
#             video.audio.write_audiofile(audio_path)

#             st.info("🔍 Audio matnga aylantirilmoqda...")
#             transcription = transcribe_audio(audio_path)
#             st.success("✅ Matnga o‘girildi!")
#             st.text_area("🎤 Ajratilgan Matn", transcription[:1000], height=200)

#             start, end = analyze_text_and_get_highlight_time(transcription, video.duration)
#             output_path = os.path.join(tmpdir, "highlight.mp4")
#             ffmpeg_extract_subclip(input_video, start, end, targetname=output_path)

#             st.success(f"🎉 Eng qiziq qism: {start} - {end} sekundlar orasida!")
#             st.video(output_path)

#             st.markdown("## 💬 Fikr bildiring:")
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("👍 Yoqqan"):
#                     send_feedback_to_telegram("✅ Foydalanuvchi klipni yoqtirdi.")
#                     st.success("Rahmat!")
#             with col2:
#                 if st.button("👎 Yoqmadi"):
#                     comment = st.text_area("Kamchilik haqida fikr:", "")
#                     if st.button("Yuborish"):
#                         if comment.strip():
#                             send_feedback_to_telegram(f"❌ Foydalanuvchiga yoqmadi. Izoh: {comment}")
#                             st.warning("Izoh yuborildi!")
#                         else:
#                             st.warning("Iltimos, izoh yozing.")

#         except Exception as e:
#             st.error(f"❌ Xatolik: {str(e)}")
#             send_feedback_to_telegram(f"❌ Xatolik yuz berdi: {str(e)}")


# import streamlit as st
# import tempfile
# import random
# import os
# import requests
# from moviepy.editor import VideoFileClip

# # Telegram bot sozlamalari
# TELEGRAM_BOT_TOKEN = "8082672620:AAEket5zvqNWjBtwGwUMg6uR70wjEEZk_-I"
# TELEGRAM_CHAT_ID = "1926076672"

# def send_feedback_to_telegram(message):
#     url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
#     data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
#     requests.post(url, data=data)

# st.set_page_config(page_title="Qiziq Video Klip Kesish", layout="centered")
# st.title("🎬 AI yordamida videoning eng qiziq 2 daqiqasi")
# st.write("Pastga videoni yuklang. AI uni tahlil qilib, eng qiziq 2 daqiqalik qismini kesib beradi.")

# uploaded_file = st.file_uploader("Videoni yuklang (MP4 formatda)", type=["mp4"])

# if uploaded_file is not None:
#     try:
#         with tempfile.TemporaryDirectory() as tmpdir:
#             input_path = os.path.join(tmpdir, "input.mp4")
#             output_path = os.path.join(tmpdir, "highlight.mp4")

#             # Faylni vaqtinchalik saqlash
#             with open(input_path, "wb") as f:
#                 f.write(uploaded_file.read())

#             # Video klipni yuklash
#             clip = VideoFileClip(input_path)
#             duration = clip.duration

#             # 2 daqiqalik segment aniqlash
#             start_time = random.uniform(0, max(1, duration - 120))
#             end_time = min(start_time + 120, duration)
#             subclip = clip.subclip(start_time, end_time)

#             # Kesilgan videoni saqlash
#             subclip.write_videofile(output_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)

#             st.success("✅ Qiziq qism tayyor!")
#             st.video(output_path)

#             st.write("Bu klip sizga yoqdimi?")
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("👍 Yoqqan"):
#                     send_feedback_to_telegram("✅ Foydalanuvchi klipni yoqtirdi.")
#                     st.success("Fikringiz uchun rahmat!")
#             with col2:
#                 if st.button("👎 Yoqmadi"):
#                     comment = st.text_area("Iltimos, kamchilik haqida izoh qoldiring:", "")
#                     if st.button("Izohni yuborish"):
#                         if comment.strip():
#                             send_feedback_to_telegram(f"❌ Foydalanuvchiga yoqmadi. Izoh: {comment}")
#                             st.warning("Izohingiz yuborildi. Rahmat!")
#                         else:
#                             st.warning("Iltimos, izoh kiriting!")

#     except Exception as e:
#         st.error(f"❌ Xatolik yuz berdi: {str(e)}")
#         send_feedback_to_telegram(f"❌ Xatolik: {str(e)}")


# import streamlit as st
# import tempfile
# import random
# import os
# from moviepy.editor import VideoFileClip

# st.set_page_config(page_title="Qiziq Video Klip Kesish", layout="centered")

# st.title("🎬 AI yordamida videoning eng qiziq 2 daqiqasi")
# st.write("Pastga videoni yuklang. AI uni tahlil qilib, eng qiziq 2 daqiqalik qismini kesib beradi.")

# uploaded_file = st.file_uploader("Videoni yuklang (MP4 formatda)", type=["mp4"])

# if uploaded_file is not None:
#     try:
#         with tempfile.TemporaryDirectory() as tmpdir:
#             input_path = os.path.join(tmpdir, "input.mp4")
#             output_path = os.path.join(tmpdir, "highlight.mp4")

#             # Faylni vaqtinchalik saqlash
#             with open(input_path, "wb") as f:
#                 f.write(uploaded_file.read())

#             # Video klipni yuklash
#             clip = VideoFileClip(input_path)
#             duration = clip.duration

#             # 2 daqiqalik segment aniqlash
#             start_time = random.uniform(0, max(1, duration - 120))
#             end_time = min(start_time + 120, duration)
#             subclip = clip.subclip(start_time, end_time)

#             # Kesilgan videoni saqlash
#             subclip.write_videofile(output_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)

#             st.success("✅ Qiziq qism tayyor!")
#             st.video(output_path)

#     except Exception as e:
#         st.error(f"❌ Xatolik yuz berdi: {str(e)}")

# import streamlit as st
# import tempfile
# import random
# import os
# from moviepy.editor import VideoFileClip
# import imageio
# imageio.plugins.ffmpeg.download()

# st.set_page_config(page_title="Qiziq Video Klip Kesish", layout="centered")

# st.title("🎬 AI yordamida videoning eng qiziq 2 daqiqasi")
# st.write("Pastga videoni yuklang. AI uni tahlil qilib, eng qiziq 2 daqiqalik qismini kesib beradi.")

# uploaded_file = st.file_uploader("Videoni yuklang (MP4 formatda)", type=["mp4"])

# if uploaded_file is not None:
#     with tempfile.TemporaryDirectory() as tmpdir:
#         input_path = os.path.join(tmpdir, "input.mp4")
#         output_path = os.path.join(tmpdir, "highlight.mp4")

#         # Foydalanuvchi yuborgan faylni saqlash
#         with open(input_path, "wb") as f:
#             f.write(uploaded_file.read())

#         # Videoni o‘qish
#         clip = VideoFileClip(input_path)
#         duration = clip.duration

#         # Tasodifiy 2 daqiqalik segment
#         start_time = random.uniform(0, max(1, duration - 120))
#         end_time = min(start_time + 120, duration)
#         subclip = clip.subclip(start_time, end_time)

#         # Foydalanuvchiga chiqariladigan video
#         subclip.write_videofile(output_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)

#         st.success("✅ Qiziq qism tayyor!")
#         st.video(output_path)
