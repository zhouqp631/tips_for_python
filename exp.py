buy1 = Decay_linear(close,0.3,10)>Decay_linear(close,0.3,20);
buy2 = Decay_linear(delay(close,1),0.3,10)<decay_linear(delay(close,1),0.3,10);


sell1 = Decay_linear(delay(close,1),0.3,10)>Decay_linear(delay(close,1),0.3,20);
sell2 = Decay_linear(close,0.3,10)<Decay_linear(close,0.3,20);


# sd = StdDev(log(close/delay(close,1)),20);
(buy1 && buy2)?1:((sell1 && sell2)?-1:0)


(buy1 && buy2)?-correlation(sd,returns,5):((sell1 && sell2)?-rank(returns):0)




buy1 = decay_exp(close,0.3,5)>decay_exp(close,0.3,8);
buy2 = decay_exp(delay(close,1),0.3,5)<decay_exp(delay(close,1),0.3,8);
sell1 = Decay_exp(delay(close,1),0.3,5)>decay_exp(delay(close,1),0.3,8);
sell2 = Decay_exp(close,0.3,5)<decay_exp(close,0.3,8);
(buy1 && buy2)?1:((sell1 && sell2)?-1:0)
