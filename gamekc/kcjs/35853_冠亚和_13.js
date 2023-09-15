function judge(bets) {
    if (bets.length != 10) {
      return -1;
    }
    var parsedBets = bets.map(function (item) {
      return parseInt(item, 10);
    });
  
    for (let i = 0; i < parsedBets.length; i ++) {
      if (parsedBets[i] < 1 || parsedBets[i] > 10) {
        return -1;
      }
    }
    
    var first = parsedBets[0]; // 冠
    var second = parsedBets[1]; // 亞

    // 冠 + 亞 = 13
    var sum = first + second;
    if (sum == 13) {
      return 1;
    }
  
    return -1;
  }
  
  // QA請勿複製這段
  module.exports = judge;
  