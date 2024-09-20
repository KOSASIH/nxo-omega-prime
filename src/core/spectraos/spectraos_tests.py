import unittest
import os
from spectraos import SpectraOS
from spectraos import SpectraOSConfig
from spectraos import SpectraOSEvent
from spectraos import ProcessManager
from spectraos import MemoryManager
from spectraos import FileSystem

class TestSpectraOS(unittest.TestCase):
    def test_init(self):
        config = SpectraOSConfig(os_name="SpectraOS", os_version="1.0", cpu_architecture="x86_64", memory_size=1024, disk_space=10240)
        spectraos = SpectraOS(config)
        self.assertIsInstance(spectraos, SpectraOS)

    def test_create_process(self):
        config = SpectraOSConfig(os_name="SpectraOS", os_version="1.0", cpu_architecture="x86_64", memory_size=1024, disk_space=10240)
        spectraos = SpectraOS(config)
        spectraos.process_manager.create_process("process1", "MyProcess", 10)
        self.assertIn("process1", spectraos.process_manager.processes)

    def test_allocate_memory(self):
        config = SpectraOSConfig(os_name="SpectraOS", os_version="1.0", cpu_architecture="x86_64", memory_size=1024, disk_space=10240)
        spectraos = SpectraOS(config)
        spectraos.memory_manager.allocate_memory("process1", 1024)
        self.assertEqual(spectraos.memory_manager.memory_usage[-1], ("process1", 1024))

    def test_create_file(self):
        config = SpectraOSConfig(os_name="SpectraOS", os_version="1.0", cpu_architecture="x86_64", memory_size=1024, disk_space=10240)
        spectraos = SpectraOS(config)
        spectraos.file_system.create_file("file1.txt", 1024)
        self.assertIn("file1.txt", spectraos.file_system.file_system)

if __name__ == "__main__":
    unittest.main()
