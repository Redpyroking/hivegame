import pygame
import time
import threading

class Timer:
    def __init__(self, waitTime) -> None:
        self.waitTime = waitTime/1000
        self.time = pygame.time.Clock()
        self.thread = None
    
    def countdown(self):
        while self.waitTime >= 0:
            time.sleep(0.001)
            self.waitTime -= 0.001

    def timeout(self):
        if self.waitTime <= 0:
            if self.thread and self.thread.is_alive():
                self.thread.join()
            return True
        return False
    
    def start(self):
        thread = threading.Thread(target=self.countdown)
        thread.start()
