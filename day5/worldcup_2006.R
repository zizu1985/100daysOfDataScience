# What is the scale of X ? X variable has continous scale (with ratio subscale)


?hist
goals<-c(6,24,91,8,4,25,3,83,89,34,25,24,18,6,23,10,28,4,63,6,60,5,40,2,22,26,23,26,44,49,34,2,33,9,16,55,23,13,23,13,23,4,8,26,70,4,6,60,23,95,28,49,6,57,33,56,7)
hist(goals,freq = FALSE,xlab ='Goal scored minute', ylab='Relative Frequency [%]')

# ECDF for original data
plot.ecdf(goals) # ECDF as stepped function 

# ECDF for grouped data
plot.ecdf()
?plot.stepfun

goals_cat <- cut(goals,breaks = c(0,15,30,45,60,75,90,96),labels=c(15,30,45,60,75,90,96))
cdf_goals_cat <- ecdf(as.numeric(as.character(goals_cat)))
plot.ecdf(cdf_goals_cat)

# g
# Determine the proportion of first goals which occured in firt half ==> H(x<=45)
cdf_goals_cat(45)
# 0.776
# Determine the proportion of first goals which occured during in the last 10 min or during extra time == H(X>80) = 1 - F(80) = 1 - 0.93 = 0.07
1 - cdf_goals_cat(80)

# Determine proportion of first goals which occured between 20th and 65th min ==> H(20 <= X <= 65)
# ==> H(20 <= X <= 65) = F(65) - F(20) + f(20)

cdf_goals_cat(65) - cdf_goals_cat(20) + 14/55 = 0.80

# Determine the time point at which in 80% of the mathces the first goals was scored at ot before time point
# Calculate sum(fi) and stop when >= 0.8, next 
goals_cat[which(cdf_goals_cat(goals_cat) == 0.8)] 
# 50.4 min
