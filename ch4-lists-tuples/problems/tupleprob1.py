# Check that a tuple type cannot be changed in python.

a = (2,4,"hii")

a[2]="hello"  # TypeError: 'tuple' object does not support item assignment