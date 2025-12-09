from logic.components.component import Component
import time
import threading
import math
import struct

try:
    import simpleaudio as sa
    _HAS_SIMPLEAUDIO = True
except Exception:
    _HAS_SIMPLEAUDIO = False


class Alarm(Component):
    def __init__(self, volume: int = 50, frequency: int = 440):
        super().__init__()

        self.__is_on = False
        self.__volume = max(0, min(100, volume))
        self.__frequency = frequency if frequency > 0 else 440
        self.last_trigger_time = None

        # playback thread controls
        self._play_thread = None
        self._stop_event = threading.Event()

    @property
    def is_on(self):
        return self.__is_on

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value: int):
        self.__volume = max(0, min(100, int(value)))

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value: int):
        if value > 0:
            self.__frequency = int(value)

    def turn_on(self):
        """Turn the alarm on and start playback in a separate thread."""
        if self.__is_on:
            return
        self.__is_on = True
        self.last_trigger_time = time.time()
        self._stop_event.clear()
        self._play_thread = threading.Thread(target=self._play_loop, daemon=True)
        self._play_thread.start()

    def turn_off(self):
        """Turn the alarm off and stop playback."""
        if not self.__is_on:
            return
        self.__is_on = False
        self._stop_event.set()
        if self._play_thread is not None:
            self._play_thread.join(timeout=1.0)
            self._play_thread = None

    def _play_loop(self):
        """Loop that generates and plays tone chunks while the alarm is on."""
        sample_rate = 44100
        duration = 0.2  # seconds per chunk
        while not self._stop_event.is_set():
            buf = self._generate_tone(self.__frequency, self.__volume, duration, sample_rate)
            if _HAS_SIMPLEAUDIO:
                try:
                    play_obj = sa.play_buffer(buf, 1, 2, sample_rate)
                    # wait_done will block the thread until the fragment finishes
                    play_obj.wait_done()
                except Exception:
                    # If playback fails, avoid crashing and sleep briefly
                    time.sleep(duration)
            else:
                # Fallback: log to console (install simpleaudio for real audio)
                print(f"[Alarm] playing {self.__frequency} Hz at vol {self.__volume}")
                time.sleep(duration)

    def _generate_tone(self, freq: int, volume: int, duration: float, sample_rate: int) -> bytes:
        """Generate a 16-bit PCM mono buffer containing a sine wave.

        Avoids external dependencies by using math and struct.
        """
        n_samples = int(sample_rate * duration)
        max_amp = int(32767 * (max(0, min(100, volume)) / 100.0))
        buf = bytearray()
        for i in range(n_samples):
            t = i / sample_rate
            sample = int(max_amp * math.sin(2 * math.pi * freq * t))
            buf += struct.pack('<h', sample)
        return bytes(buf)

    def draw(self, canvas):
        color = "red" if self.__is_on else "gray"
        size = 40

        x, y = self.position_x, self.position_y
        self.obj = canvas.create_oval(x, y, x + size, y + size, fill=color, width=2)
        canvas.create_text(x + 20, y + 55, text=f"Alarm {self.id}", font=("Arial", 10))

    def __str__(self):
        return f"Alarm(id={self.id}, on={self.is_on}, volume={self.volume}, freq={self.frequency})"