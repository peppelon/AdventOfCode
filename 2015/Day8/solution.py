print(sum(len(s.strip()) - len(eval(s)) for s in open('data.txt')))
print(sum(len(s.strip().replace("\\","\\\\").replace("\"", "\\\"")) + 2 - len(s.strip()) for s in open('data.txt')))