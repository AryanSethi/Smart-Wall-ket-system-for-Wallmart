import pygame

categories = {
    "Meat and Poultry": (1,1),
    "Soft Drinks": (1,19),
    "Alcohol and spirits": (4,6),
    "Home Items": (9,4),
    "Stationary": (16,6),
    "Sea Food": (13,14),
    "Bakery": (11,14),
    "Frozen": (20,11),
    "Grocery": (20,16),
    "Florist": (10,1)
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
            },            {
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

batched_orders =[]
destinations=[]


for order in all_orders:
    for products in order["products"]:
        batched_orders.append(products["description"])

for product in batched_orders:
    if categories[sub_categories[product]] not in destinations:
        destinations.append(categories[sub_categories[product]])

WIDTH = 22
HEIGHT = 22
BLACK = (0, 0, 0)
BLUE=(0,0,255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
MARGIN = 2
grid = []
for row in range(21):
    grid.append([])
    for column in range(21):
        grid[row].append(0)

# designing the map of one store
                        ##############################
for i in range(17):
    grid[i][0]=4
    grid[i][1]=4     #sides
    grid[i][-1]=4
    grid[i][-2]=4
for i in range(2):
    for j in range(3,18):   #top and bottom
        grid[i][j]=4
        grid[-1][j]=4
for i in range(4,7):
    for j in range(4,14):
        grid[j][i]=4         #middle
        grid[j][i+5]=4
        grid[j][i + 10] = 4
for i in range(16,18):
    for j in range(4,7):
        grid[i][j] = 4      #below middle
        grid[i][j+5] = 4
        grid[i][j+10] = 4

        ##############################
# this marks all the journey destinations we have to cover
for destination in destinations:
    grid[destination[0]][destination[1]]=1

pygame.init()
WINDOW_SIZE = [510, 520]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Store Map")
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     column = pos[0] // (WIDTH + MARGIN)
        #     row = pos[1] // (HEIGHT + MARGIN)
        #     # Set that location to one
        #     grid[row][column] = 3

    screen.fill(BLACK)

    # Draw the grid
    for row in range(21):
        for column in range(21):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            elif grid[row][column] == 2:
                    color = GREEN
            elif grid[row][column] == 3:
                color = BLACK
            elif grid[row][column] == 4:
                color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()