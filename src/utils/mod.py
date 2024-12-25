def hash_pjw(s: str) -> int:
  """
  Computes the PJW (Peter J. Weinberger) hash of a given string.

  The PJW hash function is a simple and effective hash function that
  processes each character of the input string and combines their
  ASCII values to produce a hash value.

  Args:
    s (str): The input string to be hashed.

  Returns:
    int: The resulting hash value.
  """
  h = 0
  for c in s:
    h = (h << 4) + ord(c)
    g = h & 0xf0000000
    if g != 0:
      h ^= g >> 24
    h &= ~g
  return h
