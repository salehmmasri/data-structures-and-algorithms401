
# find maximum value

## problem domain
* Write an instance method called find-maximum-value that return the maximum value stored in the tree. You can assume that the values stored in the Binary Tree.

## visual
![max](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-16/binary-tree.png
)

## Output
> `11`

## Approach & Efficiency
* big O() = O(N)

# algorithm
- create a function to find the max number in the tree 
- create a 2 variable output and tree_data and make the tree_data =  self.preOrder() which return an array
- then I use loop to find the max value inside this array 

## code 
> you can open the tree folder that located inside data_structures_and_algorithms401  folder 