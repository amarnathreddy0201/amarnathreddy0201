import cv2
import time
import os

def record_webcam_in_chunks(
    output_dir="video_chunks",
    chunk_duration=10,
    camera_index=0
):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise RuntimeError("❌ Cannot access webcam.")

    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    print(f"🎥 Webcam opened: {frame_width}x{frame_height} @ {fps} FPS")

    chunk_start_time = time.time()
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    chunk_filename = os.path.join(output_dir, f"chunk_{timestamp}.mp4")
    out = cv2.VideoWriter(chunk_filename, fourcc, fps, (frame_width, frame_height))
    print(f"⏺️ Started: {chunk_filename}")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ Frame read failed. Stopping...")
                break

            current_time = time.time()
            elapsed = current_time - chunk_start_time

            if elapsed >= chunk_duration:
                # Close current chunk
                out.release()
                print(f"✅ Saved: {chunk_filename}")

                # Start next chunk immediately
                chunk_start_time = current_time
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                chunk_filename = os.path.join(output_dir, f"chunk_{timestamp}.mp4")
                out = cv2.VideoWriter(chunk_filename, fourcc, fps, (frame_width, frame_height))
                print(f"⏺️ Started: {chunk_filename}")

            out.write(frame)
            cv2.imshow('Live Recording', frame)

            # Press Q to stop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("🛑 Stopped by user.")
                break

    finally:
        out.release()
        cap.release()
        cv2.destroyAllWindows()
        print("🎬 Webcam released.")
