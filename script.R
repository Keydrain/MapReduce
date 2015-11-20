x = seq(0, 20)
y = seq(0, 20)

png('graph1.png', width = 900, height = 500)
par(mfrow = c(1,1),
    oma = c(6,6,0,0) + 0.1,
    mar = c(0,0,1,1) + 0.1)
w = 1
plot(x^4 ~ y, type='l', col='red', lwd=5, cex.axis = 2)
lines((x^4/w^4) + w^3 ~ y, col='blue', lwd=5)
title(xlab = "Dimensionality of the Problem",
      ylab = "Run Time",
      outer = TRUE, line = 3, cex.lab = 2)
dev.off()

png('graph2.png', width = 900, height = 500)
par(mfrow = c(1,1),
    oma = c(6,6,0,0) + 0.1,
    mar = c(0,0,1,1) + 0.1)
w = 2
plot(x^4 ~ y, type='l', col='red', lwd=5, cex.axis = 2)
lines((x^4/w^4) + w^3 ~ y, col='blue', lwd=5)
title(xlab = "Dimensionality of the Problem",
      ylab = "Run Time",
      outer = TRUE, line = 3, cex.lab = 2)
dev.off()

png('graph3.png', width = 900, height = 500)
par(mfrow = c(1,1),
    oma = c(6,6,0,0) + 0.1,
    mar = c(0,0,1,1) + 0.1)
w = 5 
plot(x^4 ~ y, type='l', col='red', lwd=5, cex.axis = 2)
lines((x^4/w^4) + w^3 ~ y, col='blue', lwd=5)
title(xlab = "Dimensionality of the Problem",
      ylab = "Run Time",
      outer = TRUE, line = 3, cex.lab = 2)
dev.off()
