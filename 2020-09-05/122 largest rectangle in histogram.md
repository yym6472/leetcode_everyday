## 题意

- 链接：[https://www.lintcode.com/problem/largest-rectangle-in-histogram/description](https://www.lintcode.com/problem/largest-rectangle-in-histogram/description)

题意为给定一个数组，表示直方图每一列的高度。需要从直方图中找出面积最大的一个矩阵。例如对于直方图`[2,1,5,6,2,3]`而言，在第三列和第四列选取一个`5*2`的矩阵，面积为`10`，是这个直方图中的最大矩阵。

## 题解

直观的想法是，对于每一个元素（每一列），我们分别将该元素的高作为矩阵的高，然后找到其左边和右边第一个比它小坐标位置，相减即得到矩阵的宽，如此便可以直接得到面积。
按照这种方法，求解每一个元素需要`O(n)`的时间复杂度，若需要求最大值，则需要枚举每一个元素，因此需要`O(n^2)`的复杂度。

现在我们希望有一种方法能够从左到右扫一遍，就直接把每一列左边/右边的第一个小于该元素的坐标位置都找出来。
我们要找的这两个元素，一个在当前目标的左边，另一个在当前目标的右边（废话）。之后就把这两个位置称为当前元素的**左边界**和**右边界**吧。这就是我们对每一个元素要求的值。

如果从左到右扫一遍数组的话，当处理一个元素的时候，我们一方面可以**立刻得知该元素的左边界**（因为左边的元素已经被处理过了），另一方面需要将**以当前元素为右边界的之前元素一一处理**。

因此，我们需要使用维护一个数据结构，一方面可以在`O(1)`的时间复杂度内得到当前元素左边第一个比其小的元素；另一方面，可以在`O(1)`时间复杂度内，一一处理以当前元素为右边界（右边第一个比其小的数）的其他元素，记录它们的右边界为当前元素。
并且，这些处理完的元素就可以丢掉不再维护了，因为**之后的数不再可能是其右边界**。

在遍历数组的过程中，我们需要维护一个之前元素的单增序列。当处理每一个元素的时候：
- 我们在序列的右边逐一弹出比该元素大的元素，这些元素就是**以当前元素为右边界**的之前元素；
- 弹出完毕后，我们发现此时序列的最右边元素就是**当前元素左边第一个比其小**的元素；
- 将当前元素放进右边，继续维护单增的结构即可；

以上操作需要：右边push、右边pop、右边peak，因此使用一个栈即可。当所有元素处理完毕时，栈中可能还存有元素，需要依次弹出栈的元素，此时弹出的元素没有右边界（或者右边界就是直方图的右边界）。

有几点需要注意的地方：
1. 相等情况的处理：
   - 当栈顶元素和当前要入栈的元素相等时，这种情况栈顶元素不应该弹出。因为当前元素并不是该元素的右边界（右边界需要是右边第一个比其**小**的元素）
   - 当前元素入栈时，若栈中仍包含与当前元素相等的元素，那么当前元素记录的左边界应该就是栈顶元素记录的左边界，因为它们彼此高度相同（并且之间的所有列都比它们高），因而共享左边界；否则的话（栈顶元素小于当前元素），则当前元素的左边界应该设置为栈顶元素对应的下标+1，因为栈顶元素是左边第一个比当前元素小的元素。
2. 第一个元素入栈，以及最后留在栈中元素的特殊处理：
   - 对于第一个元素，是没有左边界的，或者说，它的左边界就是直方图的左边界（即`0`）
   - 对于最后留在栈中的元素来说，它们是没有右边界的，或者说，它们的右边界就是直方图的右边界（即`len(x)`）
   为了避免特殊处理，我在初始的`height`数组两端分别追加了`-1`能保证最后留在栈中的只有两个`-1`，而实际有意义的元素都被处理一遍了。