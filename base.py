import pygame
import sys
import ast


categories = {
    "Meat and Poultry": (1, 1),
    "Soft Drinks": (1, 19),
    "Alcohol and spirits": (4, 6),
    "Home Items": (9, 4),
    "Stationary": (16, 6),
    "Sea Food": (13, 14),
    "Bakery": (11, 14),
    "Frozen": (20, 11),
    "Grocery": (20, 16),
    "Florist": (10, 1)
}

sub_categories = {
    "Eggs": "Meat and Poultry",
    "Fresh Cut Chicken": "Meat and Poultry",
    "Fresh Cut Chicken Legs": "Meat and Poultry",
    "Frozen Nuggets": "Frozen",
    "Tide Detergent 2kg": "Home Items",
    "Coka cola 1L bottle": "Soft Drinks",
    "Red bull Energy Drink": "Soft Drinks",
    "Britania eggless cakes": "Bakery",
    "Large size cello tape": "Stationary",
    "Classmate 200 pages register": "Stationary",
    "Reynolds blue gel pens": "Stationary",
}

# 3 hardcoded orders for simplicity, containing 2, 4 and 3 products respectively
all_orders = [
    # order 1 with 2 products
    {
        "products": [
            {
                "description": "Eggs",
                "quantity": 5
            },
            {
                "description": "Tide Detergent 2kg",
                "quantity": 2
            }
        ]
    },

    # order 2 with 4 products
    {
        "products": [
            {
                "description": "Coka cola 1L bottle",
                "quantity": 2
            },
            {
                "description": "Britania eggless cakes",
                "quantity": 10
            }, {
                "description": "Eggs",
                "quantity": 15
            },
            {
                "description": "Red bull Energy Drink",
                "quantity": 10
            }
        ]
    },

    # order 3 with 3 products
    {
        "products": [
            {
                "description": "Large size cello tape",
                "quantity": 1
            },
            {
                "description": "Classmate 200 pages register",
                "quantity": 5
            },
            {
                "description": "Reynolds blue gel pens",
                "quantity": 10
            }
        ]
    },
]

batched_orders = []
destinations = []

for order in all_orders:
    for products in order["products"]:
        batched_orders.append(products["description"])

for product in batched_orders:
    if categories[sub_categories[product]] not in destinations:
        destinations.append(categories[sub_categories[product]])



pygame.init()
WINDOW_SIZE = [850, 850]
vector = pygame.math.Vector2
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Store Map")
done = False
clock = pygame.time.Clock()
background_image = pygame.image.load("new.jpg")

tilesize=10
gridwidth=800
gridheight=770
BLACK=(100,100,100)
WHITE=(255,255,255)
GRAY=(140,140,140)
BLUE=(0,0,230)



class Grid:
    def __init__(self,width,height):
        self.width=width
        self.height= height
        self.walls = []
        self.connections = [vector(1,0),vector(0,1),vector(-1,0),vector(0,-1)]

    def in_bounds(self,node):
        return 0<= node.x < self.width and 0<= node.y <self.height

    def passable(self,node):
        return node not in self.walls

    def find_neighbours(self,node):
        neigbours = [node + connection for connection in self.connections]
        neigbours= filter(self.in_bounds, neigbours)
        neigbours = filter(self.passable, neigbours)
        return neigbours

    def draw_grid(self):
        for x in range(0, self.width,tilesize):
            pygame.draw.line(screen, BLACK, (x, 0), (x, self.height))
        for y in range(0, self.height, tilesize):
            pygame.draw.line(screen, BLACK, (0, y), (self.width, y))

    def draw_wall(self):
        for wall in self.walls:
            rect= pygame.Rect(wall*tilesize,(tilesize,tilesize))
            pygame.draw.rect(screen,BLUE,rect)

g= Grid(gridwidth,gridheight)

background_image.set_alpha(200)
screen.blit(background_image, [0,0])

objects=[]

with open("list.txt", 'r') as f:
    objects = [line.rstrip('\n') for line in f]


while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True

    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         mpos = vector(pygame.mouse.get_pos()) // tilesize
    #         if event.button == 1 or event.button == 2 or event.button == 3:
    #             if mpos in g.walls:
    #                 g.walls.remove(mpos)
    #                 print("mpos is ",mpos," and type is ",type(mpos))
    #             else:
    #                 g.walls.append(mpos)
    #
    #
    # g.draw_wall()


    for string in objects:
        list = ast.literal_eval(string)
        list = pygame.math.Vector2(list)
        rect = pygame.Rect(list * tilesize, (tilesize, tilesize))
        pygame.draw.rect(screen, BLUE, rect)


    g.draw_grid()
    # Limit to 60 frames per second
    clock.tick(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    background_image.set_alpha(200)
    screen.blit(background_image, [0, 0])

pygame.quit()

# with open("list.txt",'w') as f:
#     for w in g.walls:
#         f.write(str(w)+"\n")
