require(tidyverse)
require(dplyr)
setwd("C:/Users/Techy/Anaconda3/envs/poltweet/My Stuff/Data")
temp <- list.files(pattern='([^-]*)_') %>%
    str_extract("([^-]*)_") %>%
    unique()
rootnumcases = ceiling(sqrt(length(temp)))
par(mfrow = c(rootnumcases,rootnumcases))
#### TODO 
#### iterate over temp, graphing both price and polarity somehow on the same graph
#### where you can visually see the (probably lack of) correlation