n, k = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
count = 0
smaller_counts = []

for i in range(len(nums2)):
    while count < n and nums2[i] > nums1[count]:
        count += 1
    smaller_counts.append(count)

print(" ".join(map(str, smaller_counts)))
