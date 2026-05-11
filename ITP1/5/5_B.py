while True:
  h, w = map(int, raw_input().split())
  if h + w == 0: break

  for y in xrange(h):
    print '#' * w
  print
