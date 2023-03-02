const solution = (n, k) => {
  if (k >= Math.floor(n / 10)) {
    k -= Math.floor(n / 10);
  }

  return 12000 * n + 2000 * k;
};
