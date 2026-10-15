# Sieve of Eratosthenes - Hint

## Algorithm

- Make a boolean list of length `n + 1`, all `True`, then mark `0` and `1` as `False`
- For each `i` from `2` up to `√n` that is still marked `True`, mark every multiple of `i` starting at `i²` (`i²`, `i² + i`, `i² + 2i`, …) as `False`
- The primes are the indices still marked `True`

## Note

Starting at `i²` is safe because every smaller multiple of `i` was already crossed out by a smaller prime.
