def lcg(rand, const, mod):
  return (rand * const['mul'] + const['add']) % mod

def jump_lcg(const, mod, power):
  if power < 2: return const
  square = {'mul': const['mul'] ** 2 % mod, 'add': (const['mul'] + 1) * const['add'] % mod}
  square = jump_lcg(square, mod, power/2)
  if power % 2 == 0: return square
  return {'mul': square['mul'] * const['mul'] % mod, 'add': (square['mul'] * const['add'] + square['add']) % mod}

rand = 0x1a56b091
const = {'mul': 0x41c64e6d, 'add': 0x6073}
mod = 2**32

# print(hex(rand))

print(0, '-' * 3, str(rand).rjust(10), '-' * 3, f"{rand:#0{10}x}")
print(const)
print("-" * 40)

for x in range(1,10):
  rand = lcg(rand, const, mod)
  print(x, '-' * 3, str(rand).rjust(10), '-' * 3, f"{rand:#0{10}x}")

print("-" * 40)

power = 2**32 - 1
const = jump_lcg(const, mod, power)
print(0, '-' * 3, str(rand).rjust(10), '-' * 3, f"{rand:#0{10}x}")
print(const)

print("-" * 40)

for x in range(1,10):
  rand = lcg(rand, const, mod)
  print(x, '-' * 3, str(rand).rjust(10), '-' * 3, f"{rand:#0{10}x}")