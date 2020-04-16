require(tidyverse)
require(dplyr)
require('latticeExtra')
setwd("C:/Users/Techy/Anaconda3/envs/poltweet/My Stuff/Data")
temp <- list.files(pattern='([^-]*)_') %>%
    str_extract("([^-]*)_") %>%
    unique()
rootnumcases = ceiling(sqrt(length(temp)))
par(mfrow = c(rootnumcases,rootnumcases))
#### TODO 
#### iterate over temp, graphing both price and polarity somehow on the same graph
#### where you can visually see the (probably lack of) correlation
for (i in temp){
    pol <- list.files(pattern=i) %>%
    lapply(read.csv)
    data <- data.frame(pol[[1]]$Date,pol[[1]]$Polarity,pol[[2]]$Price)
    obj1 <- xyplot(data$pol..1...Polarity ~ data$pol..1...Date, type = 'l',main=str_remove(i,"_"),xlab="Date",ylab="Polarity",horizontal=FALSE,las=2)
    obj2 <- xyplot(data$pol..2...Price ~ data$pol..1...Date, type = 'l',ylab="Stock Price Per Share")
    print(doubleYScale(obj1,obj2, add.ylab2 = TRUE, use.style=FALSE))
}