#8) How to check if a string is a palindmore or not 
#string = "madam" same forward and backward
#string = "that" reverse string = "taht"
def reverse_string(s):
    start = 0
    end = len(s) - 1
    char_list = list(s)
    while start < end:
        temp = char_list[start]
        char_list[start] = char_list[end]
        char_list[end] = temp
        start += 1
        end -= 1
    return ''.join(char_list)  # Convert the list back to a string

str = "madam"
reversed_str = reverse_string(str)
if reversed_str == str:
    print("Palindrome")
else:
    print("Not Palindrome")
