v2014 = c(rep('ANC',6215),rep('DA',2223),rep('EFF',635),rep('IFP',240),rep('COPE',67),rep('Others',620))
v2014
v2009 = c(rep('ANC',6590),rep('DA',1666),rep('EFF',1),rep('IFP',455),rep('COPE',742),rep('Others',547))
v2009
barplot(table(v2014)/length(v2014),beside=T)
barplot(table(v2009)/length(v2009),beside=T)
?barplot


library(plotly)
Labels <- c("ANC","COPE","DA","EFF","IFP","Others")
v1 <- table(v2014)/length(v2014)
v1
v2 <- table(v2009)/length(v2009)
v2
dat <- data.frame(Labels,v1,v2)
dat

table(v2009)/length(v2009)

fig <- plot_ly(dat, x = ~Labels, y = ~v1, type = 'bar', name = 'v2014')
fig <- fig %>% add_trace(y = ~v2, name = 'v2009')

fig


        