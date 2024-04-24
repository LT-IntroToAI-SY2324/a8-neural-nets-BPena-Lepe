from neural import *

# print("<<<<<<<<<<<<<< XOR >>>>>>>>>>>>>>\n")
# xor= NeuralNet(2, 2, 1)
# XOR_Data=[
# ([0,0], [0]),
#  ([0,1],[1]),
#  ([1,0],[1]),
#  ([1,1],[0])
#  ]
# xor.train(XOR_Data, iters=2000,print_interval=200)

# print(xor.test_with_expected(XOR_Data))
# print(xor.evaluate([1,1]))

print("<<<<<<<<<<<<<< Voter Data >>>>>>>>>>>>>>\n")

voter_data = [
    ([.9, .6, .8, .3, .1], [1]),
    ([.8, .8, .4, .6, .4], [1]),
    ([.7, .2, .4, .6, .3], [1]),
    ([.5, .5, .8, .4, .8], [0]),
    ([.3, .1, .6, .8, .8], [0]),
    ([.6, .3, .4, .3, .6], [0])
]
voter=NeuralNet(5,6,1)
voter.train(voter_data)
#print(voter.test_with_expected(voter_data))
print(voter.test([
    [1, 1, 1, .1, .1],
    [.5, .2, .1, .7, .7],
    [.8, .3, .3, .3, .8],
    [.8, .3, .3, .8, .3],
    [.9, .8, .8, .3, .6]
]))
    