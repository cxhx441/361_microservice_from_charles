import rpyc

conn = rpyc.connect("localhost", 18861)  # connect to server

data_1 = ("s", ["01", "02"], [(1.6, 33.2), (82.6, 41.2)], "\033[93m")
data_2 = ("r", ["03", "04"], [(353.2, 112.5), (523.9, 5.3)], "\u001b[34m")

result = conn.root.get_grid(10, data_1, data_2)  # call exposed get_grid method
conn.close()

print("*** Grid ***")
print(result)