class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotic increasing stack of indices
        # i.e. index value can stay the same or increase
        # when we see a bar lower than the stack top, we 'close' rectangles
        stack = [-1] # sentinel index to simplify width calculation
        best = 0

        for i, h in enumerate(heights):
            # maintain increasing heights in the stack
            while stack[-1] != -1 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # width is between the new stack top + 1 and i - 1
                width = i - stack[-1] - 1
                best = max(best, height * width)
            stack.append(i)
        
        # close any remaining rectangles to the end
        n = len(heights)
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            best = max(best, height * width)
        
        return best
