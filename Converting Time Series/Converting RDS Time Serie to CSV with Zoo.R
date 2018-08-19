# R has many datasets that are not available for Python. Using this quick code, I was able to convert the Wine Data Time Series
# (wineind.RDS) into a CSV that can be used with Python

library(lubridate)
library(zoo)
library(xts)

wineind <- readRDS('wineind.RDS', refhook = NULL)

monyear.to.date <- function(x)
  return(dmy(paste("01-", x , sep ="")))

zooA = as.zoo(wineind, order.by = row.names(wineind))
dat_xts <- as.xts(zooA)
index(zooA) <- monyear.to.date(index(zooA))
write.csv(zooA, file = 'Wine_Sales_R_Dataset.csv', row.names = TRUE,col.names = NULL)
