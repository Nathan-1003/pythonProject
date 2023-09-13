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
    
    // 龍為第一球，虎為第五球
    var dragon = parsedBets[0];
    var tiger = parsedBets[4];

    // 和
    if (dragon == tiger) {
        return 1;
    }
    
  
    return -1;
  }
  
  // QA請勿複製這段
  module.exports = judge;
  