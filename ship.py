import pygame
from math import *
import sys

screen_width = 500
screen_height = 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Client")

clientNumber = 0

class Ship():
    width = 20
    height = 30
    vel = 3
    angle = 0
    bullet_vel = 10
    bullets = []
    bullet_color = (255, 0, 0)

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def polygon_coordinates(self):      #Calculating the coordinates of the ship hitbox
        coordinates = []
        coordinates.append([self.x, (self.y - self.width)])
        coordinates.append([self.x + self.width, self.y+self.width])
        coordinates.append([self.x - self.width, self.y+self.width])


        hyp = self.width
        back_dim1 = (-self.width, self.width)
        back_dim2 = (-self.width, -self.width)
        angle = self.angle

        front_point = (self.x - self.width*cos(angle), self.y - hyp*sin(angle) )
        back_point1 = (self.x -back_dim1[0]*cos(angle)   + back_dim1[1]*sin(angle) , self.y  - back_dim1[0]*sin(angle) - back_dim1[1]*cos(angle))
        back_point2 = (self.x -back_dim2[0]*cos(angle)   + back_dim2[1]*sin(angle) , self.y  - back_dim2[0]*sin(angle) - back_dim2[1]*cos(angle))


        return (front_point, back_dim1, back_point2)

    def rotate_vector(self, vector, angle):       #Calculating the new coordinates of a rotated vector2
        center = (self.x, self.y)
        new_x = (vector[0]-center[0])*cos(angle) - (vector[1]-center[1])*sin(angle)
        new_y = (vector[0]-center[0])*sin(angle) + (vector[1]-center[1])*cos(angle)
        return [new_x, new_y]



    def draw(self, win):        #This is where drawing the characters happen
        angle = self.angle
        width = self.width
        height = self.height
        hyp = height
        back_dim1 = (-width, width)
        back_dim2 = (-width,-width)

        front_point = (self.x - hyp*cos(angle), self.y - hyp*sin(angle) )
        back_point1 = (self.x -back_dim1[0]*cos(angle)   + back_dim1[1]*sin(angle) , self.y  - back_dim1[0]*sin(angle) - back_dim1[1]*cos(angle))
        back_point2 = (self.x -back_dim2[0]*cos(angle)   + back_dim2[1]*sin(angle) , self.y  - back_dim2[0]*sin(angle) - back_dim2[1]*cos(angle))


        self.coordinates = (front_point, back_point1, back_point2)
        pygame.draw.polygon(win, self.color, self.coordinates)

        for bullet in self.bullets:
            bullet_pos = bullet[0]

            #delete bullet if outside screen. Causes flickering (deleting list while iterating). There's a vid about this (dafluffypotato, removing objects from list)
            if bullet_pos[0] < 0 or bullet_pos[0] > screen_width or bullet_pos[1]<0 or bullet_pos[1]>screen_height:
                self.bullets.remove(bullet)

            bullet_vel = bullet[1]
            bullet_pos[0] += bullet_vel[0]
            bullet_pos[1] += bullet_vel[1]

            print(len(self.bullets))
            pygame.draw.circle(win, self.bullet_color, bullet[0], 10)


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        if pygame.mouse.get_pressed() == (1,0,0):   #if left mouse is clicked
            self.shoot()

        mouse_position = pygame.mouse.get_pos()
        self.angle = atan2(self.y-mouse_position[1], self.x-mouse_position[0])
        

        self.rect = (self.x, self.y, self.width, self.height)


    def shoot(self):
        angle = self.angle
        velocity = (-self.bullet_vel*cos(angle), -self.bullet_vel*sin(angle))                 #normalized, angle
        self.bullets.append(([self.x, self.y], velocity))




def redrawWindow(win,player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    player = Ship(250, 250, (255, 0, 0))
    enemy = Ship(100, 100, (0,255,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        player.move()

        win.fill((255,255,255))
        player.draw(win)
        enemy.draw(win)
        pygame.display.update()
        

main()



######   TODO   #########
"""
features
    ship firing
    health


code style      
    docstring how to
    best practice for self. (self.x self.y )




"""
