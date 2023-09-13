function judge(bets) {
    if (bets.length != 5) {
      return -1;
    }
    var parsedBets = bets.map(function (item) {
      return parseInt(item, 10);
    });
  
    for (let i = 0; i < parsedBets.length; i ++) {
      if (parsedBets[i] < 0 || parsedBets[i] > 9) {
        return -1;
      }
    }
    
    // 第三球為2即為true
    var ball = parsedBets[2];
    if (ball == 2) {
      return 1;
    }
  
    return -1;
  }
  
  // QA請勿複製這段
  module.exports = judge;
  