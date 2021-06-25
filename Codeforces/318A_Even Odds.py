n, k = map(int, input().split())
if n % 2 == 0:  # amount of even and odd numbers are equal
    if k <= (n / 2):  # i don't need even numbers. odds will work
        print(1 + (2 * (k - 1)))  # k = 3. so, 1 occupies one K, rest 2k's are multiplied and printed to save memory and time
    if k > (n / 2):  # i don't need odds, just evens will do.
        print(int(2 + (k - (n / 2) - 1) * 2))  # eleminating the amount of odd values from k. for 10, odd amount of numbers are 5. eleminating 5 from 9, gives us 4, so, k = 4, 2 is one even number. That i am using manually, gives us k = 3. so, 2*3 = 6 and 6+2 = 8. Viola!
if n % 2 == 1:  # amount of odd number is greater than amount of even number.
    if (k <= (n // 2) + 1):  # i dont need even numbers. Only odds will do.
        print(1 + (2 * (k - 1)))
    if (k > (n // 2) + 1):  # i dont need odd numbers. only even will do.
        print(int(2+(k-((n//2)+1+1))*2))
