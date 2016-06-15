[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

> Results <br />

>> Effective weight difference (first minus others): -0.08867236333202932 <br />
Effective length difference (first minus others): 1.0930083433621403 <br /><br />
The first born babies were statistically lighter than the other babies, but only by .09 standard deviations or
about a twentieth of a pound difference. <br /> <br />
>> The pregnancy duration differs tremendously where first born babies tend to have longer pregnancies by 1.1
standard deviations or about 14 weeks.<br /> <br />
>> Comparing first and "other" born deviations independently, there it can been seen that first born babies have a
more predictable pregnancy duration while "other" born on average are shorter, but are generally more unpredictable.



```python
preg = nsfg.ReadFemPreg()
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
first_wgt = preg[preg['birthord']==1.0]['totalwgt_lb']
other_wgt = preg[preg['birthord']!=1.0]['totalwgt_lb']

first_wgt = first_wgt[first_wgt.notnull()]
other_wgt = other_wgt[other_wgt.notnull()]


first_len = preg[preg['birthord']==1.0]['prglngth']
other_len = preg[preg['birthord']!=1.0]['prglngth']

first_len  = first_len[first_len.notnull()]
other_len = other_len[other_len.notnull()]

print(first_wgt.mean(),other_wgt.mean(),sep='\t')
print(first_wgt.std(),other_wgt.std(),sep='\t')
print()
print(first_len.mean(),other_len.mean(),sep='\t')
print(first_len.std(),other_len.std(),sep='\t')
print("Effective weight difference (first minus others): %s" % CohenEffectSize(first_wgt,other_wgt),
     "Effective length difference (first minus others): %s" % CohenEffectSize(first_len,other_len),sep = '\n')
```