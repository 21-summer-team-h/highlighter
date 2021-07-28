from scipy.io import wavfile
import webrtcvad
import moviepy.editor as mp
import numpy as np

vad = webrtcvad.Vad()
vad.set_mode(1) # 1~3 설정

class Frame(object):
    def __init__(self, bytes, timestamp, duration):
        self.bytes = bytes
        self.timestamp = timestamp
        self.duration = duration

def frame_generator(frame_duration, audio, sample_rate):
    frames = []
    n = int(sample_rate * (frame_duration / 1000.0) * 2) # frame (chunk) size = 60ms
    offset = 0
    timestamp = 0.0
    duration = (float(n) / sample_rate)
    while offset + n < len(audio):
        frames.append(Frame(audio[offset:offset + n], timestamp, duration))
        timestamp += duration
        offset += n
    
    # 60ms -> 480 samples = 1 frame
    # 1초 -> 17 frame 정도,,
    return frames

def voice_detection(video, start, end):

    wavclip = "./wavclip.wav"

    sound = mp.AudioFileClip(video)
    soundclip = sound.subclip(start, end)
    soundclip.write_audiofile(wavclip, 8000, 2, 2000,"pcm_s16le")
    #sampling rate = 8000 , sampling bit = 16

    sample_rate, samples = wavfile.read(wavclip)

    frame_duration = 30  # 10/20/30 ms
    frames = frame_generator(frame_duration, samples, sample_rate)
    isspeaking = [] # 초 단위
    sum = 0

    for i, frame in enumerate(frames):
        if i % 17 == 0:
            if (sum > 15) : 
                isspeaking.append(1)
            else :
                isspeaking.append(0)
            sum = 0

        if vad.is_speech(frame.bytes, sample_rate):
            sum += 1

    start = 0
    end = 0
    i = 0
    while True:
        if (isspeaking[i]==0 and isspeaking[i+1]==isspeaking[i+2]==1):
            start = i
            break
        i += 1

    i = len(isspeaking)-1
    while True:
        if (isspeaking[i]==0 and isspeaking[i-1]==isspeaking[i-2]==1):
            end = i
            break
        i -= 1
 
    return start, end