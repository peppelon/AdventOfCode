
def operation(variable: str, inputs: list[str]) -> int:
    if variable in memory:
        return memory[variable]

    result = 0
    inputs_len = len(inputs)
    if inputs_len == 3:
        left_val =  int(inputs[0]) if inputs[0].isnumeric() else operation(inputs[0], circuit[inputs[0]])
        right_val =  int(inputs[2]) if inputs[2].isnumeric() else operation(inputs[2], circuit[inputs[2]])
        match(inputs[1]):
            case "OR":
                result = left_val | right_val
            case "AND":
                result = left_val & right_val
            case "RSHIFT":
                result = left_val >> right_val
            case "LSHIFT":
                result = left_val << right_val
    elif inputs_len == 2:
        right_val =  int(inputs[1]) if inputs[1].isnumeric() else operation(inputs[1], circuit[inputs[1]])
        result = ~right_val
    else: # inputs_len == 1
        left_val =  int(inputs[0]) if inputs[0].isnumeric() else operation(inputs[0], circuit[inputs[0]])
        result = left_val

    memory[variable] = result
    return result

for filename in ["data1.txt", "data2.txt"]:
    with open(filename, 'r') as data:
        circuit = {}
        memory = {}
        
        for line in data.readlines():
            inputs, output = line.strip().split(" -> ")
            circuit[output] = inputs.split(" ")

        val = operation("a", circuit["a"])
        if val < 0:
            val = 66535 + val + 1
        print(val)
        

           
        
