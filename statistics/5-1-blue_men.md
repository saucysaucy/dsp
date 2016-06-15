[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34.2746837631 percent of the male population is in the range to be in the blue man group.


```python
mew = 178
sigma = 7.7
x1 = (5+10/12)*30.48
x2 = (6+1/12)*30.48
dist = stats.norm(loc = mew,scale = sigma)
print("%s percent of the male population is in the range to be in the blue man group." % ((dist.cdf(x2)-dist.cdf(x1))*100))
```
