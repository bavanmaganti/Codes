This algoritm is to find max contagious subarry sum

nums=[-2, -3, 4, -1, -2, 1, 5, -3]
start=end=0
cm=nums[0]
cs=nums[0]
for n in range(1,len(nums)):
    cs=max(nums[n],cs+nums[n])
    if cs==nums[n]:
        tstart=n
    if cs>cm:
        start=tstart
        end=n
        cm=cs
print(start,end)
print(nums[start:end+1])
print(cm)