function fibonacci(n) {
    if (n <= 0) return 0;
    if (n === 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
  
  function fibonacciSequence(n) {
    let seq = [];
    for (let i = 0; i < n; i++) {
      seq.push(fibonacci(i));
    }
    return seq;
  }
  
  console.log(fibonacciSequence(10));
  