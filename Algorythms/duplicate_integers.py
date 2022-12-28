# a = [1,2,3,4,4,4,5,6]
#
#
# def removeDuplicates(self, nums: List[int]) -> int:
#     size = len(nums)
#     insertIndex = 1
#     for i in range(1, size):
#         # Found unique element
#         if nums[i - 1] != nums[i]:
#             # Updating insertIndex in our main array
#             nums[insertIndex] = nums[i]
#             # Incrementing insertIndex count by 1
#             insertIndex = insertIndex + 1
#     return insertIndex

def isValid(s: str) -> bool:
    for el in range(len(s)):
        print(el, s[el + 1])
        if s[el] == '(' and s[el + 1] == ')':
            return True
        elif s[el] == '[' and s[el + 1] == ']':
            return True

        elif s[el] == '{' and s[el + 1] == '}':
            return True
        else:
            return False

print(isValid('()'))