import numpy as np
import soundfile as sf

# Percentage of frame overlap
OVERLAP = 50.0

class AudioInput:
    def __init__(self, path: str, frame_size: int) -> None:
        # File attributes
        self.file_path = path
        self.pos = 0

        # Sliding frame attributes
        self.frame_size = frame_size
        self.overlap = OVERLAP / 100.0
        self.slide_amount = int(self.frame_size * self.overlap)

    def get_frame(self) -> np.ndarray:
        with sf.SoundFile(self.file_path, 'r') as f:
            # Read one frame's worth of audio sample
            f.seek(self.pos)
            self.data = f.read(self.frame_size)
            self.data = self.data[:, 0]

            # Slide the frame 
            self.pos = f.tell() - self.slide_amount

        return self.data

    def get_sample_rate(self) -> int:
        with sf.SoundFile(self.file_path, 'r') as f:
            return f.samplerate

    def _display_file_info(self) -> None:
        with sf.SoundFile(self.file_path, 'r') as f:
            print("Information about the file:", self.file_path)
            print("mode", f.mode)
            print("samplerate", f.samplerate)
            print("frames", f.frames)
            print("channels", f.channels)
            print("format", f.format)
            print("subtype", f.subtype)
            print("format info", f.format_info)
            print("extra info", f.extra_info)
            print("seekable()", f.seekable())
