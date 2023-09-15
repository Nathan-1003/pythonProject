function judge(bets) {

  //限制彩球三顆
  if (bets.length != 3) {
    return -1;
  }
  var parsedBets = bets.map(function (item) {
    return parseInt(item, 10);
  });

  //限制彩球號碼 0 - 9
  for (let i = 0; i < parsedBets.length; i++) {
    if (parsedBets[i] < 0 || parsedBets[i] >= 10) {
      return -1;
    }
  }

  const target = [15,17,19,21,23,25,27]

  var sum = parsedBets.reduce(function (acc, curr) {
    return acc + curr;
  }, 0);

  if(target.includes(sum)){
    return 1;
  }
  return -1;
}


// QA請勿複製這段
module.exports = judge;