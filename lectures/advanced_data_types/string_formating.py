def custom(a, b):
    return a + b * a

number_of_balloons = custom(4, 4)

print('Andy has {} balloons'.format(number_of_balloons))
print('Andy has {1} balloons and {0} bikes'.format(number_of_balloons, 3))
print('Andy has to create {1} {0} and open {var}'.format(1, 'review', var='pull request'))
print('Andy has to create {count} {test} and open {var}'.format(count=1, test='review', var='pull request'))
print('Andy has {0:4} balloons and {1:10} bikes'.format(number_of_balloons, 'has no'))
print('Andy has {0:4} balloons and {1:10} bikes'.format(400, 'has no'))
print('Andy has {0:4} balloons and {1:10} bikes'.format(4000, 'has no'))

bikes = 5
count = 1
test = 'review'
var = 'pull request'
print(f'Andy has {number_of_balloons} balloons')
print(f'Andy has {number_of_balloons} balloons and {bikes} bikes')
print(f'Andy has to create {count} {test} and open {var}')

name = 'Rostyslav'
print('Hey %s. How are you?' % name)
