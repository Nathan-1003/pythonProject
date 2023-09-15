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


  //排序(正反都算順子)
  parsedBets.sort(function (a, b) {
    return a - b;
  });

  const central = parsedBets[1]

  if(parsedBets[0] === central-1 && parsedBets[2] === central+1){
    return 1;
  }

  return -1;
}


// QA請勿複製這段
module.exports = judge;