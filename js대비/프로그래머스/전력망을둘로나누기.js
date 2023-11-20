function solution(n, wires) {
  var answer = n;
  var graph = {};
  for (let i = 1; i <= n; i++) {
    graph[i] = [];
  }

  wires.forEach((wire) => {
    let [a, b] = wire;
    graph[a].push(b);
    graph[b].push(a);
  });

  const dfs = (a, b, check) => {
    for (let i = 0; i < graph[a].length; i++) {
      if (check[graph[a][i]] !== 1 && graph[a][i] !== b) {
        check[graph[a][i]] = 1;
        dfs(graph[a][i], b, check);
      }
    }
    return check.filter((e) => e > 0).length;
  };
  for (wire of wires) {
    let [a, b] = wire;
    let check = Array(n + 1).fill(0);
    check[a] = 1;
    let cnt = dfs(a, b, check);
    let diff = Math.abs(n - 2 * cnt);
    answer = Math.min(answer, diff);
  }
  return answer;
}
