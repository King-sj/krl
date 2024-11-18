def hash_pjw(s: str) -> int:
  h = 0
  for c in s:
    h = (h << 4) + ord(c)
    g = h & 0xf0000000
    if g != 0:
      h ^= g >> 24
    h &= ~g
  return h
