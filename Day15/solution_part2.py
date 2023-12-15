testing = False

def hash(label):
    hash = 0
    for c in label:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash

def focusing_power(boxes):
    power = 0
    for box_num, lenses in enumerate(boxes):
        for lens_num, lens in enumerate(lenses):
            power += (box_num + 1) * (lens_num + 1) * int(lens.split(' ')[1])

    return power

boxes = [[] for i in range(256)]
with open("test.txt" if testing else "file.txt", "r") as file:
    for word in file.readline().strip().split(','):
        chars = word
        if '-' in chars:
            label = chars[:-1]
            box_idx = hash(label)
            for idx, lens in enumerate(boxes[box_idx]):
                if label in lens:
                    boxes[box_idx].pop(idx)
        else:
            label, focal_length = chars.split('=')
            box_idx = hash(label)

            label_found = False
            for idx, lens in enumerate(boxes[box_idx]):
                if label in lens:
                    boxes[box_idx][idx] = f"{label} {focal_length}"
                    label_found = True
                    break
            if not label_found:
                boxes[box_idx].append(f"{label} {focal_length}")


print(focusing_power(boxes))