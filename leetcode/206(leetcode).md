# 206. Reverse Linked List.py

## solution
1[solution](206(leetcode).py)


> 判斷條件：current.next 不等於 None
>> current 指著前面 curNext 指後面

>>temp 比current 慢一步

>>用temp寄你要指向的東西

先讓current 等於 head

curNext 等於 current.next

temp等於current

先把current,curNext往右移一格

把current.next往左指向temp

完成指向方向的reverse


再把temp更新成current

此時temp,current指向同一個node:w
