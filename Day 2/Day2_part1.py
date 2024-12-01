import sys


def main(filepath):
    result = 0
    
    with open(filepath) as f:
        line1 = f.readline()
        if line1 != '':
            f.seek(0)
            
            for line in f:
                dimentions = line.split('x')
                if len(dimentions) == 3:
                    l = int(dimentions[0])
                    w = int(dimentions[1])
                    h = int(dimentions[2])

                    lxw = l * w
                    wxh = w * h
                    lxh = l * h
                    
                    result += (2 * (lxw + wxh + lxh) + min(lxw, wxh, lxh))
    
    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(main(sys.argv[1]))
    else:
        print("this programes takes only one argument : the input filepath")