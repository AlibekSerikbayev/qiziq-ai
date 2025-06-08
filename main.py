import streamlit as st
import tempfile
import random
import os
import requests
from moviepy.editor import VideoFileClip

# Telegram bot sozlamalari
TELEGRAM_BOT_TOKEN = "8082672620:AAEket5zvqNWjBtwGwUMg6uR70wjEEZk_-I"
TELEGRAM_CHAT_ID = "1926076672"

def send_feedback_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

st.set_page_config(page_title="Qiziq Video Klip Kesish", layout="centered")
st.title("🎬 AI yordamida videoning eng qiziq 2 daqiqasi")
st.write("Pastga videoni yuklang. AI uni tahlil qilib, eng qiziq 2 daqiqalik qismini kesib beradi.")

uploaded_file = st.file_uploader("Videoni yuklang (MP4 formatda)", type=["mp4"])

if uploaded_file is not None:
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = os.path.join(tmpdir, "input.mp4")
            output_path = os.path.join(tmpdir, "highlight.mp4")

            # Faylni vaqtinchalik saqlash
            with open(input_path, "wb") as f:
                f.write(uploaded_file.read())

            # Video klipni yuklash
            clip = VideoFileClip(input_path)
            duration = clip.duration

            # 2 daqiqalik segment aniqlash
            start_time = random.uniform(0, max(1, duration - 120))
            end_time = min(start_time + 120, duration)
            subclip = clip.subclip(start_time, end_time)

            # Kesilgan videoni saqlash
            subclip.write_videofile(output_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)

            st.success("✅ Qiziq qism tayyor!")
            st.video(output_path)

            st.write("Bu klip sizga yoqdimi?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("👍 Yoqqan"):
                    send_feedback_to_telegram("✅ Foydalanuvchi klipni yoqtirdi.")
                    st.success("Fikringiz uchun rahmat!")
            with col2:
                if st.button("👎 Yoqmadi"):
                    comment = st.text_area("Iltimos, kamchilik haqida izoh qoldiring:", "")
                    if st.button("Izohni yuborish"):
                        if comment.strip():
                            send_feedback_to_telegram(f"❌ Foydalanuvchiga yoqmadi. Izoh: {comment}")
                            st.warning("Izohingiz yuborildi. Rahmat!")
                        else:
                            st.warning("Iltimos, izoh kiriting!")

    except Exception as e:
        st.error(f"❌ Xatolik yuz berdi: {str(e)}")
        send_feedback_to_telegram(f"❌ Xatolik: {str(e)}")


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
