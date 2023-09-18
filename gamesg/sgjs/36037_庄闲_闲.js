/**
 * 26,20,21,5,1,29,40,5,1
 * 前面3个数字是闲的牌型， 
	- 第4个数字是闲的点数
	- 第5-7个数字是庄的牌型
	- 第8 个数字是庄的点数
	最后一个数字是哪方赢。 0:庄赢，1:闲赢， 2:和
 * @param bets
 * @returns
 */
function judge(bets) {

  //限制彩球9顆
  if (bets.length != 9) {
    return -1;
  }
  var parsedBets = bets.map(function (item) {
	    return parseInt(item, 10);
  });

  //限制彩球號碼 1 - 52
  for (let i = 0; i < parsedBets.length; i++) {
    if (parsedBets[i] < 1 || parsedBets[i] > 52) {
      return -1;
    }
  }
  
  var result = parsedBets[8];
  if (result == 1 ) {
      return 1;
  }
  return -1;

}


//QA請勿複製這段
module.exports = judge;