function solveSingle(arr){
    arr = arr.slice();
    while(arr.length-1){
      if(arr[1] === '*') arr[0] = arr[0] * arr[2]
      if(arr[1] === '-') arr[0] = arr[0] - arr[2]
      if(arr[1] === '+') arr[0] = +arr[0] + (+arr[2])
      if(arr[1] === '/') arr[0] = arr[0] / arr[2]
      arr.splice(1,1);
      arr.splice(1,1);
    }
    return arr[0];
  }
  
  function solve(eq) {

    let res = eq.split(/(\+|-)/g).map(x => x.trim().split(/(\*|\/)/g).map(a => a.trim()));
    console.log(res)
    res = res.map(x => solveSingle(x)); //evaluating nested * and  / operations.
     
    return solveSingle(res) //at last evaluating + and -
    
    
  }
  
  console.log(solve("3 - 6 * 3 / 9 + 5")); //6
  console.log(eval("3 - 6 * 3 / 9 + 5")) 