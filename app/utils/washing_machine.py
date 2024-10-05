import time


class WashingMachine:
    def start(self):
        stages = [
            {"status": "Заповнення водою", "duration": 2},
            {"status": "Прання", "duration": 5},
            {"status": "Полоскання", "duration": 3},
            {"status": "Віджимання", "duration": 4},
        ]

        for stage in stages:
            self.state = stage["status"]
            time.sleep(stage["duration"])
            yield {"status": self.state}

        yield {"status": "Цикл прання завершений!"}
