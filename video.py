import math
import cv2


def _get_fps(video):
    major_ver = (cv2.__version__).split('.')[0]
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)

    return math.ceil(fps)


def extract_frames(file, sample_rate=None):
    frames = []
    cap = cv2.VideoCapture(file)
    if not cap.isOpened():
        cap.release()
        return frames

    if not sample_rate:
        sample_rate = _get_fps(cap)

    cur_frame = 0
    while True:
        rval, frame = cap.read()
        if not rval:
            break

        if cur_frame % sample_rate == 0:
            frames.append(frame)

        cur_frame += 1

    cap.release()
    return frames
