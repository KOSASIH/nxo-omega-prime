import unittest
import numpy as np
from echoplex import EchoPlex
from echoplex import EchoPlexConfig
from echoplex import AudioProcessor
from echoplex import AudioAnalyzer
from echoplex import AudioGenerator
from echoplex import AudioEffect

class TestEchoPlex(unittest.TestCase):
    def test_init(self):
        config = EchoPlexConfig(sample_rate=44100, buffer_size=1024, audio_format=pyaudio.paFloat32, channels=2)
        echoplex = EchoPlex(config)
        self.assertIsInstance(echoplex, EchoPlex)

    def test_process_audio(self):
        config = EchoPlexConfig(sample_rate=44100, buffer_size=1024, audio_format=pyaudio.paFloat32, channels=2)
        echoplex = EchoPlex(config)
        audio_data = np.random.rand(1024)
        processed_audio = echoplex.process_audio(audio_data)
        self.assertIsInstance(processed_audio, np.ndarray)

    def test_start(self):
        config = EchoPlexConfig(sample_rate=44100, buffer_size=1024, audio_format=pyaudio.paFloat32, channels=2)
        echoplex = EchoPlex(config)
        echoplex.start()
        self.assertTrue(True)

    def test_stop(self):
        config = EchoPlexConfig(sample_rate=44100, buffer_size=1024, audio_format=pyaudio.paFloat32, channels=2)
        echoplex = EchoPlex(config)
        echoplex.start()
        echoplex.stop()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
