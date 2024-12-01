import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        # Yield x and y in order to make the object iterable
        yield self.x
        yield self.y
        
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))  # Hash based on (x, y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def main(filepath):
    result = 0
    
    with open(filepath) as f:
        line = f.readline()
        if line != '':
            
            current_house = Point(0, 0)
            
            visited_houses = set(current_house)
            
            for direction in line:
                current_house = Point(current_house.x, current_house.y)
                if direction == '^':
                    current_house.y += 1
                elif direction == 'v':
                    current_house.y -= 1
                elif direction == '>':
                    current_house.x += 1
                elif direction == '<':
                    current_house.x -= 1
                    
                visited_houses.add(current_house)
            
            result = len(visited_houses)
            
    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input filepath")