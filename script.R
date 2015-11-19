x = seq(0, 20)
y = seq(0, 20)

png('graph.png')
par(mfrow = c(3,1),
    oma = c(6,6,0,0) + 0.1,
    mar = c(0,0,1,1) + 0.1)
w = 1
plot(x^4 ~ y, type='l', col='red', xaxt='n', lwd=5)
lines((x^4/w^4) + w^3 ~ y, col='blue', lwd=5)
w = 2
plot(x^4 ~ y, type='l', col='red', xaxt='n', lwd=5)
lines((x^4/w^4) + w^3 ~ y,col='blue', lwd=5)
w = 5
plot(x^4 ~ y, type='l', col='red', lwd=5)
lines((x^4/w^4) + w^3 ~ y, col='blue', lwd=5)
title(xlab = "Dimensionality of the Problem",
      ylab = "Run Time",
      outer = TRUE, line = 3, cex.lab = 2)
dev.off()