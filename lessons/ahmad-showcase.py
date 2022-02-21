import random

dino: str = "\U0001F996"
other_dino: str = "\U0001F995"

dinosaurs: list[str] = list()

while len(dinosaurs) == 0 or dinosaurs[len(dinosaurs) - 1] != 1:
    dinosaurs.append(randint(dino, other_dino))
