# task 1
# a=int(input("Insert a: "))
# for i in range(a):
#     b=((i+1)**3)
#     print("Number is:",i+1," and cube if the ",i+1," is ",b)

# task 2

# a=list(map(int,input().split()))
# a.reverse()
# for i in range(len(a)):
#     print(a[i])
# task 3
# a=int(input())
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(fact)

# task 4
# a=int(input())
# sum=0
# for i in range(1,a+1):
#     sum=sum+i
#
# print(sum)

# task 5
# a=int(input())
# temp=a
# b=0
# while a>0:
#     c=a%10
#     a=a//10
#     b=b*10+c
# if(temp==b):
#     print("palindrome")
# else:
#     print("No palindrome")

# task 1
# a=int(input())
# for i in range(a,0,-1):
#     for j in range(0,i):
#         print(i-j,end=" ")
#     print()

# task 2
# a=(int(input()))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()

# task 1
# get_Discount = lambda a,b:(100-b)*a/100
# a=int(input())
# b=int(input())
# print(get_Discount(a,b))

# task 2
# def sum_numbers(n):
#     if n==1:
#         return 1
#     return sum_numbers(n-1)+n
# a=int(input())
# print(sum_numbers(a))