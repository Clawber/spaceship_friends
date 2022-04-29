import pygame, sys

class Vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __abs__(self):
        return (self.x ** 2+ self.y ** 2)**.5

    def __add__(self, vectorB):
        a = Vector2(self.x+vectorB.x, self.y+ vectorB.y)
        return a

    def __iadd__(self, vectorB):      
        self = self+vectorB
        return self
    
    def __mul__(self, scalar):
        return Vector2(self.x*scalar, self.y*scalar)
        

    # def __getitem__(self, key):
    #     vector = [self.x, self.y]
    #     return vector[key]

class Particle():
    def __init__(self, position, velocity, radius, color=(255,255,255), gravity=0.1):
        self.position = Vector2(position[0], position[1])
        self.velocity = Vector2(velocity[0], velocity[1])
        self.radius = radius
        self.time = radius
        self.color = color
        self.gravity = gravity

    def render(self, screen):
        self.velocity.y += self.gravity 
        self.position = self.position +  self.velocity
        self.time += -.1
        pygame.draw.circle((screen), 
                self.color,
                [int(self.position.x), int(self.position.y)], 
                int(self.time))

def DrawParticles(particles, screen):
    for particle in particles[-1:0:-1]:
        particle.render(screen)
        if particle.radius <= 0:
            particles.remove(particle)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)

