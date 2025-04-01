'''Task: If we encounter //, /* or */ ignore that line in the list

create a new list to hold the source code without the comments

source_code_without_comments = {}

iterate through each character of each element in source and looking for one of 
the comment blocks.

create a flag denoting if we encounter /* so we ignore all lines until we find */

if we find // only ignore that line

in_comment_block = False

nested loop

if (source[i] == "/" and source[i + 1] == "/") and not in_comment_block:
    skip this line
elif (source[i] == "/" and source[i + 1] == "*") and not in_comment_block:
    in_comment_block = True
    skip all characters till we find the closing comment
elif (souce[i] == "*" and source[i + 1] == "/") and in_comment_block:
    in_comment_block == False
    skip i + 1 character and continue adding to the no comment list
elif not in_block_comment:
    add to source[i] to temp variable

append temp var to source_code_without_comments 
reset the temp var for the next line
return source_code_without_comments
'''

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        source_code_without_comments = []
        in_comment_block = False
        temp = ''

        for code in source:
            i = 0
            while i < len(code):

                if code[i] == '/' and (i + 1) < len(code) and code[i + 1] == '/' and not in_comment_block:
                    i = len(code)
                elif code[i] == '/' and (i + 1) < len(code) and code[i + 1] == '*' and not in_comment_block:
                    in_comment_block = True
                    i += 1
                elif code[i] == '*' and (i + 1) < len(code) and code[i + 1] == '/' and in_comment_block:
                    in_comment_block = False
                    i += 1
                elif not in_comment_block:
                    temp += code[i]
            
                i += 1
            if temp and not in_comment_block:
                source_code_without_comments.append(temp)
                temp = ''
        return source_code_without_comments

            
