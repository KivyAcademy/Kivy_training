## https://gist.github.com/Cheaterman/138d3a153c918394ead2d49b0a763d79

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import (
    ListProperty,
    NumericProperty,
)
from kivy.vector import Vector
from kivy.uix.widget import Widget
import random


POOL_SIZE = 30
GENOME_SIZE = 200


class Krokets(App):
    frame_count = NumericProperty()

    def build(self):
        self.target = self.root.ids.target
        Clock.schedule_interval(self.update, 0)
        self.reset()

    def reset(self):
        self.population = None

    def update(self, *args):
        if not self.population:
            self.population = Population()

        self.population.update()
        self.frame_count += 1

        if self.frame_count > GENOME_SIZE:
            self.frame_count = 0
            self.population = Population()


class Population:
    def __init__(self):
        self.rockets = []
        for _ in range(POOL_SIZE):
            rocket = Rocket(center_x=app.root.center_x)
            self.rockets.append(rocket)
            app.root.add_widget(rocket)

    def __del__(self):
        for rocket in self.rockets:
            app.root.remove_widget(rocket)

    def update(self):
        for rocket in self.rockets:
            rocket.update()

    def calculate_fitness(self):
        for rocket in self.rockets:
            rocket.calculate_fitness()
        fitnesses = [rocket.fitness for rocket in self.rockets]
        total_fitness = sum(fitnesses)
        for rocket in self.rockets:
            rocket.fitness /= total_fitness

    def new_generation(self):
        self.mating_pool = []

        for _ in range(POOL_SIZE):
            selected = -1
            selector = random.random()
            while selector > 0:
                selector -= self.rockets[selected].fitness
                selected += 1
            self.mating_pool.append(self.rockets[selected].dna)

    def natural_selection(self):
        mother, father = (random.choice(self.mating_pool) for _ in 'mf')
        mother.crossover(father)


class Rocket(Widget):
    velocity = ListProperty([0, 0])
    acceleration = ListProperty([0, 0])

    def __init__(self, dna=None, **kwargs):
        super(Rocket, self).__init__(**kwargs)
        if not dna:
            self.dna = DNA()
        else:
            self.dna = dna

    def apply_force(self, force):
        self.acceleration = force + self.acceleration

    def update(self):
        if app.frame_count < GENOME_SIZE:
            self.apply_force(self.dna.genes[app.frame_count])
        self.velocity = Vector(self.velocity) + self.acceleration
        self.pos = Vector(self.velocity) + self.pos
        self.acceleration = [0, 0]

    def calculate_fitness(self):
        self.fitness = (
            app.root.width / Vector(self.center).distance(app.target.center)
        )


class DNA:
    def __init__(self, genome=None):
        if genome:
            self.genes = genome
        else:
            self.genes = []
            for _ in range(GENOME_SIZE):
                self.genes.append(
                    Vector((random.random() * 2 - 1 for _ in 'xy')) * .1
                )

    def crossover(self, dna):
        genome = []
        midpoint = random.randrange(0, GENOME_SIZE)
        for index, gene in self.genes:
            if index < midpoint:
                genome.append(gene)
            else:
                genome.append(dna.genes[index])
        return DNA(genome)

    def mutate(self, rate):
        pass  # TODO: WIP


app = Krokets()

if __name__ == '__main__':
    app.run()
