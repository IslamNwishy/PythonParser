#FileName: PythonParser.py
#Name: Islam Osama Nwsihy

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

#Adds a space between each whole number and any symbol around it
def addSpaceTo(expr):
    h=0
    for c in expr:
        if c != ' ':
            if c.isdigit() is False:
                expr=expr[:h+1] + ' ' + expr[h+1:]
                h+=1
            elif expr[h+1].isdigit() is False:
                expr=expr[:h+1] + ' ' + expr[h+1:]
                h+=1
        h+=1
    return expr

#Parses a given of a simple infix mathimatical expression
def Parse(expr):

    #Spaces are added to guarantee a correct split of the stings
    expr=addSpaceTo(expr)
    term = expr.split()
    ParseStack = Stack()
    Tree = BinaryTree('')
    ParseStack.push(Tree)
    currentTree = Tree
    for i in term:
        if i == '(':
            currentTree.insertLeft('')
            ParseStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = ParseStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            ParseStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = ParseStack.pop()
        else:
            raise ValueError
    return Tree


COUNT = [8] #COUNT Controls the number of spaces between each level
#Given a root to a tree it prints the entire tree in a way that is 
#easier to visualize
def printTree(root, space) : 
  
    # Base case  
    if (root == None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    printTree(root.getRightChild(), space)  
  
    # Print current node after space  
    # count  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.key)  
  
    # Process left child  
    printTree(root.getLeftChild(), space)  

ParseTree = Parse("(((10+5)*3)/(27+9))")
printTree(ParseTree,0)
