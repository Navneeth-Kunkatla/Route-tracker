###
### Author: Navneeth Mohan Kunkatla
### Class: CSc 110
### Description: A program that navigates based on the user input
###              around the University of Arizona campus

from graphics import graphics
import campus

def get_locations():
    '''
    This function's job is to load in the path file.
    The function will prompt the user for a file name, and then loac those
    contents into a a 2D list.
    Each row of the list represents one of the locations along the path.
    Each inner list will have three elements - the x coordinate, the y
    coordinate and lastly the name of the location.
    '''
    path = input('Path file name: ')
    path_file = open(path, 'r')
    locations = []
    for line in path_file:
        sp = line.split(' - ')
        loc = sp[1].split(',')
        locations.append([int(loc[0]), int(loc[1]), sp[0]])
    return locations

### This function navigates the next point hence routes the path
def navigation(x, y, dest_x, dest_y):
    if x == dest_x and y == dest_y:
        return False, []

    if dest_x - x >= 0:
        if dest_y - y > 0:
            if dest_x - x == 0:
                return True, [(x, y+1), (x+1, y+1), (x-1, y+1)]
            else:
                return True, [(x+1, y+1), (x, y+1), (x+1, y)]
        else:
            if dest_x - x == 0:
                return True, [(x, y-1), (x+1, y-1), (x-1, y-1)]
            else:
                return True, [(x+1, y-1), (x, y-1), (x+1, y)]
    else:
        if dest_y - y > 0:
            return True, [(x-1, y+1), (x, y+1), (x-1, y)]
        else:
            return True, [(x-1, y-1), (x, y-1), (x-1, y)]

### The main function, taking in the mapping detail and executing the functions and drawing the path hence creating the map

def main():
    gui = graphics(1000, 560, "the path finder")
    pi = gui.image(0, 0, 1, 1, "campus.gif")
    gui.update_frame(100)
    locations = get_locations()
    gui.ellipse(locations[0][0], locations[0][1], 12, 12, '#003399')
    gui.text(locations[0][0], locations[0][1], locations[0][2], '#003399', 20)
    # TODO: You, the student, should take over from here!
    campus_grid = campus.campus_grid
    for i in range(len(locations) -1):
        if i > 0:
            gui.ellipse(locations[i][0], locations[i][1], 12, 12, '#003399')
            gui.text(locations[i][0], locations[i][1], locations[i][2], '#003399', 20)
        x = locations[i][0]
        y = locations[i][1]
        dest_x = locations[i+1][0]
        dest_y = locations[i+1][1]
        T = True
        while T:
            T, possible_move = navigation(x, y, dest_x, dest_y)
            if T:
                for element in possible_move:
                    if campus_grid[element[1]][element[0]] == " ":
                        gui.line(x,y,element[0] ,element[1],'red')
                        gui.update_frame(100)
                        x = element[0]
                        y = element[1]
                        if x == dest_x and y == dest_y:
                            gui.ellipse(locations[-1][0], locations[-1][1], 12, 12, '#003399')
                            gui.text(locations[-1][0], locations[-1][1], locations[-1][2], '#003399', 20)
                        break

main()