"""
https://leetcode.com/problems/top-k-frequent-elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Multiple approaches to solve this problem.

1. Counter.most_common(n): returns the list of the top n most frequent elements.

2. Heapq Algorithm: (need to learn)

3. Bucket Sort: (need to learn)

4. Quick select: (need to learn)

"""

from collections import Counter

def topKFrequent1(nums, k):
  freq = Counter(nums)
  top = freq.most_common(k)
  out = []
  for i in range(k):
    out.append(top[i][0])
  return out


def topKFrequent2(nums, k):
  """
  Time Complexity: O(n log k)
  Space Complexity: O(n)
  Approach: Count frequencies, use min-heap of size k
  """
  
  import heapq
  # Count frequencies
  count = Counter(nums)
  # Use heap to keep top k frequent
  # Python heapq is min-heap, so use negative frequencies
  return [num for num, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]



def topKFrequent_bucket3(nums, k):
  """
  Time Complexity: O(n) - Optimal!
  Space Complexity: O(n)

  Approach: Bucket sort by frequency
  """
  # Count frequencies
  count = Counter(nums)

  # Create buckets: bucket[i] contains all numbers with frequency i
  # Max frequency is len(nums)
  buckets = [[] for _ in range(len(nums) + 1)]

  for num, freq in count.items():
    buckets[freq].append(num)

  # Collect top k from highest frequency buckets
  result = []
  for freq in range(len(buckets) - 1, 0, -1):
    for num in buckets[freq]:
      result.append(num)
      if len(result) == k:
        return result
 return result

