def hanoi(n,from_pole,to_pole,with_pole):
    if n>=1:
        hanoi(n-1,from_pole,with_pole,to_pole)
        #move(from_pole,to_pole)
        print(from_pole,'-->',to_pole)
        hanoi(n-1,with_pole,from_pole,to_pole)


