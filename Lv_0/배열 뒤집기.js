// 1
const solution1 = (num_list) => {
  let ans = [];
  for (let i = num_list.length - 1; i > -1; i--) {
    ans.push(num_list[i]);
  }

  return ans;
};

// 2
const solution2 = (num_list) => {
  num_list.reverse();
  return num_list;
};
