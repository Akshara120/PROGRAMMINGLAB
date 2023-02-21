#statistics module
import statistics as s
list1=[20,40,60,40,80,100]
print("mean :",s.mean(list1))
print("median :",s.median(list1))
print("mode :",s.mode(list1))
print("Harmonic mean:",s.harmonic_mean(list1))
print("statistics varience:",s.variance(list1))
print()
print("statistics median Low:",s.median_low([1,3,5,7,9,11,13]))
print("statistics median Low:",s.median_low([1,3,5,7,9,11]))
print("statistics median Low:",s.median_low([-11,5.5,-3.4,7.1,-9,22]))
