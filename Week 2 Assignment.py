#task 1
#learning bin and hex functions?
x = 31
print (x,bin(x), hex(x))

#task 2
#incorrect input error
# with x = 1.825, x becomes a float value, which cannot be translated into a hex value
x = 18
print (x,bin(x), hex(x))

#task 3
#assigning a binary or hex velaue to a variable
y = 0b1011
z = 0xa3
print (y,z)

#task 4
#adding variables in any form
w = x+y+z
print ("the sum is",w)

#task 5
#calculating the result of variables
original_size = 400
dictionary_size = 25
compressed_text_size = 102
compression_decimal = (1 - ((compressed_text_size + dictionary_size) / original_size))
#changing the compression decimal to have 2 decimal places and look more like a percent value
compression_percent = f"{(compression_decimal) * 100:.2f}"
print ('Compressed text size:', str(compressed_text_size), 'characters')
print ('     Dictionary size:', str(dictionary_size), 'characters')
print ('               Total:', str(dictionary_size + compressed_text_size), 'characters')
print ('  Original text size:', str(original_size), 'characters')
print (f"         Compression: {compression_percent}%")


