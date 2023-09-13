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
    
    var sum = 0;
    for (let i = 0; i < parsedBets.length; i ++) {
        sum += parsedBets[i];
    }

    // 如果總和加起來小於等於22
    if (sum <= 22) {
        return 1;
    }
  
    return -1;
  }
  
  // QA請勿複製這段
  module.exports = judge;
  