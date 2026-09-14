class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n = len(nums)

        # Find first index to the right with a smaller value
        next_smaller = [n] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)

        # Process indices by value, from large to small.
        # Fenwick contains positions whose value is > current value.
        order = sorted(range(n), key=lambda i: nums[i], reverse=True)

        bit = [0] * (n + 1)

        def add(i):
            i += 1
            while i <= n:
                bit[i] += 1
                i += i & -i

        def query(i):
            # Number of active positions [0, i)
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        p = 0

        while p < n:
            q = p

            # Same values must NOT be active yet,
            # because we need nums[j] > nums[i].
            while q < n and nums[order[q]] == nums[order[p]]:
                q += 1

            # Query all indices having this value
            for t in range(p, q):
                i = order[t]

                r = next_smaller[i]

                # Positions (i, r)
                # having value strictly greater than nums[i]
                ans += query(r) - query(i + 1)

            # Now activate this value for smaller values
            for t in range(p, q):
                add(order[t])

            p = q

        return ans