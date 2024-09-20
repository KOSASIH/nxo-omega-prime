import os
import threading
import psutil
from collections import deque

class SpectraOSConfig:
    def __init__(self, os_name, os_version, cpu_architecture, memory_size, disk_space):
        self.os_name = os_name
        self.os_version = os_version
        self.cpu_architecture = cpu_architecture
        self.memory_size = memory_size
        self.disk_space = disk_space

class SpectraOSEvent:
    def __init__(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data

class ProcessManager:
    def __init__(self, config):
        self.config = config
        self.processes = {}

    def create_process(self, process_id, process_name, process_priority):
        self.processes[process_id] = {"name": process_name, "priority": process_priority}

    def terminate_process(self, process_id):
        if process_id in self.processes:
            del self.processes[process_id]

class MemoryManager:
    def __init__(self, config):
        self.config = config
        self.memory_usage = deque(maxlen=100)

    def allocate_memory(self, process_id, memory_size):
        self.memory_usage.append((process_id, memory_size))

    def deallocate_memory(self, process_id, memory_size):
        self.memory_usage.remove((process_id, memory_size))

class FileSystem:
    def __init__(self, config):
        self.config = config
        self.file_system = {}

    def create_file(self, file_name, file_size):
        self.file_system[file_name] = file_size

    def delete_file(self, file_name):
        if file_name in self.file_system:
            del self.file_system[file_name]

class SpectraOS:
    def __init__(self, config):
        self.config = config
        self.process_manager = ProcessManager(config)
        self.memory_manager = MemoryManager(config)
        self.file_system = FileSystem(config)

    def start(self):
        threading.Thread(target=self.monitor_system, args=()).start()

    def stop(self):
        # Implement OS stopping logic here
        pass

    def monitor_system(self):
        while True:
            # Implement system monitoring logic here
            pass

    def handle_event(self, event):
        if event.event_type == "PROCESS_CREATED":
            self.process_manager.create_process(event.event_data["process_id"], event.event_data["process_name"], event.event_data["process_priority"])
        elif event.event_type == "PROCESS_TERMINATED":
            self.process_manager.terminate_process(event.event_data["process_id"])
        elif event.event_type == "MEMORY_ALLOCATED":
            self.memory_manager.allocate_memory(event.event_data["process_id"], event.event_data["memory_size"])
        elif event.event_type == "MEMORY_DEALLOCATED":
            self.memory_manager.deallocate_memory(event.event_data["process_id"], event.event_data["memory_size"])
        elif event.event_type == "FILE_CREATED":
            self.file_system.create_file(event.event_data["file_name"], event.event_data["file_size"])
        elif event.event_type == "FILE_DELETED":
            self.file_system.delete_file(event.event_data["file_name"])
